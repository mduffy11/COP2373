import csv

def write_csv():

    students = int(input("How many students would you like to enter? "))

    with open("grades.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        for count in range(1, students + 1):

            while True:
                full_name = input(f"Enter student #{count}'s first and last name: ").strip()
                name_parts = full_name.split(maxsplit=1)

                if (
                        len(name_parts) == 2
                        and any(char.isalpha() for char in name_parts[0])
                        and any(char.isalpha() for char in name_parts[1])
                ):
                    first_name = name_parts[0]
                    last_name = name_parts[1]
                    break

                print("Please enter a valid first and last name.")

            while True:
                grades_input = input(
                    "Enter the three exam grades: "
                ).replace(",", " ")

                grade_parts = grades_input.split()

                if len(grade_parts) == 3 and all(part.isdigit() for part in grade_parts):
                    exam1 = int(grade_parts[0])
                    exam2 = int(grade_parts[1])
                    exam3 = int(grade_parts[2])
                    break

                print("Please enter exactly three numerical grades separated by spaces or commas.")

            writer.writerow([first_name, last_name, exam1, exam2, exam3])
    print("The grades have been written to the grades.csv file.")

def read_csv():

    with open("grades.csv", "r", newline="") as csv_file:
        reader = csv.reader(csv_file)

        print("\nStudent Grades")
        print()

        for row_number, row in enumerate(reader):
            print("{:<15}{:<20}{:<10}{:<10}{:<10}".format(
                row[0], row[1], row[2], row[3], row[4]
            ))

            if row_number == 0:
                print("-" * 65)

def main():

    write_csv()
    print("\nThe grades.csv file has been created.\n")
    read_csv()


if __name__ == "__main__":
    main()

write_csv()