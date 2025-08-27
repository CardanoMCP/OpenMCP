from .base import BaseResource


class ContractsResource(BaseResource):
    def compile(self, source: str) -> dict:
        return {"bytecode": "0x"} 