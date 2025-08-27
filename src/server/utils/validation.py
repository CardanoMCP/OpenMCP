def require_fields(data: dict, fields: list[str]) -> bool:
    return all(field in data for field in fields) 