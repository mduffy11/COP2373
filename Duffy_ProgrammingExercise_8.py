import csv

def write_csv():

    students = int(input("How many students would you like to enter? "))

    for count in range(1, students + 1):
        full_name = input(f"Enter student #{count}'s first and last name: ").strip()
        name_parts = full_name.split(maxsplit=1)
        first_name = name_parts[0]
        last_name = name_parts[1]

        grades_input = input("Enter the three exam grades: ").replace(",", " ")
        grade_parts = grades_input.split()
        exam1 = int(grade_parts[0])
        exam2 = int(grade_parts[1])
        exam3 = int(grade_parts[2])

write_csv()