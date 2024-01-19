from __future__ import annotations

import re
from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from typing import Any
from typing import Dict
from typing import List
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union

from stubgen.log import get_logger

logger = get_logger(__name__)

T = TypeVar("T")

JsonType = Union[None, int, float, str, Sequence, Mapping]


class DocDict:
    doc_tree: Mapping[str, Any]
    imports: Set[str] = set()
    type_vars: Set[str] = set()

    def __init__(self, doc_tree: Mapping[str, Any]):
        self.doc_tree = doc_tree

    @staticmethod
    def split(text: str, indent: int = 0, line_limit: int = 100, prefix: str = "") -> Sequence[str]:
        lines: List[str] = []
        for doc_paragraph in text.splitlines():
            words: List[str] = doc_paragraph.split(" ")
            doc_line: str = ("    " * indent) + words[0]
            for word in words[1:]:
                if len(doc_line) + len(word) + 1 > line_limit:
                    lines.append(doc_line)
                    doc_line = ("    " * indent) + prefix + word
                else:
                    doc_line += " " + word
            lines.append(doc_line)
        return lines

    def get_doc(self, type_str: str, indent: int = 0, line_limit: int = 100) -> Sequence[str]:
        search: str
        doc_dict: Mapping[str, Any] = self.doc_tree
        while True:
            if type_str in doc_dict:
                doc_dict = doc_dict[type_str]
                break
            if "." in type_str:
                search, type_str = type_str.split(".", 1)
            else:
                search = type_str
            if search not in doc_dict:
                return (f'{"    " * indent}""""""',)
            doc_dict = doc_dict[search]

        doc: str = doc_dict.get("doc", "")
        parameters: Mapping[str, str] = doc_dict.get("parameters", {})
        return_str: Optional[str] = doc_dict.get("return", None)
        exceptions: Mapping[str, str] = doc_dict.get("exceptions", {})
        if len(parameters) == 0 and return_str is None and len(exceptions) == 0:
            if doc == "":
                return (f'{"    " * indent}""""""',)
            if "\n" not in doc and 4 * indent + len(doc) + 3 <= line_limit:
                return (f'{"    " * indent}"""{doc}"""',)

        doc = '"""' + doc.replace("\n", "\n\n")
        doc_lines: List[str] = list(self.split(doc, indent, line_limit))

        if len(parameters) > 0 or return_str is not None or len(exceptions) > 0:
            doc_lines.append("")

            for param, param_doc in parameters.items():
                param_str: str = f":param {param}: {param_doc}"
                doc_lines.extend(self.split(param_str, indent, line_limit, "  "))

            if return_str is not None:
                doc_lines.extend(self.split(f":return: {return_str}", indent, line_limit, "  "))

            for exception, exception_doc in exceptions.items():
                param_str: str = f":except {exception}: {exception_doc}"
                doc_lines.extend(self.split(param_str, indent, line_limit, "  "))

        doc_formatted: Mapping[str, Sequence[str]] = doc_dict.get("doc_formatted", {})
        line_index: int = 0
        while line_index < len(doc_lines):
            line: str = doc_lines[line_index]
            for replace_str, replace_seq in doc_formatted.items():
                replace_str = f"%{replace_str}%"
                if replace_str in line:
                    doc_lines[line_index] = line.replace(replace_str, replace_seq[0])
                    for new_line in reversed(replace_seq[1:]):
                        doc_lines.insert(line_index + 1, ("    " * indent) + new_line)
            line_index += 1

        doc_lines.append(("    " * indent) + '"""')
        return tuple(doc_lines)


@dataclass(frozen=True)
class CNamespace:
    name: str
    types: Mapping[str, CTypeDefinition]

    def to_json(self) -> JsonType:
        return {"name": self.name, "types": {k: v.to_json() for k, v in self.types.items()}}

    @classmethod
    def from_json(cls, json: JsonType) -> CNamespace:
        return cls(
            name=json["name"],
            types={k: CTypeDefinition.from_json(v) for k, v in json["types"].items()},
        )


