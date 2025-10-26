from cats import get_cats_info

def main():
    print("Test Basic\n")
    print(get_cats_info("cats_file.txt"))
    print("\n------------\n")

    print("Test No File\n")
    print(get_cats_info("no_file.txt"))
    print("\n------------\n")

    print("Test Invalid Format\n")
    print(get_cats_info("cats_file_invalid_format.txt"))

if __name__ == "__main__":
    main()