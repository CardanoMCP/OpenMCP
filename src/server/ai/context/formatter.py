def format_context(context: dict) -> str:
    parts = [f"{k}: {v}" for k, v in context.items()]
    return "\n".join(parts) 