@dataclass(frozen=True)
class CTypeDefinition(ABC):
    name: str
    namespace: Optional[str]

    def __str__(self) -> str:
        name: str = self.name
        if self.namespace is not None:
            name = f"{self.namespace}.{name}"
        return name

    def __lt__(self, other: CField) -> bool:
        return self.name < other.name

    def __le__(self, other: CField) -> bool:
        return self.name <= other.name

    def __gt__(self, other: CField) -> bool:
        return self.name > other.name

    def __ge__(self, other: CField) -> bool:
        return self.name >= other.name

    @abstractmethod
    def to_json(self) -> JsonType:
        pass

    @abstractmethod
    def to_doc_json(self) -> Tuple[str, JsonType]:
        pass

    @abstractmethod
    def to_stub_lines(self, doc_dict: DocDict, indent: int = 0) -> Sequence[str]:
        pass

    @classmethod
    def from_json(cls: Type[T], json: JsonType) -> T:
        type: str = json["type"]
        if type == "class":
            return CClass.from_json(json)
        if type == "struct":
            return CStruct.from_json(json)
        if type == "interface":
            return CInterface.from_json(json)
        if type == "enum":
            return CEnum.from_json(json)
        if type == "delegate":
            return CDelegate.from_json(json)


@dataclass(frozen=True)
class CClass(CTypeDefinition):
    abstract: bool
    generic_args: Sequence[CType]
    super_class: Optional[CType]
    interfaces: Sequence[CType]
    fields: Mapping[str, CField]
    constructors: Mapping[str, CConstructor]
    properties: Mapping[str, CProperty]
    methods: Mapping[str, CMethod]
    events: Mapping[str, CEvent]
    nested: Mapping[str, CTypeDefinition]

    def __str__(self) -> str:
        name: str = self.name
        if self.namespace is not None:
            name = f"{self.namespace}.{name}"
        if len(self.generic_args) > 0:
            generic: str = ", ".join(map(str, self.generic_args))
            name = f"{name}[{generic}]"
        return name

    def to_json(self) -> JsonType:
        return {
            "type": "class",
            "name": self.name,
            "namespace": self.namespace,
            "abstract": self.abstract,
            "generic_args": tuple(sorted(map(CType.to_json, self.generic_args))),
            "super_class": None if self.super_class is None else self.super_class.to_json(),
            "interfaces": tuple(sorted(map(CType.to_json, self.interfaces))),
            "fields": {k: v.to_json() for k, v in self.fields.items()},
            "constructors": {k: v.to_json() for k, v in self.constructors.items()},
            "properties": {k: v.to_json() for k, v in self.properties.items()},
            "methods": {k: v.to_json() for k, v in self.methods.items()},
            "events": {k: v.to_json() for k, v in self.events.items()},
            "nested": {k: v.to_json() for k, v in self.nested.items()},
        }

    def to_doc_json(self) -> Tuple[str, JsonType]:
        doc_dict: Dict[str, Any] = {"doc": "", "doc_formatted": {}}

        members: Sequence[CMember] = (
            *self.fields.values(),
            *self.constructors.values(),
            *self.properties.values(),
            *self.methods.values(),
            *self.events.values(),
        )
        for member in members:
            if member.declaring_type.name == self.name:
                name, json = member.to_doc_json()
                doc_dict[name] = json

        child: CTypeDefinition
        for child in self.nested.values():
            name, json = child.to_doc_json()
            doc_dict[name] = json

        return self.name, doc_dict

    def to_stub_lines(self, doc_dict: DocDict, indent: int = 0) -> Sequence[str]:
        # abstract: bool
        # generic_args: Sequence[CType]
        # super_class: Optional[CType]
        # interfaces: Sequence[CType]
        # fields: Mapping[str, CField]
        # constructors: Mapping[str, CConstructor]
        # properties: Mapping[str, CProperty]
        # methods: Mapping[str, CMethod]
        # events: Mapping[str, CEvent]
        # nested: Mapping[str, CTypeDefinition]

        if self.abstract:
            doc_dict.imports.add("abc.ABC")
        if self.super_class is not None:
            doc_dict.imports.add(self.super_class.import_name)
        for interface in self.interfaces:
            doc_dict.imports.add(interface.import_name)

        # if self.super_class is not None or len(self.interfaces) > 0:
        parents: List[CType] = []
        if self.super_class is not None:
            parents.append(self.super_class)
        parents.extend(self.interfaces)
        class_def: str = f"{'    ' * indent}{self.name}:"
        if len(parents) > 0:
            class_def = (
                f"{'    ' * indent}{self.name}({', '.join(t.simple_name for t in parents)}):"
            )

        lines: List[str] = [
            class_def,
            *doc_dict.get_doc(f"{self.namespace}.{self.name}", indent + 1),
            "",
        ]
        for field in self.fields.values():
            lines.extend(field.to_stub_lines(doc_dict, indent + 1))
        for constructor in self.constructors.values():
            lines.extend(constructor.to_stub_lines(doc_dict, False, indent=indent + 1))

        return lines

    @classmethod
    def from_json(cls: Type[T], json: JsonType) -> T:
        return cls(
            name=json["name"],
            namespace=json["namespace"],
            abstract=json["abstract"],
            generic_args=tuple(map(CType.from_json, json["generic_args"])),
            super_class=CType.from_json(json["super_class"]),
            interfaces=tuple(map(CType.from_json, json["interfaces"])),
            fields={k: CField.from_json(v) for k, v in json["fields"].items()},
            constructors={k: CConstructor.from_json(v) for k, v in json["constructors"].items()},
            properties={k: CProperty.from_json(v) for k, v in json["properties"].items()},
            methods={k: CMethod.from_json(v) for k, v in json["methods"].items()},
            events={k: CEvent.from_json(v) for k, v in json["events"].items()},
            nested={k: CTypeDefinition.from_json(v) for k, v in json["nested"].items()},
        )


