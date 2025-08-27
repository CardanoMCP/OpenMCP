class ContextManager:
    def __init__(self) -> None:
        self.state: dict = {}

    def set(self, key: str, value: object) -> None:
        self.state[key] = value

    def get(self, key: str, default: object | None = None) -> object | None:
        return self.state.get(key, default) 