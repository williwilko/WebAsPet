from typing import Any


class Reply():
    success: bool
    data: Any | None
    message: str

    def __init__(self, success: bool, data: Any = None, message: str = None) -> None:
        self.success = success
        self.data = data
        self.message = message