@dataclass(frozen=True)
class CStruct(CClass):
    def to_json(self) -> JsonType:
        json: Dict[str, Any] = dict(**super().to_json())
        json["type"] = "struct"
        return json


@dataclass(frozen=True)
class CInterface(CTypeDefinition):
    generic_args: Sequence[CType]
    interfaces: Sequence[CType]
    fields: Mapping[str, CField]
    properties: Mapping[str, CProperty]
    methods: Mapping[str, CMethod]
    events: Mapping[str, CEvent]
    nested: Mapping[str, CTypeDefinition]

    def __str__(self) -> str:
        name: str = self.name
        if self.namespace is not None:
            name = f"{self.namespace}.{name}"
        if len(self.generic_args) > 0:
            generic: str = ", ".join(map(str, self.generic_args))
            name = f"{name}[{generic}]"
        return name

    def to_json(self) -> JsonType:
        return {
            "type": "interface",
            "name": self.name,
            "namespace": self.namespace,
            "generic_args": tuple(map(CType.to_json, self.generic_args)),
            "interfaces": tuple(sorted(map(CType.to_json, self.interfaces))),
            "fields": {k: v.to_json() for k, v in self.fields.items()},
            "properties": {k: v.to_json() for k, v in self.properties.items()},
            "methods": {k: v.to_json() for k, v in self.methods.items()},
            "events": {k: v.to_json() for k, v in self.events.items()},
            "nested": {k: v.to_json() for k, v in self.nested.items()},
        }

    def to_doc_json(self) -> Tuple[str, JsonType]:
        doc_dict: Dict[str, Any] = {"doc": "", "doc_formatted": {}}

        members: Sequence[CMember] = (
            *self.fields.values(),
            *self.properties.values(),
            *self.methods.values(),
            *self.events.values(),
        )
        for member in members:
            if member.declaring_type.name == self.name:
                name, json = member.to_doc_json()
                doc_dict[name] = json

        child: CTypeDefinition
        for child in self.nested.values():
            name, json = child.to_doc_json()
            doc_dict[name] = json

        return self.name, doc_dict

    def to_stub_lines(self, doc_dict: DocDict, indent: int = 0) -> Sequence[str]:
        return ()

    @classmethod
    def from_json(cls: Type[T], json: JsonType) -> T:
        return cls(
            name=json["name"],
            namespace=json["namespace"],
            generic_args=tuple(sorted(map(CType.from_json, json["generic_args"]))),
            interfaces=tuple(map(CType.from_json, json["interfaces"])),
            fields={k: CField.from_json(v) for k, v in json["fields"].items()},
            properties={k: CProperty.from_json(v) for k, v in json["properties"].items()},
            methods={k: CMethod.from_json(v) for k, v in json["methods"].items()},
            events={k: CEvent.from_json(v) for k, v in json["events"].items()},
            nested={k: CTypeDefinition.from_json(v) for k, v in json["nested"].items()},
        )


