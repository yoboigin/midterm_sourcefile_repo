# Hands-On Exercise: Student Grade Analyzer V2



## Goals

Develop a simple **Student Grade Analyzer Version 2**. The program must read student records from `grades.txt`. Each valid record contains a student number, student name, and final grade separated by commas.

Example record:

```text
2026-001,Ana Cruz,88
```

The program should ignore blank or invalid records, analyze all valid grades, let the user search for a student, and create a report file.

## Files Provided

- `student_grade_analyzer_starter.py` – starter program containing incomplete functions
- `grades.txt` – sample student records

Keep the three files in the same folder while testing the program.

## Grade Classification

Use the following classifications:

| Grade | Classification | Status |
| ---: | --- | --- |
| 90–100 | Excellent | Passed |
| 85–89 | Very Good | Passed |
| 80–84 | Good | Passed |
| 75–79 | Satisfactory | Passed |
| Below 75 | Needs Improvement | Failed |

Only grades from **0 to 100** are valid.

## Program Requirements

### Part A – Load and Validate the Records

Complete `load_students(filename)` so that it:

1. Opens the file in read mode.
2. Uses a `for` loop to process each line.
3. Removes surrounding whitespace using `strip()`.
4. Skips blank lines using `continue`.
5. Splits each nonblank line using `split(",")`.
6. Accepts only records containing exactly three fields.
7. Converts the grade to a number using `float()`.
8. Accepts only grades from 0 to 100.
9. Stores every valid record as a dictionary in a list.
10. Uses `try`/`except` to handle a missing file and invalid numeric grades.

Suggested dictionary structure:

```python
{"student_id": "2026-001", "name": "Ana Cruz", "grade": 88.0}
```

### Part B – Classify a Grade

Complete `classify_grade(grade)`.

- It must accept one grade as a parameter.
- It must return both the classification and status.
- Example: `classify_grade(88)` returns `("Very Good", "Passed")`.

### Part C – Analyze the Class

Complete `calculate_statistics(students)` without using `sum()`, `max()`, or `min()`.

Use a loop, counters, and an accumulator to determine:

- Number of students
- Class average
- Number of passed students
- Number of failed students
- Student with the highest grade
- Student with the lowest grade

Return the results in a dictionary. Prevent division by zero when the list is empty.

### Part D – Display All Students

Complete `display_students(students)` so it prints a readable table containing:

- Student number
- Student name
- Grade shown with two decimal places
- Classification
- Status

Use formatted strings. Use slicing if a name must be shortened for a fixed-width display.

### Part E – Search for a Student

Complete `search_student(students, keyword)`.

- Search by student number or name.
- Make the search case-insensitive using `lower()`.
- Permit partial-name matching using `in`.
- Return all matching records.

Example: searching for `ana` should find `Ana Cruz`.

### Part F – Save the Report

Complete `save_report(students, statistics, filename)`.

Write the following to `grade_report.txt`:

1. Report title
2. Each student's complete result
3. Class average
4. Passed and failed counts
5. Highest-performing student
6. Lowest-performing student

Use `with open(...)` and handle possible writing errors with `try`/`except`.

### Part G – Complete the Menu

Use a `while` loop to repeatedly show this menu:

```text
STUDENT GRADE ANALYZER
[1] Display all students
[2] Display class statistics
[3] Search for a student
[4] Save report
[5] Exit
```

Menu rules:

- Use `continue` after an invalid menu choice so the menu is shown again.
- Use `break` when the user selects Exit.
- Display a friendly message if no valid student data was loaded.

## Minimum Expected Output

```text
STUDENT GRADE ANALYZER
[1] Display all students
[2] Display class statistics
[3] Search for a student
[4] Save report
[5] Exit
Enter your choice: 2

CLASS STATISTICS
Number of students: 8
Class average: 81.88
Passed: 6
Failed: 2
Highest: Carla Reyes - 95.00
Lowest: Grace Lim - 68.00
```

*The exact layout may differ, but the computed results must be correct.*

## Testing Checklist

Before submitting, test the following situations:

- [ ] The program reads all valid records.
- [ ] Blank and invalid lines do not crash the program.
- [ ] A missing `grades.txt` file produces a friendly error message.
- [ ] Grades below 0 or above 100 are rejected.
- [ ] The average, passed count, and failed count are correct.
- [ ] The highest and lowest students are correct.
- [ ] Search works with uppercase, lowercase, and partial names.
- [ ] An invalid menu choice returns to the menu.
- [ ] The report is successfully saved and can be opened.



## Submission Requirements

Submit the following:

1. Completed `student_grade_analyzer.py`
2. Generated `grade_report.txt`
3. Sample Screenshots of Output (1-2 pictures)
4. Youtube Link of Video Demo (max of 3 minutes)
5. Attach and turn in.



