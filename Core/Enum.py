from enum import Enum


class TestStatus(Enum):
    Pass = 1
    Failed = 2
    Error = 3


class Keyboard(Enum):
    Backspace = 8
    Tab = 9
    Clear = 12
    Enter = 13
    Shift = 16
    Control = 17
    Alt = 18
    CapsLock = 20
    Esc = 27