@dataclass(frozen=True)
class CEnum(CTypeDefinition):
    fields: Sequence[str]

    def to_json(self) -> JsonType:
        return {
            "type": "enum",
            "name": self.name,
            "namespace": self.namespace,
            "fields": self.fields,
        }

    def to_doc_json(self) -> Tuple[str, JsonType]:
        return self.name, {
            "doc": "",
            "doc_formatted": "",
            "fields": {f: {"doc": ""} for f in self.fields},
        }

    def to_stub_lines(self, doc_dict: DocDict, indent: int = 0) -> Sequence[str]:
        return ()

    @classmethod
    def from_json(cls: Type[T], json: JsonType) -> T:
        return cls(
            name=json["name"],
            namespace=json["namespace"],
            fields=tuple(json["fields"]),
        )


@dataclass(frozen=True)
class CDelegate(CTypeDefinition):
    parameters: Sequence[CParameter]
    return_type: CType

    def to_json(self) -> JsonType:
        return {
            "type": "delegate",
            "name": self.name,
            "namespace": self.namespace,
            "parameters": tuple(map(CParameter.to_json, self.parameters)),
            "return_type": self.return_type.to_json(),
        }

    def to_doc_json(self) -> Tuple[str, JsonType]:
        return self.name, {
            "doc": "",
            "doc_formatted": "",
            "parameters": {p.name: {"doc": ""} for p in self.parameters},
            "return": "",
        }

    def to_stub_lines(self, doc_dict: DocDict, indent: int = 0) -> Sequence[str]:
        return ()

    @classmethod
    def from_json(cls: Type[T], json: JsonType) -> T:
        return cls(
            name=json["name"],
            namespace=json["namespace"],
            parameters=tuple(map(CParameter.from_json, json["parameters"])),
            return_type=CType.from_json(json["return_type"]),
        )


