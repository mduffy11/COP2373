import csv
import numpy as np

def load_grades(filename):
    grade_rows = []

    with open(filename, "r", newline="") as csv_file:
        reader = csv.reader(csv_file)
        next(reader) # Skip header row

        for row in reader:
            exams = [int(row[2]), int(row[3]), int(row[4])]
            grade_rows.append(exams)

    grades = np.array(grade_rows, dtype=int)

    return grades

def print_first_few_rows(grades, rows=4):
    print(f"First {rows} rows of the dataset:")
    print(grades[:rows])

grades = load_grades("grades.csv")
print_first_few_rows(grades)