def build_url(base: str, path: str) -> str:
    return base.rstrip("/") + "/" + path.lstrip("/") 