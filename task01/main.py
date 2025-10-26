from salary import total_salary, run_salary_tests

def main():
    run_salary_tests()

    total, average = total_salary("salaries.txt")
    print(f"Total salary: {total}, Average salary: {average}")

if __name__ == "__main__":
    main()