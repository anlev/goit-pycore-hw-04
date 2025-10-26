def parse_cat_line(line: str) -> dict[str, int]:
    raw = line.strip()
    if not raw:
        raise ValueError("Empty line")

    parts = []
    for p in raw.split(",", 2):
        parts.append(p.strip())

    if len(parts) != 3:
        raise ValueError(f"Expected 3 parts, got {len(parts)}")

    cat_id, cat_name, cat_age_str = parts
    if not cat_id or not cat_name or not cat_age_str:
        raise ValueError("Cat id, name and age must be specified")

    cat_age = int(cat_age_str)

    return { "id": cat_id, "name": cat_name, "age": cat_age }
