class Reply():
    status: str
    message: str

    def __init__(self, status: str, data: Any = None, message: str = None) -> None:
        self.status = status
        self.data = data
        self.message = message