def salaries_from_lines(lines) -> list[float]:
    salaries = []
    for line in lines:
        _, salary = line.strip().split(",", 1)
        try:
            salaries.append(float(salary))
        except ValueError:
            continue
    return salaries

def parse_salaries(path: str) -> list[float]:
    try:
        with open(path, "r") as file:
            return salaries_from_lines(file)
    except (FileNotFoundError, OSError):
        return []