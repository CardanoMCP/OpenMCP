def to_json_schema(data: dict) -> dict:
    return {"type": "object", "properties": {k: {"type": "string"} for k in data.keys()}} 