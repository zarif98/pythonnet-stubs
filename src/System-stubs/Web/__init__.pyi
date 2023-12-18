from __future__ import annotations

from typing import Union
from typing import overload

from System import Boolean
from System import Enum
from System import Int32
from System import Void
from System.Runtime.InteropServices import _Attribute
from System.Security import CodeAccessPermission
from System.Security import IPermission
from System.Security import ISecurityEncodable
from System.Security import IStackWalk
from System.Security import SecurityElement
from System.Security.Permissions import CodeAccessSecurityAttribute
from System.Security.Permissions import IUnrestrictedPermission
from System.Security.Permissions import PermissionState
from System.Security.Permissions import SecurityAction

# ---------- Types ---------- #

BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class AspNetHostingPermission(
    CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission
):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, state: PermissionState): ...
    @overload
    def __init__(self, level: AspNetHostingPermissionLevel): ...

    # ---------- Properties ---------- #

    @property
    def Level(self) -> AspNetHostingPermissionLevel: ...
    @Level.setter
    def Level(self, value: AspNetHostingPermissionLevel) -> None: ...

    # ---------- Methods ---------- #

    def Copy(self) -> IPermission: ...
    def FromXml(self, securityElement: SecurityElement) -> VoidType: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    def IsUnrestricted(self) -> BooleanType: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, target: IPermission) -> IPermission: ...
    def get_Level(self) -> AspNetHostingPermissionLevel: ...
    def set_Level(self, value: AspNetHostingPermissionLevel) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class AspNetHostingPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, action: SecurityAction): ...

    # ---------- Properties ---------- #

    @property
    def Level(self) -> AspNetHostingPermissionLevel: ...
    @Level.setter
    def Level(self, value: AspNetHostingPermissionLevel) -> None: ...

    # ---------- Methods ---------- #

    def CreatePermission(self) -> IPermission: ...
    def get_Level(self) -> AspNetHostingPermissionLevel: ...
    def set_Level(self, value: AspNetHostingPermissionLevel) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

# No Structs

# No Interfaces

# ---------- Enums ---------- #

class AspNetHostingPermissionLevel(Enum):
    # None = 100
    Minimal = 200
    Low = 300
    Medium = 400
    High = 500
    Unrestricted = 600

# No Delegates

__all__ = [
    AspNetHostingPermission,
    AspNetHostingPermissionAttribute,
    AspNetHostingPermissionLevel,
]
