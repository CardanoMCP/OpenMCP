class BaseResource:
    def list(self) -> list[dict]:
        return []

    def get(self, resource_id: str) -> dict | None:
        return None 