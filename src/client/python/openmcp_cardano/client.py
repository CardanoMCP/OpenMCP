class OpenMCPCardanoClient:
    def __init__(self, endpoint: str = "http://localhost:8000") -> None:
        self.endpoint = endpoint

    def health(self) -> dict:
        return {"status": "ok"} 