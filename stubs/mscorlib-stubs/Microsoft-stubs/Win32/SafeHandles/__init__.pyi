from __future__ import annotations

from abc import ABC
from typing import Union

from System import Boolean, IDisposable, IntPtr
from System.Runtime.InteropServices import CriticalHandle, SafeBuffer, SafeHandle

# ---------- Types ---------- #

BooleanType = Union[bool, Boolean]
NIntType = Union[int, IntPtr]

# ---------- Classes ---------- #

class CriticalHandleMinusOneIsInvalid(ABC, CriticalHandle, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsInvalid(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_IsInvalid(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CriticalHandleZeroOrMinusOneIsInvalid(ABC, CriticalHandle, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsInvalid(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_IsInvalid(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeAccessTokenHandle(SafeHandle, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, handle: NIntType): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def InvalidHandle() -> SafeAccessTokenHandle: ...
    
    @property
    def IsInvalid(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_InvalidHandle() -> SafeAccessTokenHandle: ...
    
    def get_IsInvalid(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeFileHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, preexistingHandle: NIntType, ownsHandle: BooleanType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeFileMappingHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeFindHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeHandleMinusOneIsInvalid(ABC, SafeHandle, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsInvalid(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_IsInvalid(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeHandleZeroOrMinusOneIsInvalid(ABC, SafeHandle, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsInvalid(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_IsInvalid(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeLocalAllocHandle(SafeBuffer, IDisposable):
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


class SafeLsaLogonProcessHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeLsaMemoryHandle(SafeBuffer, IDisposable):
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


class SafeLsaPolicyHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeLsaReturnBufferHandle(SafeBuffer, IDisposable):
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


class SafePEFileHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeProcessHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeRegistryHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, preexistingHandle: NIntType, ownsHandle: BooleanType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeThreadHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeViewOfFileHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeWaitHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, existingHandle: NIntType, ownsHandle: BooleanType): ...
    
    # No Properties
    
    # No Methods
    
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
    CriticalHandleMinusOneIsInvalid,
    CriticalHandleZeroOrMinusOneIsInvalid,
    SafeAccessTokenHandle,
    SafeFileHandle,
    SafeFileMappingHandle,
    SafeFindHandle,
    SafeHandleMinusOneIsInvalid,
    SafeHandleZeroOrMinusOneIsInvalid,
    SafeLocalAllocHandle,
    SafeLsaLogonProcessHandle,
    SafeLsaMemoryHandle,
    SafeLsaPolicyHandle,
    SafeLsaReturnBufferHandle,
    SafePEFileHandle,
    SafeProcessHandle,
    SafeRegistryHandle,
    SafeThreadHandle,
    SafeViewOfFileHandle,
    SafeWaitHandle,
]
