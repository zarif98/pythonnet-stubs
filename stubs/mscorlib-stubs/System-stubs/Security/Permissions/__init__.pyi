from __future__ import annotations

from abc import ABC
from typing import List, Protocol, Union, overload

from System import Array, Attribute, Boolean, Byte, Enum, Int32, Int64, Object, String, Version, Void
from System.Collections import ArrayList, ICollection, IEnumerable, IEnumerator
from System.Runtime.InteropServices import _Attribute
from System.Security import CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, PermissionSet, SecurityElement, SecurityZone
from System.Security.AccessControl import AccessControlActions
from System.Security.Cryptography import CspParameters
from System.Security.Cryptography.X509Certificates import X509Certificate
from System.Security.Util import StringExpressionSet

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class BuiltInPermissionIndex(ABC, ObjectType):
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


class CodeAccessSecurityAttribute(ABC, SecurityAttribute, _Attribute):
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


class EnvironmentPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission, IBuiltInPermission):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: PermissionState): ...
    
    @overload
    def __init__(self, flag: EnvironmentPermissionAccess, pathList: StringType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AddPathList(self, flag: EnvironmentPermissionAccess, pathList: StringType) -> VoidType: ...
    
    def Copy(self) -> IPermission: ...
    
    def FromXml(self, esd: SecurityElement) -> VoidType: ...
    
    def GetPathList(self, flag: EnvironmentPermissionAccess) -> StringType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def IsUnrestricted(self) -> BooleanType: ...
    
    def SetPathList(self, flag: EnvironmentPermissionAccess, pathList: StringType) -> VoidType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, other: IPermission) -> IPermission: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EnvironmentPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, action: SecurityAction): ...
    
    # ---------- Properties ---------- #
    
    @property
    def All(self) -> StringType: ...
    
    @All.setter
    def All(self, value: StringType) -> None: ...
    
    @property
    def Read(self) -> StringType: ...
    
    @Read.setter
    def Read(self, value: StringType) -> None: ...
    
    @property
    def Write(self) -> StringType: ...
    
    @Write.setter
    def Write(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CreatePermission(self) -> IPermission: ...
    
    def get_All(self) -> StringType: ...
    
    def get_Read(self) -> StringType: ...
    
    def get_Write(self) -> StringType: ...
    
    def set_All(self, value: StringType) -> VoidType: ...
    
    def set_Read(self, value: StringType) -> VoidType: ...
    
    def set_Write(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EnvironmentStringExpressionSet(StringExpressionSet):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, str: StringType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileDialogPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission, IBuiltInPermission):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: PermissionState): ...
    
    @overload
    def __init__(self, access: FileDialogPermissionAccess): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Access(self) -> FileDialogPermissionAccess: ...
    
    @Access.setter
    def Access(self, value: FileDialogPermissionAccess) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> IPermission: ...
    
    def FromXml(self, esd: SecurityElement) -> VoidType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def IsUnrestricted(self) -> BooleanType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, target: IPermission) -> IPermission: ...
    
    def get_Access(self) -> FileDialogPermissionAccess: ...
    
    def set_Access(self, value: FileDialogPermissionAccess) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileDialogPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, action: SecurityAction): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Open(self) -> BooleanType: ...
    
    @Open.setter
    def Open(self, value: BooleanType) -> None: ...
    
    @property
    def Save(self) -> BooleanType: ...
    
    @Save.setter
    def Save(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CreatePermission(self) -> IPermission: ...
    
    def get_Open(self) -> BooleanType: ...
    
    def get_Save(self) -> BooleanType: ...
    
    def set_Open(self, value: BooleanType) -> VoidType: ...
    
    def set_Save(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileIOAccess(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, pathDiscovery: BooleanType): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    @overload
    def __init__(self, allFiles: BooleanType, allLocalFiles: BooleanType, pathDiscovery: BooleanType): ...
    
    @overload
    def __init__(self, set: StringExpressionSet, allFiles: BooleanType, allLocalFiles: BooleanType, pathDiscovery: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AllFiles(self) -> BooleanType: ...
    
    @AllFiles.setter
    def AllFiles(self, value: BooleanType) -> None: ...
    
    @property
    def AllLocalFiles(self) -> BooleanType: ...
    
    @AllLocalFiles.setter
    def AllLocalFiles(self, value: BooleanType) -> None: ...
    
    @PathDiscovery.setter
    def PathDiscovery(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddExpressions(self, values: ArrayList, checkForDuplicates: BooleanType) -> VoidType: ...
    
    def Copy(self) -> FileIOAccess: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def Intersect(self, operand: FileIOAccess) -> FileIOAccess: ...
    
    def IsEmpty(self) -> BooleanType: ...
    
    def IsSubsetOf(self, operand: FileIOAccess) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    def ToStringArray(self) -> ArrayType[StringType]: ...
    
    def Union(self, operand: FileIOAccess) -> FileIOAccess: ...
    
    def get_AllFiles(self) -> BooleanType: ...
    
    def get_AllLocalFiles(self) -> BooleanType: ...
    
    def set_AllFiles(self, value: BooleanType) -> VoidType: ...
    
    def set_AllLocalFiles(self, value: BooleanType) -> VoidType: ...
    
    def set_PathDiscovery(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileIOPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission, IBuiltInPermission):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: PermissionState): ...
    
    @overload
    def __init__(self, access: FileIOPermissionAccess, path: StringType): ...
    
    @overload
    def __init__(self, access: FileIOPermissionAccess, pathList: ArrayType[StringType]): ...
    
    @overload
    def __init__(self, access: FileIOPermissionAccess, control: AccessControlActions, path: StringType): ...
    
    @overload
    def __init__(self, access: FileIOPermissionAccess, control: AccessControlActions, pathList: ArrayType[StringType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AllFiles(self) -> FileIOPermissionAccess: ...
    
    @AllFiles.setter
    def AllFiles(self, value: FileIOPermissionAccess) -> None: ...
    
    @property
    def AllLocalFiles(self) -> FileIOPermissionAccess: ...
    
    @AllLocalFiles.setter
    def AllLocalFiles(self, value: FileIOPermissionAccess) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AddPathList(self, access: FileIOPermissionAccess, path: StringType) -> VoidType: ...
    
    @overload
    def AddPathList(self, access: FileIOPermissionAccess, pathList: ArrayType[StringType]) -> VoidType: ...
    
    def Copy(self) -> IPermission: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def FromXml(self, esd: SecurityElement) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetPathList(self, access: FileIOPermissionAccess) -> ArrayType[StringType]: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def IsUnrestricted(self) -> BooleanType: ...
    
    @overload
    def SetPathList(self, access: FileIOPermissionAccess, path: StringType) -> VoidType: ...
    
    @overload
    def SetPathList(self, access: FileIOPermissionAccess, pathList: ArrayType[StringType]) -> VoidType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, other: IPermission) -> IPermission: ...
    
    def get_AllFiles(self) -> FileIOPermissionAccess: ...
    
    def get_AllLocalFiles(self) -> FileIOPermissionAccess: ...
    
    def set_AllFiles(self, value: FileIOPermissionAccess) -> VoidType: ...
    
    def set_AllLocalFiles(self, value: FileIOPermissionAccess) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileIOPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, action: SecurityAction): ...
    
    # ---------- Properties ---------- #
    
    @property
    def All(self) -> StringType: ...
    
    @All.setter
    def All(self, value: StringType) -> None: ...
    
    @property
    def AllFiles(self) -> FileIOPermissionAccess: ...
    
    @AllFiles.setter
    def AllFiles(self, value: FileIOPermissionAccess) -> None: ...
    
    @property
    def AllLocalFiles(self) -> FileIOPermissionAccess: ...
    
    @AllLocalFiles.setter
    def AllLocalFiles(self, value: FileIOPermissionAccess) -> None: ...
    
    @property
    def Append(self) -> StringType: ...
    
    @Append.setter
    def Append(self, value: StringType) -> None: ...
    
    @property
    def ChangeAccessControl(self) -> StringType: ...
    
    @ChangeAccessControl.setter
    def ChangeAccessControl(self, value: StringType) -> None: ...
    
    @property
    def PathDiscovery(self) -> StringType: ...
    
    @PathDiscovery.setter
    def PathDiscovery(self, value: StringType) -> None: ...
    
    @property
    def Read(self) -> StringType: ...
    
    @Read.setter
    def Read(self, value: StringType) -> None: ...
    
    @property
    def ViewAccessControl(self) -> StringType: ...
    
    @ViewAccessControl.setter
    def ViewAccessControl(self, value: StringType) -> None: ...
    
    @property
    def ViewAndModify(self) -> StringType: ...
    
    @ViewAndModify.setter
    def ViewAndModify(self, value: StringType) -> None: ...
    
    @property
    def Write(self) -> StringType: ...
    
    @Write.setter
    def Write(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CreatePermission(self) -> IPermission: ...
    
    def get_All(self) -> StringType: ...
    
    def get_AllFiles(self) -> FileIOPermissionAccess: ...
    
    def get_AllLocalFiles(self) -> FileIOPermissionAccess: ...
    
    def get_Append(self) -> StringType: ...
    
    def get_ChangeAccessControl(self) -> StringType: ...
    
    def get_PathDiscovery(self) -> StringType: ...
    
    def get_Read(self) -> StringType: ...
    
    def get_ViewAccessControl(self) -> StringType: ...
    
    def get_ViewAndModify(self) -> StringType: ...
    
    def get_Write(self) -> StringType: ...
    
    def set_All(self, value: StringType) -> VoidType: ...
    
    def set_AllFiles(self, value: FileIOPermissionAccess) -> VoidType: ...
    
    def set_AllLocalFiles(self, value: FileIOPermissionAccess) -> VoidType: ...
    
    def set_Append(self, value: StringType) -> VoidType: ...
    
    def set_ChangeAccessControl(self, value: StringType) -> VoidType: ...
    
    def set_PathDiscovery(self, value: StringType) -> VoidType: ...
    
    def set_Read(self, value: StringType) -> VoidType: ...
    
    def set_ViewAccessControl(self, value: StringType) -> VoidType: ...
    
    def set_ViewAndModify(self, value: StringType) -> VoidType: ...
    
    def set_Write(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GacIdentityPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IBuiltInPermission):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: PermissionState): ...
    
    @overload
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> IPermission: ...
    
    def FromXml(self, securityElement: SecurityElement) -> VoidType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, target: IPermission) -> IPermission: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GacIdentityPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, action: SecurityAction): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CreatePermission(self) -> IPermission: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HostProtectionAttribute(CodeAccessSecurityAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, action: SecurityAction): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ExternalProcessMgmt(self) -> BooleanType: ...
    
    @ExternalProcessMgmt.setter
    def ExternalProcessMgmt(self, value: BooleanType) -> None: ...
    
    @property
    def ExternalThreading(self) -> BooleanType: ...
    
    @ExternalThreading.setter
    def ExternalThreading(self, value: BooleanType) -> None: ...
    
    @property
    def MayLeakOnAbort(self) -> BooleanType: ...
    
    @MayLeakOnAbort.setter
    def MayLeakOnAbort(self, value: BooleanType) -> None: ...
    
    @property
    def Resources(self) -> HostProtectionResource: ...
    
    @Resources.setter
    def Resources(self, value: HostProtectionResource) -> None: ...
    
    @property
    def SecurityInfrastructure(self) -> BooleanType: ...
    
    @SecurityInfrastructure.setter
    def SecurityInfrastructure(self, value: BooleanType) -> None: ...
    
    @property
    def SelfAffectingProcessMgmt(self) -> BooleanType: ...
    
    @SelfAffectingProcessMgmt.setter
    def SelfAffectingProcessMgmt(self, value: BooleanType) -> None: ...
    
    @property
    def SelfAffectingThreading(self) -> BooleanType: ...
    
    @SelfAffectingThreading.setter
    def SelfAffectingThreading(self, value: BooleanType) -> None: ...
    
    @property
    def SharedState(self) -> BooleanType: ...
    
    @SharedState.setter
    def SharedState(self, value: BooleanType) -> None: ...
    
    @property
    def Synchronization(self) -> BooleanType: ...
    
    @Synchronization.setter
    def Synchronization(self, value: BooleanType) -> None: ...
    
    @property
    def UI(self) -> BooleanType: ...
    
    @UI.setter
    def UI(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CreatePermission(self) -> IPermission: ...
    
    def get_ExternalProcessMgmt(self) -> BooleanType: ...
    
    def get_ExternalThreading(self) -> BooleanType: ...
    
    def get_MayLeakOnAbort(self) -> BooleanType: ...
    
    def get_Resources(self) -> HostProtectionResource: ...
    
    def get_SecurityInfrastructure(self) -> BooleanType: ...
    
    def get_SelfAffectingProcessMgmt(self) -> BooleanType: ...
    
    def get_SelfAffectingThreading(self) -> BooleanType: ...
    
    def get_SharedState(self) -> BooleanType: ...
    
    def get_Synchronization(self) -> BooleanType: ...
    
    def get_UI(self) -> BooleanType: ...
    
    def set_ExternalProcessMgmt(self, value: BooleanType) -> VoidType: ...
    
    def set_ExternalThreading(self, value: BooleanType) -> VoidType: ...
    
    def set_MayLeakOnAbort(self, value: BooleanType) -> VoidType: ...
    
    def set_Resources(self, value: HostProtectionResource) -> VoidType: ...
    
    def set_SecurityInfrastructure(self, value: BooleanType) -> VoidType: ...
    
    def set_SelfAffectingProcessMgmt(self, value: BooleanType) -> VoidType: ...
    
    def set_SelfAffectingThreading(self, value: BooleanType) -> VoidType: ...
    
    def set_SharedState(self, value: BooleanType) -> VoidType: ...
    
    def set_Synchronization(self, value: BooleanType) -> VoidType: ...
    
    def set_UI(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HostProtectionPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission, IBuiltInPermission):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: PermissionState): ...
    
    @overload
    def __init__(self, resources: HostProtectionResource): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Resources(self) -> HostProtectionResource: ...
    
    @Resources.setter
    def Resources(self, value: HostProtectionResource) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> IPermission: ...
    
    def FromXml(self, esd: SecurityElement) -> VoidType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def IsUnrestricted(self) -> BooleanType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, target: IPermission) -> IPermission: ...
    
    def get_Resources(self) -> HostProtectionResource: ...
    
    def set_Resources(self, value: HostProtectionResource) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IDRole(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetHashCode(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IsolatedStorageFilePermission(IsolatedStoragePermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission, IBuiltInPermission):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, state: PermissionState): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> IPermission: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, target: IPermission) -> IPermission: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IsolatedStorageFilePermissionAttribute(IsolatedStoragePermissionAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, action: SecurityAction): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CreatePermission(self) -> IPermission: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IsolatedStoragePermission(ABC, CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def UsageAllowed(self) -> IsolatedStorageContainment: ...
    
    @UsageAllowed.setter
    def UsageAllowed(self, value: IsolatedStorageContainment) -> None: ...
    
    @property
    def UserQuota(self) -> LongType: ...
    
    @UserQuota.setter
    def UserQuota(self, value: LongType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def FromXml(self, esd: SecurityElement) -> VoidType: ...
    
    def IsUnrestricted(self) -> BooleanType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def get_UsageAllowed(self) -> IsolatedStorageContainment: ...
    
    def get_UserQuota(self) -> LongType: ...
    
    def set_UsageAllowed(self, value: IsolatedStorageContainment) -> VoidType: ...
    
    def set_UserQuota(self, value: LongType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IsolatedStoragePermissionAttribute(ABC, CodeAccessSecurityAttribute, _Attribute):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def UsageAllowed(self) -> IsolatedStorageContainment: ...
    
    @UsageAllowed.setter
    def UsageAllowed(self, value: IsolatedStorageContainment) -> None: ...
    
    @property
    def UserQuota(self) -> LongType: ...
    
    @UserQuota.setter
    def UserQuota(self, value: LongType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_UsageAllowed(self) -> IsolatedStorageContainment: ...
    
    def get_UserQuota(self) -> LongType: ...
    
    def set_UsageAllowed(self, value: IsolatedStorageContainment) -> VoidType: ...
    
    def set_UserQuota(self, value: LongType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class KeyContainerPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission, IBuiltInPermission):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: PermissionState): ...
    
    @overload
    def __init__(self, flags: KeyContainerPermissionFlags): ...
    
    @overload
    def __init__(self, flags: KeyContainerPermissionFlags, accessList: ArrayType[KeyContainerPermissionAccessEntry]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AccessEntries(self) -> KeyContainerPermissionAccessEntryCollection: ...
    
    @property
    def Flags(self) -> KeyContainerPermissionFlags: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> IPermission: ...
    
    def FromXml(self, securityElement: SecurityElement) -> VoidType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def IsUnrestricted(self) -> BooleanType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, target: IPermission) -> IPermission: ...
    
    def get_AccessEntries(self) -> KeyContainerPermissionAccessEntryCollection: ...
    
    def get_Flags(self) -> KeyContainerPermissionFlags: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class KeyContainerPermissionAccessEntry(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, keyContainerName: StringType, flags: KeyContainerPermissionFlags): ...
    
    @overload
    def __init__(self, parameters: CspParameters, flags: KeyContainerPermissionFlags): ...
    
    @overload
    def __init__(self, keyStore: StringType, providerName: StringType, providerType: IntType, keyContainerName: StringType, keySpec: IntType, flags: KeyContainerPermissionFlags): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Flags(self) -> KeyContainerPermissionFlags: ...
    
    @Flags.setter
    def Flags(self, value: KeyContainerPermissionFlags) -> None: ...
    
    @property
    def KeyContainerName(self) -> StringType: ...
    
    @KeyContainerName.setter
    def KeyContainerName(self, value: StringType) -> None: ...
    
    @property
    def KeySpec(self) -> IntType: ...
    
    @KeySpec.setter
    def KeySpec(self, value: IntType) -> None: ...
    
    @property
    def KeyStore(self) -> StringType: ...
    
    @KeyStore.setter
    def KeyStore(self, value: StringType) -> None: ...
    
    @property
    def ProviderName(self) -> StringType: ...
    
    @ProviderName.setter
    def ProviderName(self, value: StringType) -> None: ...
    
    @property
    def ProviderType(self) -> IntType: ...
    
    @ProviderType.setter
    def ProviderType(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Flags(self) -> KeyContainerPermissionFlags: ...
    
    def get_KeyContainerName(self) -> StringType: ...
    
    def get_KeySpec(self) -> IntType: ...
    
    def get_KeyStore(self) -> StringType: ...
    
    def get_ProviderName(self) -> StringType: ...
    
    def get_ProviderType(self) -> IntType: ...
    
    def set_Flags(self, value: KeyContainerPermissionFlags) -> VoidType: ...
    
    def set_KeyContainerName(self, value: StringType) -> VoidType: ...
    
    def set_KeySpec(self, value: IntType) -> VoidType: ...
    
    def set_KeyStore(self, value: StringType) -> VoidType: ...
    
    def set_ProviderName(self, value: StringType) -> VoidType: ...
    
    def set_ProviderType(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class KeyContainerPermissionAccessEntryCollection(ObjectType, ICollection, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def Item(self) -> KeyContainerPermissionAccessEntry: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, accessEntry: KeyContainerPermissionAccessEntry) -> IntType: ...
    
    def Clear(self) -> VoidType: ...
    
    def CopyTo(self, array: ArrayType[KeyContainerPermissionAccessEntry], index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> KeyContainerPermissionAccessEntryEnumerator: ...
    
    def IndexOf(self, accessEntry: KeyContainerPermissionAccessEntry) -> IntType: ...
    
    def Remove(self, accessEntry: KeyContainerPermissionAccessEntry) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> KeyContainerPermissionAccessEntry: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class KeyContainerPermissionAccessEntryEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> KeyContainerPermissionAccessEntry: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> KeyContainerPermissionAccessEntry: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class KeyContainerPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, action: SecurityAction): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Flags(self) -> KeyContainerPermissionFlags: ...
    
    @Flags.setter
    def Flags(self, value: KeyContainerPermissionFlags) -> None: ...
    
    @property
    def KeyContainerName(self) -> StringType: ...
    
    @KeyContainerName.setter
    def KeyContainerName(self, value: StringType) -> None: ...
    
    @property
    def KeySpec(self) -> IntType: ...
    
    @KeySpec.setter
    def KeySpec(self, value: IntType) -> None: ...
    
    @property
    def KeyStore(self) -> StringType: ...
    
    @KeyStore.setter
    def KeyStore(self, value: StringType) -> None: ...
    
    @property
    def ProviderName(self) -> StringType: ...
    
    @ProviderName.setter
    def ProviderName(self, value: StringType) -> None: ...
    
    @property
    def ProviderType(self) -> IntType: ...
    
    @ProviderType.setter
    def ProviderType(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CreatePermission(self) -> IPermission: ...
    
    def get_Flags(self) -> KeyContainerPermissionFlags: ...
    
    def get_KeyContainerName(self) -> StringType: ...
    
    def get_KeySpec(self) -> IntType: ...
    
    def get_KeyStore(self) -> StringType: ...
    
    def get_ProviderName(self) -> StringType: ...
    
    def get_ProviderType(self) -> IntType: ...
    
    def set_Flags(self, value: KeyContainerPermissionFlags) -> VoidType: ...
    
    def set_KeyContainerName(self, value: StringType) -> VoidType: ...
    
    def set_KeySpec(self, value: IntType) -> VoidType: ...
    
    def set_KeyStore(self, value: StringType) -> VoidType: ...
    
    def set_ProviderName(self, value: StringType) -> VoidType: ...
    
    def set_ProviderType(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PermissionSetAttribute(CodeAccessSecurityAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, action: SecurityAction): ...
    
    # ---------- Properties ---------- #
    
    @property
    def File(self) -> StringType: ...
    
    @File.setter
    def File(self, value: StringType) -> None: ...
    
    @property
    def Hex(self) -> StringType: ...
    
    @Hex.setter
    def Hex(self, value: StringType) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def UnicodeEncoded(self) -> BooleanType: ...
    
    @UnicodeEncoded.setter
    def UnicodeEncoded(self, value: BooleanType) -> None: ...
    
    @property
    def XML(self) -> StringType: ...
    
    @XML.setter
    def XML(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CreatePermission(self) -> IPermission: ...
    
    def CreatePermissionSet(self) -> PermissionSet: ...
    
    def get_File(self) -> StringType: ...
    
    def get_Hex(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_UnicodeEncoded(self) -> BooleanType: ...
    
    def get_XML(self) -> StringType: ...
    
    def set_File(self, value: StringType) -> VoidType: ...
    
    def set_Hex(self, value: StringType) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_UnicodeEncoded(self, value: BooleanType) -> VoidType: ...
    
    def set_XML(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PrincipalPermission(ObjectType, IPermission, ISecurityEncodable, IUnrestrictedPermission, IBuiltInPermission):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: PermissionState): ...
    
    @overload
    def __init__(self, name: StringType, role: StringType): ...
    
    @overload
    def __init__(self, name: StringType, role: StringType, isAuthenticated: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> IPermission: ...
    
    def Demand(self) -> VoidType: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def FromXml(self, elem: SecurityElement) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def IsUnrestricted(self) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, other: IPermission) -> IPermission: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PrincipalPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, action: SecurityAction): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Authenticated(self) -> BooleanType: ...
    
    @Authenticated.setter
    def Authenticated(self, value: BooleanType) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def Role(self) -> StringType: ...
    
    @Role.setter
    def Role(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CreatePermission(self) -> IPermission: ...
    
    def get_Authenticated(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Role(self) -> StringType: ...
    
    def set_Authenticated(self, value: BooleanType) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_Role(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PublisherIdentityPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IBuiltInPermission):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: PermissionState): ...
    
    @overload
    def __init__(self, certificate: X509Certificate): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Certificate(self) -> X509Certificate: ...
    
    @Certificate.setter
    def Certificate(self, value: X509Certificate) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> IPermission: ...
    
    def FromXml(self, esd: SecurityElement) -> VoidType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, target: IPermission) -> IPermission: ...
    
    def get_Certificate(self) -> X509Certificate: ...
    
    def set_Certificate(self, value: X509Certificate) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PublisherIdentityPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, action: SecurityAction): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CertFile(self) -> StringType: ...
    
    @CertFile.setter
    def CertFile(self, value: StringType) -> None: ...
    
    @property
    def SignedFile(self) -> StringType: ...
    
    @SignedFile.setter
    def SignedFile(self, value: StringType) -> None: ...
    
    @property
    def X509Certificate(self) -> StringType: ...
    
    @X509Certificate.setter
    def X509Certificate(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CreatePermission(self) -> IPermission: ...
    
    def get_CertFile(self) -> StringType: ...
    
    def get_SignedFile(self) -> StringType: ...
    
    def get_X509Certificate(self) -> StringType: ...
    
    def set_CertFile(self, value: StringType) -> VoidType: ...
    
    def set_SignedFile(self, value: StringType) -> VoidType: ...
    
    def set_X509Certificate(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReflectionPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission, IBuiltInPermission):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: PermissionState): ...
    
    @overload
    def __init__(self, flag: ReflectionPermissionFlag): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Flags(self) -> ReflectionPermissionFlag: ...
    
    @Flags.setter
    def Flags(self, value: ReflectionPermissionFlag) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> IPermission: ...
    
    def FromXml(self, esd: SecurityElement) -> VoidType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def IsUnrestricted(self) -> BooleanType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, other: IPermission) -> IPermission: ...
    
    def get_Flags(self) -> ReflectionPermissionFlag: ...
    
    def set_Flags(self, value: ReflectionPermissionFlag) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReflectionPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, action: SecurityAction): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Flags(self) -> ReflectionPermissionFlag: ...
    
    @Flags.setter
    def Flags(self, value: ReflectionPermissionFlag) -> None: ...
    
    @property
    def MemberAccess(self) -> BooleanType: ...
    
    @MemberAccess.setter
    def MemberAccess(self, value: BooleanType) -> None: ...
    
    @property
    def ReflectionEmit(self) -> BooleanType: ...
    
    @ReflectionEmit.setter
    def ReflectionEmit(self, value: BooleanType) -> None: ...
    
    @property
    def RestrictedMemberAccess(self) -> BooleanType: ...
    
    @RestrictedMemberAccess.setter
    def RestrictedMemberAccess(self, value: BooleanType) -> None: ...
    
    @property
    def TypeInformation(self) -> BooleanType: ...
    
    @TypeInformation.setter
    def TypeInformation(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CreatePermission(self) -> IPermission: ...
    
    def get_Flags(self) -> ReflectionPermissionFlag: ...
    
    def get_MemberAccess(self) -> BooleanType: ...
    
    def get_ReflectionEmit(self) -> BooleanType: ...
    
    def get_RestrictedMemberAccess(self) -> BooleanType: ...
    
    def get_TypeInformation(self) -> BooleanType: ...
    
    def set_Flags(self, value: ReflectionPermissionFlag) -> VoidType: ...
    
    def set_MemberAccess(self, value: BooleanType) -> VoidType: ...
    
    def set_ReflectionEmit(self, value: BooleanType) -> VoidType: ...
    
    def set_RestrictedMemberAccess(self, value: BooleanType) -> VoidType: ...
    
    def set_TypeInformation(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegistryPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission, IBuiltInPermission):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: PermissionState): ...
    
    @overload
    def __init__(self, access: RegistryPermissionAccess, pathList: StringType): ...
    
    @overload
    def __init__(self, access: RegistryPermissionAccess, control: AccessControlActions, pathList: StringType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def AddPathList(self, access: RegistryPermissionAccess, pathList: StringType) -> VoidType: ...
    
    @overload
    def AddPathList(self, access: RegistryPermissionAccess, control: AccessControlActions, pathList: StringType) -> VoidType: ...
    
    def Copy(self) -> IPermission: ...
    
    def FromXml(self, esd: SecurityElement) -> VoidType: ...
    
    def GetPathList(self, access: RegistryPermissionAccess) -> StringType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def IsUnrestricted(self) -> BooleanType: ...
    
    def SetPathList(self, access: RegistryPermissionAccess, pathList: StringType) -> VoidType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, other: IPermission) -> IPermission: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegistryPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, action: SecurityAction): ...
    
    # ---------- Properties ---------- #
    
    @property
    def All(self) -> StringType: ...
    
    @All.setter
    def All(self, value: StringType) -> None: ...
    
    @property
    def ChangeAccessControl(self) -> StringType: ...
    
    @ChangeAccessControl.setter
    def ChangeAccessControl(self, value: StringType) -> None: ...
    
    @property
    def Create(self) -> StringType: ...
    
    @Create.setter
    def Create(self, value: StringType) -> None: ...
    
    @property
    def Read(self) -> StringType: ...
    
    @Read.setter
    def Read(self, value: StringType) -> None: ...
    
    @property
    def ViewAccessControl(self) -> StringType: ...
    
    @ViewAccessControl.setter
    def ViewAccessControl(self, value: StringType) -> None: ...
    
    @property
    def ViewAndModify(self) -> StringType: ...
    
    @ViewAndModify.setter
    def ViewAndModify(self, value: StringType) -> None: ...
    
    @property
    def Write(self) -> StringType: ...
    
    @Write.setter
    def Write(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CreatePermission(self) -> IPermission: ...
    
    def get_All(self) -> StringType: ...
    
    def get_ChangeAccessControl(self) -> StringType: ...
    
    def get_Create(self) -> StringType: ...
    
    def get_Read(self) -> StringType: ...
    
    def get_ViewAccessControl(self) -> StringType: ...
    
    def get_ViewAndModify(self) -> StringType: ...
    
    def get_Write(self) -> StringType: ...
    
    def set_All(self, value: StringType) -> VoidType: ...
    
    def set_ChangeAccessControl(self, value: StringType) -> VoidType: ...
    
    def set_Create(self, value: StringType) -> VoidType: ...
    
    def set_Read(self, value: StringType) -> VoidType: ...
    
    def set_ViewAccessControl(self, value: StringType) -> VoidType: ...
    
    def set_ViewAndModify(self, value: StringType) -> VoidType: ...
    
    def set_Write(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityAttribute(ABC, Attribute, _Attribute):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Action(self) -> SecurityAction: ...
    
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    
    @property
    def Unrestricted(self) -> BooleanType: ...
    
    @Unrestricted.setter
    def Unrestricted(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CreatePermission(self) -> IPermission: ...
    
    def get_Action(self) -> SecurityAction: ...
    
    def get_Unrestricted(self) -> BooleanType: ...
    
    def set_Action(self, value: SecurityAction) -> VoidType: ...
    
    def set_Unrestricted(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission, IBuiltInPermission):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: PermissionState): ...
    
    @overload
    def __init__(self, flag: SecurityPermissionFlag): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Flags(self) -> SecurityPermissionFlag: ...
    
    @Flags.setter
    def Flags(self, value: SecurityPermissionFlag) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> IPermission: ...
    
    def FromXml(self, esd: SecurityElement) -> VoidType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def IsUnrestricted(self) -> BooleanType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, target: IPermission) -> IPermission: ...
    
    def get_Flags(self) -> SecurityPermissionFlag: ...
    
    def set_Flags(self, value: SecurityPermissionFlag) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, action: SecurityAction): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Assertion(self) -> BooleanType: ...
    
    @Assertion.setter
    def Assertion(self, value: BooleanType) -> None: ...
    
    @property
    def BindingRedirects(self) -> BooleanType: ...
    
    @BindingRedirects.setter
    def BindingRedirects(self, value: BooleanType) -> None: ...
    
    @property
    def ControlAppDomain(self) -> BooleanType: ...
    
    @ControlAppDomain.setter
    def ControlAppDomain(self, value: BooleanType) -> None: ...
    
    @property
    def ControlDomainPolicy(self) -> BooleanType: ...
    
    @ControlDomainPolicy.setter
    def ControlDomainPolicy(self, value: BooleanType) -> None: ...
    
    @property
    def ControlEvidence(self) -> BooleanType: ...
    
    @ControlEvidence.setter
    def ControlEvidence(self, value: BooleanType) -> None: ...
    
    @property
    def ControlPolicy(self) -> BooleanType: ...
    
    @ControlPolicy.setter
    def ControlPolicy(self, value: BooleanType) -> None: ...
    
    @property
    def ControlPrincipal(self) -> BooleanType: ...
    
    @ControlPrincipal.setter
    def ControlPrincipal(self, value: BooleanType) -> None: ...
    
    @property
    def ControlThread(self) -> BooleanType: ...
    
    @ControlThread.setter
    def ControlThread(self, value: BooleanType) -> None: ...
    
    @property
    def Execution(self) -> BooleanType: ...
    
    @Execution.setter
    def Execution(self, value: BooleanType) -> None: ...
    
    @property
    def Flags(self) -> SecurityPermissionFlag: ...
    
    @Flags.setter
    def Flags(self, value: SecurityPermissionFlag) -> None: ...
    
    @property
    def Infrastructure(self) -> BooleanType: ...
    
    @Infrastructure.setter
    def Infrastructure(self, value: BooleanType) -> None: ...
    
    @property
    def RemotingConfiguration(self) -> BooleanType: ...
    
    @RemotingConfiguration.setter
    def RemotingConfiguration(self, value: BooleanType) -> None: ...
    
    @property
    def SerializationFormatter(self) -> BooleanType: ...
    
    @SerializationFormatter.setter
    def SerializationFormatter(self, value: BooleanType) -> None: ...
    
    @property
    def SkipVerification(self) -> BooleanType: ...
    
    @SkipVerification.setter
    def SkipVerification(self, value: BooleanType) -> None: ...
    
    @property
    def UnmanagedCode(self) -> BooleanType: ...
    
    @UnmanagedCode.setter
    def UnmanagedCode(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CreatePermission(self) -> IPermission: ...
    
    def get_Assertion(self) -> BooleanType: ...
    
    def get_BindingRedirects(self) -> BooleanType: ...
    
    def get_ControlAppDomain(self) -> BooleanType: ...
    
    def get_ControlDomainPolicy(self) -> BooleanType: ...
    
    def get_ControlEvidence(self) -> BooleanType: ...
    
    def get_ControlPolicy(self) -> BooleanType: ...
    
    def get_ControlPrincipal(self) -> BooleanType: ...
    
    def get_ControlThread(self) -> BooleanType: ...
    
    def get_Execution(self) -> BooleanType: ...
    
    def get_Flags(self) -> SecurityPermissionFlag: ...
    
    def get_Infrastructure(self) -> BooleanType: ...
    
    def get_RemotingConfiguration(self) -> BooleanType: ...
    
    def get_SerializationFormatter(self) -> BooleanType: ...
    
    def get_SkipVerification(self) -> BooleanType: ...
    
    def get_UnmanagedCode(self) -> BooleanType: ...
    
    def set_Assertion(self, value: BooleanType) -> VoidType: ...
    
    def set_BindingRedirects(self, value: BooleanType) -> VoidType: ...
    
    def set_ControlAppDomain(self, value: BooleanType) -> VoidType: ...
    
    def set_ControlDomainPolicy(self, value: BooleanType) -> VoidType: ...
    
    def set_ControlEvidence(self, value: BooleanType) -> VoidType: ...
    
    def set_ControlPolicy(self, value: BooleanType) -> VoidType: ...
    
    def set_ControlPrincipal(self, value: BooleanType) -> VoidType: ...
    
    def set_ControlThread(self, value: BooleanType) -> VoidType: ...
    
    def set_Execution(self, value: BooleanType) -> VoidType: ...
    
    def set_Flags(self, value: SecurityPermissionFlag) -> VoidType: ...
    
    def set_Infrastructure(self, value: BooleanType) -> VoidType: ...
    
    def set_RemotingConfiguration(self, value: BooleanType) -> VoidType: ...
    
    def set_SerializationFormatter(self, value: BooleanType) -> VoidType: ...
    
    def set_SkipVerification(self, value: BooleanType) -> VoidType: ...
    
    def set_UnmanagedCode(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SiteIdentityPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IBuiltInPermission):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: PermissionState): ...
    
    @overload
    def __init__(self, site: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Site(self) -> StringType: ...
    
    @Site.setter
    def Site(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> IPermission: ...
    
    def FromXml(self, esd: SecurityElement) -> VoidType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, target: IPermission) -> IPermission: ...
    
    def get_Site(self) -> StringType: ...
    
    def set_Site(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SiteIdentityPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, action: SecurityAction): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Site(self) -> StringType: ...
    
    @Site.setter
    def Site(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CreatePermission(self) -> IPermission: ...
    
    def get_Site(self) -> StringType: ...
    
    def set_Site(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StrongName2(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def m_name(self) -> StringType: ...
    
    @m_name.setter
    def m_name(self, value: StringType) -> None: ...
    
    @property
    def m_publicKeyBlob(self) -> StrongNamePublicKeyBlob: ...
    
    @m_publicKeyBlob.setter
    def m_publicKeyBlob(self, value: StrongNamePublicKeyBlob) -> None: ...
    
    @property
    def m_version(self) -> Version: ...
    
    @m_version.setter
    def m_version(self, value: Version) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, publicKeyBlob: StrongNamePublicKeyBlob, name: StringType, version: Version): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> StrongName2: ...
    
    @overload
    def Equals(self, target: StrongName2) -> BooleanType: ...
    
    def Intersect(self, target: StrongName2) -> StrongName2: ...
    
    def IsSubsetOf(self, target: StrongName2) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StrongNameIdentityPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IBuiltInPermission):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: PermissionState): ...
    
    @overload
    def __init__(self, blob: StrongNamePublicKeyBlob, name: StringType, version: Version): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def PublicKey(self) -> StrongNamePublicKeyBlob: ...
    
    @PublicKey.setter
    def PublicKey(self, value: StrongNamePublicKeyBlob) -> None: ...
    
    @property
    def Version(self) -> Version: ...
    
    @Version.setter
    def Version(self, value: Version) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> IPermission: ...
    
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, target: IPermission) -> IPermission: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_PublicKey(self) -> StrongNamePublicKeyBlob: ...
    
    def get_Version(self) -> Version: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_PublicKey(self, value: StrongNamePublicKeyBlob) -> VoidType: ...
    
    def set_Version(self, value: Version) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StrongNameIdentityPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, action: SecurityAction): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def PublicKey(self) -> StringType: ...
    
    @PublicKey.setter
    def PublicKey(self, value: StringType) -> None: ...
    
    @property
    def Version(self) -> StringType: ...
    
    @Version.setter
    def Version(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CreatePermission(self) -> IPermission: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_PublicKey(self) -> StringType: ...
    
    def get_Version(self) -> StringType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_PublicKey(self, value: StringType) -> VoidType: ...
    
    def set_Version(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StrongNamePublicKeyBlob(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, publicKey: ArrayType[ByteType]): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UIPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission, IBuiltInPermission):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: PermissionState): ...
    
    @overload
    def __init__(self, windowFlag: UIPermissionWindow, clipboardFlag: UIPermissionClipboard): ...
    
    @overload
    def __init__(self, windowFlag: UIPermissionWindow): ...
    
    @overload
    def __init__(self, clipboardFlag: UIPermissionClipboard): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Clipboard(self) -> UIPermissionClipboard: ...
    
    @Clipboard.setter
    def Clipboard(self, value: UIPermissionClipboard) -> None: ...
    
    @property
    def Window(self) -> UIPermissionWindow: ...
    
    @Window.setter
    def Window(self, value: UIPermissionWindow) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> IPermission: ...
    
    def FromXml(self, esd: SecurityElement) -> VoidType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def IsUnrestricted(self) -> BooleanType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, target: IPermission) -> IPermission: ...
    
    def get_Clipboard(self) -> UIPermissionClipboard: ...
    
    def get_Window(self) -> UIPermissionWindow: ...
    
    def set_Clipboard(self, value: UIPermissionClipboard) -> VoidType: ...
    
    def set_Window(self, value: UIPermissionWindow) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UIPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, action: SecurityAction): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Clipboard(self) -> UIPermissionClipboard: ...
    
    @Clipboard.setter
    def Clipboard(self, value: UIPermissionClipboard) -> None: ...
    
    @property
    def Window(self) -> UIPermissionWindow: ...
    
    @Window.setter
    def Window(self, value: UIPermissionWindow) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CreatePermission(self) -> IPermission: ...
    
    def get_Clipboard(self) -> UIPermissionClipboard: ...
    
    def get_Window(self) -> UIPermissionWindow: ...
    
    def set_Clipboard(self, value: UIPermissionClipboard) -> VoidType: ...
    
    def set_Window(self, value: UIPermissionWindow) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UrlIdentityPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IBuiltInPermission):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: PermissionState): ...
    
    @overload
    def __init__(self, site: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Url(self) -> StringType: ...
    
    @Url.setter
    def Url(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> IPermission: ...
    
    def FromXml(self, esd: SecurityElement) -> VoidType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, target: IPermission) -> IPermission: ...
    
    def get_Url(self) -> StringType: ...
    
    def set_Url(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UrlIdentityPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, action: SecurityAction): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Url(self) -> StringType: ...
    
    @Url.setter
    def Url(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CreatePermission(self) -> IPermission: ...
    
    def get_Url(self) -> StringType: ...
    
    def set_Url(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ZoneIdentityPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IBuiltInPermission):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: PermissionState): ...
    
    @overload
    def __init__(self, zone: SecurityZone): ...
    
    # ---------- Properties ---------- #
    
    @property
    def SecurityZone(self) -> SecurityZone: ...
    
    @SecurityZone.setter
    def SecurityZone(self, value: SecurityZone) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> IPermission: ...
    
    def FromXml(self, esd: SecurityElement) -> VoidType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, target: IPermission) -> IPermission: ...
    
    def get_SecurityZone(self) -> SecurityZone: ...
    
    def set_SecurityZone(self, value: SecurityZone) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ZoneIdentityPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, action: SecurityAction): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Zone(self) -> SecurityZone: ...
    
    @Zone.setter
    def Zone(self, value: SecurityZone) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CreatePermission(self) -> IPermission: ...
    
    def get_Zone(self) -> SecurityZone: ...
    
    def set_Zone(self, value: SecurityZone) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# ---------- Interfaces ---------- #