@dataclass(frozen=True)
class CType:
    name: str
    namespace: Optional[str] = None
    inner: Sequence[CType] = tuple()
    reference: bool = False
    generic: bool = False
    nullable: bool = False

    def __str__(self) -> str:
        return self.full_name

    def __lt__(self, other: CType) -> bool:
        return CType.compare(self, other) < 0

    def __le__(self, other: CType) -> bool:
        return CType.compare(self, other) <= 0

    def __gt__(self, other: CType) -> bool:
        return CType.compare(self, other) > 0

    def __ge__(self, other: CType) -> bool:
        return CType.compare(self, other) >= 0

    @property
    def import_name(self) -> str:
        name: str = self.name
        if self.namespace is not None:
            name = f"{self.namespace}.{name}"
        return name

    @property
    def simple_name(self) -> str:
        name: str = self.name
        if len(self.inner) > 0:
            name = f"{name}[{', '.join(t.simple_name for t in self.inner)}]"
        return name

    @property
    def full_name(self) -> str:
        name: str = self.name
        if self.reference:
            name = "*" + name
        if self.generic:
            name = "$" + name
        if self.nullable:
            name = name + "?"
        if self.namespace is not None:
            name = f"{self.namespace}.{name}"
        if len(self.inner) > 0:
            name = f"{name}[{', '.join(map(str, self.inner))}]"
        return name

    def to_json(self) -> JsonType:
        return str(self)

    @classmethod
    def from_json(cls, json: JsonType) -> Optional[CType]:
        if json is None:
            return None
        match: re.Match = re.match(r"(?:(\w+(?:\.\w+)*)\.)?(\$?\*?\w+\??)(?:\[(.*)])?", json)
        name: str = match.group(2)
        inner: Sequence[CType] = tuple()
        if (inner_str := match.group(3)) is not None:
            inner = tuple(map(CType.from_json, inner_str.split(", ")))
        return cls(
            name=re.sub(r"[?$*]", "", name),
            namespace=match.group(1),
            inner=inner,
            reference="*" in name,
            generic="$" in name,
            nullable="?" in name,
        )

    @staticmethod
    def compare(type0: CType, type1: CType) -> int:
        if type0.namespace != type1.namespace:
            return -1 if type0.namespace < type1.namespace else 1
        if type0.name != type1.name:
            return -1 if type0.name < type1.name else 1
        if (inner := CType.compare_seq(type0.inner, type1.inner)) != 0:
            return inner
        if type0.reference != type1.reference:
            return 1 if type0.reference else -1
        if type0.generic != type1.generic:
            return 1 if type0.generic else -1
        if type0.nullable != type1.nullable:
            return 1 if type0.nullable else -1
        return 0

    @staticmethod
    def compare_seq(types0: Sequence[CType], types1: Sequence[CType]) -> int:
        len0: int = len(types0)
        len1: int = len(types1)
        if len0 < len1:
            return -1
        if len0 > len1:
            return 1

        type0: CType
        type1: CType
        for type0, type1 in zip(types0, types1):
            if (compare := CType.compare(type0, type1)) != 0:
                return compare
        return 0


@dataclass(frozen=True)
class CParameter:
    name: str
    type: CType
    default: bool = False
    out: bool = False

    def to_json(self) -> JsonType:
        return {
            "name": self.name,
            "type": self.type.to_json(),
            "default": self.default,
            "out": self.out,
        }

    @classmethod
    def from_json(cls, json: JsonType) -> CParameter:
        return cls(
            name=json["name"],
            type=CType.from_json(json["type"]),
            default=json["default"],
            out=json["out"],
        )

    @staticmethod
    def compare(params0: Sequence[CParameter], params1: Sequence[CParameter]) -> int:
        len0: int = len(params0)
        len1: int = len(params1)
        if len0 < len1:
            return -1
        if len0 > len1:
            return 1

        param0: CParameter
        param1: CParameter
        for param0, param1 in zip(params0, params1):
            str0: str = str(param0.type)
            str1: str = str(param1.type)
            if str0 < str1:
                return -1
            if str0 > str1:
                return 1
        return 0


@dataclass(frozen=True)
class CMember(ABC):
    name: str
    declaring_type: CType

    def __str__(self) -> str:
        return f"{self.declaring_type}.{self.name}"

    @abstractmethod
    def to_json(self) -> JsonType:
        pass

    @abstractmethod
    def to_doc_json(self) -> Tuple[str, JsonType]:  # TODO - tests
        pass


