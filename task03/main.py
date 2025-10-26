import sys
from pathlib import Path
from colorama import init, Fore, Style

def color_dir(name: str) -> str:
    return Fore.BLUE + Style.BRIGHT + name + Style.RESET_ALL

def color_file(name: str) -> str:
    return Fore.GREEN + Style.BRIGHT + name + Style.RESET_ALL

def color_warning(name: str) -> str:
    return Fore.YELLOW + name + Style.RESET_ALL

def color_red(name: str) -> str:
    return Fore.RED + name + Style.RESET_ALL

def print_tree(root: Path):
    print(color_dir(root.name))

    def walk(dir_path: Path, depth: int):
        indent = "\t" * (depth + 1)

        try:
            entries = list(dir_path.iterdir())
        except Exception as e:
            print(indent + Fore.RED + f"Error: {e}" + Style.RESET_ALL)
            return

        entries.sort(key=lambda p: (not p.is_dir(), p.name.lower()))
        for entry in entries:
            if entry.is_dir():
                print(indent + color_dir(entry.name + "/"))
                walk(entry, depth + 1)
            else:
                print(indent + color_file(entry.name))

    walk(root, 0)

def main():
    init(autoreset=True)

    if len(sys.argv) != 2:
        print(color_warning("Usage: python main.py /absolute/path/to/dir"))
        return

    path = Path(sys.argv[1])

    if not path.exists():
        print(color_red(f"Error: path does not exist: {path}"))
        return

    if not path.is_dir():
        print(color_red(f"Error: not a directory: {path}"))
        return

    print_tree(path)

if __name__ == "__main__":
    main()