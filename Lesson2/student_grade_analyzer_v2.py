def classify_grade(grade):
    """Return the classification and status of a grade."""
    if 90 <= grade <= 100:
        return ("Excellent", "Passed")
    elif 85 <= grade < 90:
        return ("Very Good", "Passed")
    elif 80 <= grade < 85:
        return ("Good", "Passed")
    elif 75 <= grade < 80:
        return ("Satisfactory", "Passed")
    else:
        return ("Needs Improvement", "Failed")


def load_students(filename):
    """Read valid student records from a text file and return them as a list."""
    students = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                # Remove surrounding whitespace
                cleaned_line = line.strip()

                # Skip blank lines or comment lines
                if not cleaned_line or cleaned_line.startswith("#"):
                    continue

                # Split record by comma
                fields = cleaned_line.split(",")

                # Accept only records with exactly three fields
                if len(fields) != 3:
                    continue

                student_id = fields[0].strip()
                name = fields[1].strip()

                # Validate grade value
                try:
                    grade = float(fields[2].strip())
                except ValueError:
                    continue  # Skip line if grade cannot be converted to float

                # Accept only valid grades from 0 to 100
                if 0 <= grade <= 100:
                    students.append({
                        "student_id": student_id,
                        "name": name,
                        "grade": grade
                    })

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except OSError as e:
        print(f"Error opening or reading file '{filename}': {e}")

    return students


def calculate_statistics(students):
    """Calculate and return the class statistics without using sum(), max(), or min()."""
    if not students:
        return None

    total_grade = 0
    passed_count = 0
    failed_count = 0
    highest_student = students[0]
    lowest_student = students[0]

    for student in students:
        grade = student["grade"]

        # Accumulator for total grade
        total_grade += grade

        # Counters for passed/failed status
        _, status = classify_grade(grade)
        if status == "Passed":
            passed_count += 1
        else:
            failed_count += 1

        # Track highest and lowest grade students
        if grade > highest_student["grade"]:
            highest_student = student

        if grade < lowest_student["grade"]:
            lowest_student = student

    num_students = len(students)
    average_grade = total_grade / num_students if num_students > 0 else 0.0

    return {
        "num_students": num_students,
        "average": average_grade,
        "passed": passed_count,
        "failed": failed_count,
        "highest": highest_student,
        "lowest": lowest_student
    }


def display_students(students):
    """Display all student records in a formatted table."""
    if not students:
        print("No student records available.")
        return

    print("\n" + "=" * 70)
    print(f"{'STUDENT ID':<12} | {'NAME':<20} | {'GRADE':<7} | {'CLASSIFICATION':<18} | {'STATUS'}")
    print("=" * 70)

    for student in students:
        classification, status = classify_grade(student["grade"])
        # Format name length to fit fixed display column
        name_display = student['name'][:20]
        print(f"{student['student_id']:<12} | {name_display:<20} | {student['grade']:<7.2f} | {classification:<18} | {status}")

    print("=" * 70)


def display_statistics(statistics):
    """Display the calculated class statistics."""
    if not statistics:
        print("No statistics to display.")
        return

    print("\nCLASS STATISTICS")
    print("-" * 35)
    print(f"Number of students: {statistics['num_students']}")
    print(f"Class average:      {statistics['average']:.2f}")
    print(f"Passed:             {statistics['passed']}")
    print(f"Failed:             {statistics['failed']}")
    print(f"Highest:            {statistics['highest']['name']} - {statistics['highest']['grade']:.2f}")
    print(f"Lowest:             {statistics['lowest']['name']} - {statistics['lowest']['grade']:.2f}")
    print("-" * 35)


def search_student(students, keyword):
    """Return records whose student number or name matches the keyword."""
    matches = []
    cleaned_keyword = keyword.lower().strip()

    for student in students:
        student_id_lower = student["student_id"].lower()
        name_lower = student["name"].lower()

        if cleaned_keyword in student_id_lower or cleaned_keyword in name_lower:
            matches.append(student)

    return matches


def save_report(students, statistics, filename="grade_report.txt"):
    """Write the student results and class statistics to a report file."""
    if not students or not statistics:
        print("Cannot save report: missing student records or statistics.")
        return

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("==================================================\n")
            file.write("            STUDENT GRADE ANALYZER REPORT          \n")
            file.write("==================================================\n\n")

            file.write("STUDENT RECORDS:\n")
            file.write("-" * 50 + "\n")
            file.write(f"{'ID':<12} {'NAME':<20} {'GRADE':<8} {'STATUS':<10} {'CLASSIFICATION'}\n")
            file.write("-" * 50 + "\n")

            for student in students:
                classification, status = classify_grade(student["grade"])
                file.write(f"{student['student_id']:<12} {student['name']:<20} {student['grade']:<8.2f} {status:<10} {classification}\n")

            file.write("\n" + "=" * 50 + "\n")
            file.write("CLASS STATISTICS:\n")
            file.write("-" * 50 + "\n")
            file.write(f"Total Students:     {statistics['num_students']}\n")
            file.write(f"Class Average:      {statistics['average']:.2f}\n")
            file.write(f"Passed Count:       {statistics['passed']}\n")
            file.write(f"Failed Count:       {statistics['failed']}\n")
            file.write(f"Highest Performing: {statistics['highest']['name']} ({statistics['highest']['grade']:.2f})\n")
            file.write(f"Lowest Performing:  {statistics['lowest']['name']} ({statistics['lowest']['grade']:.2f})\n")
            file.write("==================================================\n")

        print(f"\nReport successfully saved to '{filename}'.")

    except OSError as e:
        print(f"Error saving report to file '{filename}': {e}")


def main():
    """Run the menu-driven Student Grade Analyzer."""
    filename = "grades.txt"
    students = load_students(filename)

    if not students:
        print(f"No valid student records were loaded from '{filename}'. Please check the file.")
        return

    statistics = calculate_statistics(students)

    while True:
        print("\nSTUDENT GRADE ANALYZER")
        print("[1] Display all students")
        print("[2] Display class statistics")
        print("[3] Search for a student")
        print("[4] Save report")
        print("[5] Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_students(students)
        elif choice == "2":
            display_statistics(statistics)
        elif choice == "3":
            keyword = input("Enter student name or ID keyword to search: ")
            results = search_student(students, keyword)
            if results:
                print(f"\nFound {len(results)} matching record(s):")
                display_students(results)
            else:
                print(f"\nNo students found matching '{keyword}'.")
        elif choice == "4":
            save_report(students, statistics, "grade_report.txt")
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue


if __name__ == "__main__":
    main()