@dataclass(frozen=True)
class CField(CMember):
    return_type: CType
    static: bool = False

    def __lt__(self, other: CField) -> bool:
        return self.name < other.name

    def __le__(self, other: CField) -> bool:
        return self.name <= other.name

    def __gt__(self, other: CField) -> bool:
        return self.name > other.name

    def __ge__(self, other: CField) -> bool:
        return self.name >= other.name

    def to_json(self) -> JsonType:
        return {
            "name": self.name,
            "declaring_type": self.declaring_type.to_json(),
            "return_type": self.return_type.to_json(),
            "static": self.static,
        }

    def to_doc_json(self) -> Tuple[str, JsonType]:
        return self.name, {"doc": "", "doc_formatted": {}, "return": ""}

    def to_stub_lines(self, doc_dict: DocDict, indent: int = 0) -> Sequence[str]:
        doc_dict.imports.add("typing.Final")
        doc_dict.imports.add(self.return_type.import_name)

        type_str: str = self.return_type.name
        if self.static:
            doc_dict.imports.add("typing.ClassVar")
            type_str = f"ClassVar[{type_str}]"

        return (
            f"{'    ' * indent}{self.name}: Final[{type_str}]",
            *doc_dict.get_doc(f"{self.declaring_type.import_name}.{self.name}", indent),
        )

    @classmethod
    def from_json(cls, json: JsonType) -> CField:
        return cls(
            name=json["name"],
            declaring_type=CType.from_json(json["declaring_type"]),
            return_type=CType.from_json(json["return_type"]),
            static=json["static"],
        )


@dataclass(frozen=True)
class CConstructor(CMember):
    parameters: Sequence[CParameter]

    def __init__(self, declaring_type: CType, parameters: Sequence[CParameter]) -> None:
        super().__init__("__init__", declaring_type)
        object.__setattr__(self, "parameters", parameters)

    def __str__(self) -> str:
        param_types: str = ", ".join(str(p.type) for p in self.parameters)
        return f"{self.declaring_type}.__init__({param_types})"

    def __lt__(self, other: CConstructor) -> bool:
        return CParameter.compare(self.parameters, other.parameters) < 0

    def __le__(self, other: CConstructor) -> bool:
        return CParameter.compare(self.parameters, other.parameters) <= 0

    def __gt__(self, other: CConstructor) -> bool:
        return CParameter.compare(self.parameters, other.parameters) > 0

    def __ge__(self, other: CConstructor) -> bool:
        return CParameter.compare(self.parameters, other.parameters) >= 0

    def to_json(self) -> JsonType:
        return {
            "declaring_type": self.declaring_type.to_json(),
            "parameters": tuple(map(CParameter.to_json, self.parameters)),
        }

    def to_doc_json(self) -> Tuple[str, JsonType]:
        param_types: str = ", ".join(str(p.type) for p in self.parameters)
        return f"__init__({param_types})", {
            "doc": "",
            "doc_formatted": {},
            "parameters": {p.name: "" for p in self.parameters},
        }

    def to_stub_lines(self, doc_dict: DocDict, overload: bool, indent: int = 0) -> Sequence[str]:
        lines: List[str] = []

        if overload:
            doc_dict.imports.add("typing.overload")
            lines.append(f"{'    ' * indent}@overload")

        parameters: List[str] = []
        for parameter in self.parameters:
            doc_dict.imports.add(parameter.type.import_name)
            parameters.append(f", {parameter.name}: {parameter.type.simple_name}")

        lines.append(f"{'    ' * indent}def __init__(self{''.join(parameters)}):")
        lines.extend(doc_dict.get_doc(str(self), indent + 1))

        return lines

    @classmethod
    def from_json(cls, json: JsonType) -> CConstructor:
        return cls(
            declaring_type=CType.from_json(json["declaring_type"]),
            parameters=tuple(map(CParameter.from_json, json["parameters"])),
        )