class IBuiltInPermission(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetTokenIndex(self) -> IntType: ...
    
    # No Events


class IUnrestrictedPermission(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def IsUnrestricted(self) -> BooleanType: ...
    
    # No Events


# ---------- Enums ---------- #

class BuiltInPermissionFlag(Enum):
    EnvironmentPermission: IntType = 1
    FileDialogPermission: IntType = 2
    FileIOPermission: IntType = 4
    IsolatedStorageFilePermission: IntType = 8
    ReflectionPermission: IntType = 16
    RegistryPermission: IntType = 32
    SecurityPermission: IntType = 64
    UIPermission: IntType = 128
    PrincipalPermission: IntType = 256
    PublisherIdentityPermission: IntType = 512
    SiteIdentityPermission: IntType = 1024
    StrongNameIdentityPermission: IntType = 2048
    UrlIdentityPermission: IntType = 4096
    ZoneIdentityPermission: IntType = 8192
    KeyContainerPermission: IntType = 16384


class EnvironmentPermissionAccess(Enum):
    NoAccess: IntType = 0
    Read: IntType = 1
    Write: IntType = 2
    AllAccess: IntType = 3


class FileDialogPermissionAccess(Enum):
    #None: IntType = 0
    Open: IntType = 1
    Save: IntType = 2
    OpenSave: IntType = 3


class FileIOPermissionAccess(Enum):
    NoAccess: IntType = 0
    Read: IntType = 1
    Write: IntType = 2
    Append: IntType = 4
    PathDiscovery: IntType = 8
    AllAccess: IntType = 15


class HostProtectionResource(Enum):
    #None: IntType = 0
    Synchronization: IntType = 1
    SharedState: IntType = 2
    ExternalProcessMgmt: IntType = 4
    SelfAffectingProcessMgmt: IntType = 8
    ExternalThreading: IntType = 16
    SelfAffectingThreading: IntType = 32
    SecurityInfrastructure: IntType = 64
    UI: IntType = 128
    MayLeakOnAbort: IntType = 256
    All: IntType = 511


class IsolatedStorageContainment(Enum):
    #None: IntType = 0
    DomainIsolationByUser: IntType = 16
    ApplicationIsolationByUser: IntType = 21
    AssemblyIsolationByUser: IntType = 32
    DomainIsolationByMachine: IntType = 48
    AssemblyIsolationByMachine: IntType = 64
    ApplicationIsolationByMachine: IntType = 69
    DomainIsolationByRoamingUser: IntType = 80
    AssemblyIsolationByRoamingUser: IntType = 96
    ApplicationIsolationByRoamingUser: IntType = 101
    AdministerIsolatedStorageByUser: IntType = 112
    UnrestrictedIsolatedStorage: IntType = 240


class KeyContainerPermissionFlags(Enum):
    NoFlags: IntType = 0
    Create: IntType = 1
    Open: IntType = 2
    Delete: IntType = 4
    Import: IntType = 16
    Export: IntType = 32
    Sign: IntType = 256
    Decrypt: IntType = 512
    ViewAcl: IntType = 4096
    ChangeAcl: IntType = 8192
    AllFlags: IntType = 13111


class PermissionState(Enum):
    #None: IntType = 0
    Unrestricted: IntType = 1


class ReflectionPermissionFlag(Enum):
    NoFlags: IntType = 0
    TypeInformation: IntType = 1
    MemberAccess: IntType = 2
    ReflectionEmit: IntType = 4
    AllFlags: IntType = 7
    RestrictedMemberAccess: IntType = 8


class RegistryPermissionAccess(Enum):
    NoAccess: IntType = 0
    Read: IntType = 1
    Write: IntType = 2
    Create: IntType = 4
    AllAccess: IntType = 7


class SecurityAction(Enum):
    Demand: IntType = 2
    Assert: IntType = 3
    Deny: IntType = 4
    PermitOnly: IntType = 5
    LinkDemand: IntType = 6
    InheritanceDemand: IntType = 7
    RequestMinimum: IntType = 8
    RequestOptional: IntType = 9
    RequestRefuse: IntType = 10


class SecurityPermissionFlag(Enum):
    NoFlags: IntType = 0
    Assertion: IntType = 1
    UnmanagedCode: IntType = 2
    SkipVerification: IntType = 4
    Execution: IntType = 8
    ControlThread: IntType = 16
    ControlEvidence: IntType = 32
    ControlPolicy: IntType = 64
    SerializationFormatter: IntType = 128
    ControlDomainPolicy: IntType = 256
    ControlPrincipal: IntType = 512
    ControlAppDomain: IntType = 1024
    RemotingConfiguration: IntType = 2048
    Infrastructure: IntType = 4096
    BindingRedirects: IntType = 8192
    AllFlags: IntType = 16383


class UIPermissionClipboard(Enum):
    NoClipboard: IntType = 0
    OwnClipboard: IntType = 1
    AllClipboard: IntType = 2


class UIPermissionWindow(Enum):
    NoWindows: IntType = 0
    SafeSubWindows: IntType = 1
    SafeTopLevelWindows: IntType = 2
    AllWindows: IntType = 3


# No Delegates

__all__ = [
    BuiltInPermissionIndex,
    CodeAccessSecurityAttribute,
    EnvironmentPermission,
    EnvironmentPermissionAttribute,
    EnvironmentStringExpressionSet,
    FileDialogPermission,
    FileDialogPermissionAttribute,
    FileIOAccess,
    FileIOPermission,
    FileIOPermissionAttribute,
    GacIdentityPermission,
    GacIdentityPermissionAttribute,
    HostProtectionAttribute,
    HostProtectionPermission,
    IDRole,
    IsolatedStorageFilePermission,
    IsolatedStorageFilePermissionAttribute,
    IsolatedStoragePermission,
    IsolatedStoragePermissionAttribute,
    KeyContainerPermission,
    KeyContainerPermissionAccessEntry,
    KeyContainerPermissionAccessEntryCollection,
    KeyContainerPermissionAccessEntryEnumerator,
    KeyContainerPermissionAttribute,
    PermissionSetAttribute,
    PrincipalPermission,
    PrincipalPermissionAttribute,
    PublisherIdentityPermission,
    PublisherIdentityPermissionAttribute,
    ReflectionPermission,
    ReflectionPermissionAttribute,
    RegistryPermission,
    RegistryPermissionAttribute,
    SecurityAttribute,
    SecurityPermission,
    SecurityPermissionAttribute,
    SiteIdentityPermission,
    SiteIdentityPermissionAttribute,
    StrongName2,
    StrongNameIdentityPermission,
    StrongNameIdentityPermissionAttribute,
    StrongNamePublicKeyBlob,
    UIPermission,
    UIPermissionAttribute,
    UrlIdentityPermission,
    UrlIdentityPermissionAttribute,
    ZoneIdentityPermission,
    ZoneIdentityPermissionAttribute,
    IBuiltInPermission,
    IUnrestrictedPermission,
    BuiltInPermissionFlag,
    EnvironmentPermissionAccess,
    FileDialogPermissionAccess,
    FileIOPermissionAccess,
    HostProtectionResource,
    IsolatedStorageContainment,
    KeyContainerPermissionFlags,
    PermissionState,
    ReflectionPermissionFlag,
    RegistryPermissionAccess,
    SecurityAction,
    SecurityPermissionFlag,
    UIPermissionClipboard,
    UIPermissionWindow,
]
