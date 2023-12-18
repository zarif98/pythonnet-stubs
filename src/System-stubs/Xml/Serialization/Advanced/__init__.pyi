from __future__ import annotations

from abc import ABC
from typing import List
from typing import Union
from typing import overload

from System import Array
from System import Boolean
from System import Int32
from System import Object
from System import String
from System import Type
from System import Void
from System.CodeDom import CodeCompileUnit
from System.CodeDom import CodeExpression
from System.CodeDom import CodeNamespace
from System.CodeDom.Compiler import CodeDomProvider
from System.Collections import CollectionBase
from System.Collections import ICollection
from System.Collections import IEnumerable
from System.Collections import IList
from System.Xml.Schema import XmlSchemaAny
from System.Xml.Schema import XmlSchemaObject
from System.Xml.Schema import XmlSchemaType
from System.Xml.Serialization import CodeGenerationOptions
from System.Xml.Serialization import XmlSchemaImporter
from System.Xml.Serialization import XmlSchemas

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class MappedTypeDesc(ObjectType):
    """"""

    # No Fields

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SchemaImporterExtension(ABC, ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def ImportAnyElement(
        self,
        any: XmlSchemaAny,
        mixed: BooleanType,
        schemas: XmlSchemas,
        importer: XmlSchemaImporter,
        compileUnit: CodeCompileUnit,
        mainNamespace: CodeNamespace,
        options: CodeGenerationOptions,
        codeProvider: CodeDomProvider,
    ) -> StringType: ...
    def ImportDefaultValue(self, value: StringType, type: StringType) -> CodeExpression: ...
    @overload
    def ImportSchemaType(
        self,
        name: StringType,
        ns: StringType,
        context: XmlSchemaObject,
        schemas: XmlSchemas,
        importer: XmlSchemaImporter,
        compileUnit: CodeCompileUnit,
        mainNamespace: CodeNamespace,
        options: CodeGenerationOptions,
        codeProvider: CodeDomProvider,
    ) -> StringType: ...
    @overload
    def ImportSchemaType(
        self,
        type: XmlSchemaType,
        context: XmlSchemaObject,
        schemas: XmlSchemas,
        importer: XmlSchemaImporter,
        compileUnit: CodeCompileUnit,
        mainNamespace: CodeNamespace,
        options: CodeGenerationOptions,
        codeProvider: CodeDomProvider,
    ) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SchemaImporterExtensionCollection(CollectionBase, IList, ICollection, IEnumerable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    def __getitem__(self, key: IntType) -> SchemaImporterExtension: ...
    def __setitem__(self, key: IntType, value: SchemaImporterExtension) -> None: ...

    # ---------- Methods ---------- #

    @overload
    def Add(self, extension: SchemaImporterExtension) -> IntType: ...
    @overload
    def Add(self, name: StringType, type: TypeType) -> IntType: ...
    @overload
    def Clear(self) -> VoidType: ...
    def Contains(self, extension: SchemaImporterExtension) -> BooleanType: ...
    def CopyTo(self, array: ArrayType[SchemaImporterExtension], index: IntType) -> VoidType: ...
    def IndexOf(self, extension: SchemaImporterExtension) -> IntType: ...
    def Insert(self, index: IntType, extension: SchemaImporterExtension) -> VoidType: ...
    @overload
    def Remove(self, name: StringType) -> VoidType: ...
    @overload
    def Remove(self, extension: SchemaImporterExtension) -> VoidType: ...
    def get_Item(self, index: IntType) -> SchemaImporterExtension: ...
    def set_Item(self, index: IntType, value: SchemaImporterExtension) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

# No Structs

# No Interfaces

# No Enums

# No Delegates

__all__ = [
    MappedTypeDesc,
    SchemaImporterExtension,
    SchemaImporterExtensionCollection,
]
