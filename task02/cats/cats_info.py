from .cats_parser import parse_cat_line

def get_cats_info(path: str) -> list[dict[str, int]]:
    cats: list[dict[str, int]] = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, 1):
                try:
                    cats.append(parse_cat_line(line))
                except ValueError as e:
                    print(f"Line {line_number}: {e} in {line}")
    except Exception as e:
        print('An exception occurred: {}'.format(e))


    return cats