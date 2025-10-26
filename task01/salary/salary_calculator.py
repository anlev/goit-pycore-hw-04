from .salary_parser import parse_salaries

def total_salary(path: str) -> tuple[float, float]:
    salaries = parse_salaries(path)
    return calculate_total_and_average_salary(salaries)

def calculate_total_and_average_salary(salaries: list[float]) -> tuple[float, float]:
    total = float(sum(salaries))
    average = total / len(salaries) if salaries else 0
    return total, average