@dataclass(frozen=True)
class CProperty(CMember):
    type: CType
    setter: bool = False
    static: bool = False

    def __lt__(self, other: CProperty) -> bool:
        return self.name < other.name

    def __le__(self, other: CProperty) -> bool:
        return self.name <= other.name

    def __gt__(self, other: CProperty) -> bool:
        return self.name > other.name

    def __ge__(self, other: CProperty) -> bool:
        return self.name >= other.name

    def to_json(self) -> JsonType:
        return {
            "name": self.name,
            "declaring_type": self.declaring_type.to_json(),
            "type": self.type.to_json(),
            "setter": self.setter,
            "static": self.static,
        }

    def to_doc_json(self) -> Tuple[str, JsonType]:
        return self.name, {"doc": "", "doc_formatted": {}, "return": ""}

    @classmethod
    def from_json(cls, json: JsonType) -> CProperty:
        return cls(
            name=json["name"],
            declaring_type=CType.from_json(json["declaring_type"]),
            type=CType.from_json(json["type"]),
            setter=json["setter"],
            static=json["static"],
        )


@dataclass(frozen=True)
class CMethod(CMember):
    parameters: Sequence[CParameter]
    return_types: Sequence[CType]
    static: bool = False

    def __str__(self) -> str:
        param_types: str = ", ".join(str(p.type) for p in self.parameters)
        returns: str = ", ".join(map(str, self.return_types))
        return f"{self.declaring_type}.{self.name}({param_types}) -> {returns}"

    def __lt__(self, other: CMethod) -> bool:
        if self.name == other.name:
            return CParameter.compare(self.parameters, other.parameters) < 0
        return self.name < other.name

    def __le__(self, other: CMethod) -> bool:
        if self.name == other.name:
            return CParameter.compare(self.parameters, other.parameters) <= 0
        return self.name <= other.name

    def __gt__(self, other: CMethod) -> bool:
        if self.name == other.name:
            return CParameter.compare(self.parameters, other.parameters) > 0
        return self.name > other.name

    def __ge__(self, other: CMethod) -> bool:
        if self.name == other.name:
            return CParameter.compare(self.parameters, other.parameters) >= 0
        return self.name >= other.name

    def to_json(self) -> JsonType:
        return {
            "name": self.name,
            "declaring_type": self.declaring_type.to_json(),
            "parameters": tuple(map(CParameter.to_json, self.parameters)),
            "return_types": tuple(map(CType.to_json, self.return_types)),
            "static": self.static,
        }

    def to_doc_json(self) -> Tuple[str, JsonType]:
        param_types: str = ", ".join(str(p.type) for p in self.parameters)
        return f"{self.name}({param_types})", {
            "doc": "",
            "doc_formatted": {},
            "parameters": {p.name: "" for p in self.parameters},
            "return": "",
            "exceptions": {},
        }

    @classmethod
    def from_json(cls, json: JsonType) -> CMethod:
        return cls(
            name=json["name"],
            declaring_type=CType.from_json(json["declaring_type"]),
            parameters=tuple(map(CParameter.from_json, json["parameters"])),
            return_types=tuple(map(CType.from_json, json["return_types"])),
            static=json["static"],
        )


@dataclass(frozen=True)
class CEvent(CMember):
    type: CType

    def __str__(self) -> str:
        return f"{self.declaring_type}.{self.name} -> ({self.type})"

    def __lt__(self, other: CProperty) -> bool:
        return self.name < other.name

    def __le__(self, other: CProperty) -> bool:
        return self.name <= other.name

    def __gt__(self, other: CProperty) -> bool:
        return self.name > other.name

    def __ge__(self, other: CProperty) -> bool:
        return self.name >= other.name

    def to_json(self) -> JsonType:
        return {
            "name": self.name,
            "declaring_type": self.declaring_type.to_json(),
            "type": self.type.to_json(),
        }

    def to_doc_json(self) -> Tuple[str, JsonType]:
        return f"{self.name} -> ({self.type})", {"doc": "", "doc_formatted": {}}

    @classmethod
    def from_json(cls, json: JsonType) -> CEvent:
        return cls(
            name=json["name"],
            declaring_type=CType.from_json(json["declaring_type"]),
            type=CType.from_json(json["type"]),
        )


class StubFile:
    imports: List[str] = []
