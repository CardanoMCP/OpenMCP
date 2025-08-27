from typing import Callable, Any


def apply_middleware(handler: Callable[[dict], dict], middlewares: list[Callable[[dict], dict]]) -> Callable[[dict], dict]:
    def wrapped(request: dict) -> dict:
        for mw in middlewares:
            request = mw(request)
        return handler(request)

    return wrapped 