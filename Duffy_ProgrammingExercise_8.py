# Import the csv module.
import csv


def write_csv():
    """
    Collects student names and exam grades, then writes each student record
    to grades.csv.

    Parameters:
        None

    Variables:
        students (int): The number of student records to enter.
        writer (csv.writer): The csv writer object used to write rows to grades.csv.
        count (int): The numbered position of the current student record being entered.
        full_name (str): The student's full name entered by the user.
        name_parts (list): The student's full name split into first and last name parts.
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        grades_input (str): The three exam grades entered on one line.
        grade_parts (list): The three separated grade values entered by the user.
        exam1 (int): The student's first exam grade.
        exam2 (int): The student's second exam grade.
        exam3 (int): The student's third exam grade.

    Logic:
        1. Read the number of students to enter.
        2. Open grades.csv for writing with the csv module.
        3. Write the header row to grades.csv.
        4. Loop through each student record to collect a name and three grades.
        5. Validate the full name entry and split it into first and last name values.
        6. Validate the grade entry and convert the three values to integers.
        7. Write the completed student record to grades.csv.

    Return:
        None
    """

    # Read the number of student records to enter.
    print()
    students = int(input("How many students would you like to enter? "))

    # Open grades.csv for writing and prepare the csv writer object.
    with open("grades.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)

        # Write the header row to grades.csv.
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Loop through each student record and collect the required values.
        for count in range(1, students + 1):

            # Read and validate the student's full name.
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

            # Read and validate the student's three exam grades.
            while True:
                grades_input = input(
                    "Enter the three exam grades separated by spaces or commas: "
                ).replace(",", " ")

                grade_parts = grades_input.split()

                if len(grade_parts) == 3 and all(part.isdigit() for part in grade_parts):
                    exam1 = int(grade_parts[0])
                    exam2 = int(grade_parts[1])
                    exam3 = int(grade_parts[2])
                    break

                print("Please enter exactly three numerical grades separated by spaces or commas.")

            # Write the completed student record to grades.csv.
            writer.writerow([first_name, last_name, exam1, exam2, exam3])


def read_csv():
    """
    Reads grades.csv and displays the stored records in tabular format.

    Parameters:
        None

    Variables:
        reader (csv.reader): The csv reader object used to read rows from grades.csv.
        row_number (int): The numbered position of the current row in the file.
        row (list): The current row of data read from grades.csv.

    Logic:
        1. Open grades.csv for reading with the csv module.
        2. Print a title for the displayed table.
        3. Loop through each row in grades.csv.
        4. Display each row in aligned columns with string formatting.
        5. Print a separator line after the header row.

    Return:
        None
    """

    # Open grades.csv for reading and prepare the csv reader object.
    with open("grades.csv", "r", newline="") as csv_file:
        reader = csv.reader(csv_file)

        # Print the table title.
        print("\nStudent Grades")
        print()

        # Loop through each row and display the values in tabular format.
        for row_number, row in enumerate(reader):
            print(
                "{:<15}{:<20}{:<10}{:<10}{:<10}".format(
                    row[0], row[1], row[2], row[3], row[4]
                )
            )

            # Print a separator line after the header row.
            if row_number == 0:
                print("-" * 65)


def main():
    """
    Runs the csv writing and reading program.

    Parameters:
        None

    Variables:
        None

    Logic:
        1. Call write_csv() to collect student data and create grades.csv.
        2. Print a message confirming that grades.csv was created.
        3. Call read_csv() to display the stored records in tabular format.

    Return:
        None
    """

    # Call write_csv() to collect input and create grades.csv.
    write_csv()

    # Print a message confirming that grades.csv was created.
    print("\nThe grades.csv file has been created.\n")

    # Call read_csv() to display the stored records.
    read_csv()


# Call main() only when the file runs directly.
if __name__ == "__main__":
    main()

