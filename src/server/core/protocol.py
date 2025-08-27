class ProtocolHandler:
    def handle_request(self, request: dict) -> dict:
        return {"ok": True, "echo": request} 