from .base import BaseResource


class StakingResource(BaseResource):
    def get_stake_info(self, stake_key: str) -> dict:
        return {"stake_key": stake_key} 