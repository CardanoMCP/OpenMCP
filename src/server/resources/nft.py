from .base import BaseResource


class NFTResource(BaseResource):
    def get_collection(self, policy_id: str) -> list[dict]:
        return [] 