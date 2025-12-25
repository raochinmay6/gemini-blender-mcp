def is_valid_command(code: str) -> bool:
    return code.strip().startswith("import bpy")
