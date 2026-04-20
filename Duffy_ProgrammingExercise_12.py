import csv
import numpy as np


def load_grades(filename):
    # Create a list to store the exam grade rows.
    grade_rows = []

    # Open the CSV file.
    with open(filename, "r", newline="") as csv_file:
        # Create the CSV reader.
        reader = csv.reader(csv_file)

        # Skip the header row.
        next(reader)

        # Read each row from the file.
        for row in reader:
            # Extract the three exam grades.
            exams = [int(row[2]), int(row[3]), int(row[4])]

            # Add the exam grades to the list.
            grade_rows.append(exams)

    # Convert the list of lists into a NumPy array.
    grades = np.array(grade_rows, dtype=int)

    # Return the NumPy array.
    return grades


def first_few_rows(grades, rows=4):
    # Print the first few rows of the dataset.
    print(f"First {rows} rows of the dataset:")
    print(grades[:rows])


def exam_statistics(grades):
    # Calculate the mean for each exam.
    exam_means = np.mean(grades, axis=0)

    # Calculate the median for each exam.
    exam_medians = np.median(grades, axis=0)

    # Calculate the standard deviation for each exam.
    exam_std_devs = np.std(grades, axis=0)

    # Calculate the minimum for each exam.
    exam_mins = np.min(grades, axis=0)

    # Calculate the maximum for each exam.
    exam_maxes = np.max(grades, axis=0)

    # Print the statistics for each exam.
    for i in range(grades.shape[1]):
        print(f"\nExam {i + 1} Statistics:")
        print(f"Mean: {exam_means[i]:.2f}")
        print(f"Median: {exam_medians[i]:.2f}")
        print(f"Standard Deviation: {exam_std_devs[i]:.2f}")
        print(f"Minimum: {exam_mins[i]}")
        print(f"Maximum: {exam_maxes[i]}")


def total_statistics(grades):
    # Calculate the mean for all grades combined.
    total_mean = np.mean(grades)

    # Calculate the median for all grades combined.
    total_median = np.median(grades)

    # Calculate the standard deviation for all grades combined.
    total_std_dev = np.std(grades)

    # Calculate the minimum for all grades combined.
    total_min = np.min(grades)

    # Calculate the maximum for all grades combined.
    total_max = np.max(grades)

    # Print the total statistics.
    print("\nTotal Dataset Statistics:")
    print(f"Mean: {total_mean:.2f}")
    print(f"Median: {total_median:.2f}")
    print(f"Standard Deviation: {total_std_dev:.2f}")
    print(f"Minimum: {total_min}")
    print(f"Maximum: {total_max}")


def pass_count(grades):
    # Count the passing grades for each exam.
    passes = np.sum(grades >= 60, axis=0)

    # Count the failing grades for each exam.
    fails = np.sum(grades < 60, axis=0)

    # Print the pass and fail counts for each exam.
    for i in range(grades.shape[1]):
        print(f"\nExam {i + 1} Pass/Fail Counts:")
        print(f"Passed: {passes[i]}")
        print(f"Failed: {fails[i]}")


def total_percentage(grades):
    # Count all passing grades in the dataset.
    total_passes = int(np.sum(grades >= 60))

    # Count all grades in the dataset.
    total_grades = grades.size

    # Calculate the overall pass percentage.
    pass_percentage = (total_passes / total_grades) * 100

    # Print the overall pass percentage.
    print(f"\nTotal Pass Percentage: {pass_percentage:.2f}%")


def main():
    # Load the grades from the CSV file.
    grades = load_grades("grades.csv")

    # Print the first few rows of the dataset.
    first_few_rows(grades)

    # Print the statistics for each exam.
    exam_statistics(grades)

    # Print the total statistics for the dataset.
    total_statistics(grades)

    # Print the pass and fail counts for each exam.
    pass_count(grades)

    # Print the overall pass percentage.
    total_percentage(grades)


# Run the main function.
if __name__ == "__main__":
    main()