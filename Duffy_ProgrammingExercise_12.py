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

def print_exam_statistics(grades):
    # Calculate statistics for each exam column.
    exam_means = np.mean(grades, axis=0)
    exam_medians = np.median(grades, axis=0)
    exam_std_devs = np.std(grades, axis=0)
    exam_mins = np.min(grades, axis=0)
    exam_maxes = np.max(grades, axis=0)

    # Print the statistics for each exam.
    for i in range(grades.shape[1]):
        print(f"\nExam {i + 1} Statistics:")
        print(f"Mean: {exam_means[i]:.2f}")
        print(f"Median: {exam_medians[i]:.2f}")
        print(f"Standard Deviation: {exam_std_devs[i]:.2f}")
        print(f"Minimum: {exam_mins[i]}")
        print(f"Maximum: {exam_maxes[i]}")

def print_total_statistics(grades):
    # Calculate total statistics for all exam grades combined.
    total_mean = np.mean(grades)
    total_median = np.median(grades)
    total_std_dev = np.std(grades)
    total_min = np.min(grades)
    total_max = np.max(grades)

    # Print the total statistics.
    print("\ntotal Dataset Statistics:")
    print(f"Mean: {total_mean:.2f}")
    print(f"Median: {total_median:.2f}")
    print(f"Standard Deviation: {total_std_dev:.2f}")
    print(f"Minimum: {total_min}")
    print(f"Maximum: {total_max}")

grades = load_grades("grades.csv")
print_first_few_rows(grades)
print_exam_statistics(grades)
print_total_statistics(grades)