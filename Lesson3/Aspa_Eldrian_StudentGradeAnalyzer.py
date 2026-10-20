# Raw input records including invalid test cases
raw_records = [
    "Ana,88,92,90",
    "Ben,70,72,74",
    "Cara,95,91,94",
    "Dan,78,80,76",
    "Ella,85,89,87",
    "Fred,90,85",
    "Gina",
    "Henry,90,eighty,85",
    "Ivy,",
]

PASSING_GRADE = 75
student_scores = {}

# PART A: Parse raw records safely
for record in raw_records:
    fields = record.split(",")

    # Check field count guardian
    if len(fields) != 4:
        print(f"Skipped invalid record: {record}")
        continue

    name = fields[0].strip()
    scores = []
    has_error = False

    # Convert score fields to numbers
    for score_str in fields[1:]:
        try:
            scores.append(float(score_str.strip()))
        except ValueError:
            has_error = True
            break

    # Skip record if numeric conversion failed
    if has_error:
        print(f"Skipped invalid record: {record}")
        continue

    student_scores[name] = scores

# PART B: Display records alphabetically
print("\nORGANIZED STUDENT RECORDS")
print("-" * 35)
for name in sorted(student_scores.keys()):
    print(f"{name}: {student_scores[name]}")

ranking = []
passed_count = 0
failed_count = 0
sum_of_averages = 0

# PART C: Calculate student metrics
for name, scores in student_scores.items():
    if not scores:
        continue

    total = sum(scores)
    count = len(scores)
    average = total / count
    highest_score = max(scores)
    lowest_score = min(scores)

    if average >= PASSING_GRADE:
        remark = "Passed"
        passed_count += 1
    else:
        remark = "Failed"
        failed_count += 1

    sum_of_averages += average
    ranking.append((average, name, highest_score, lowest_score, remark))

# PART D: Sort and print rankings
ranking.sort(reverse=True)

print("\nSTUDENT GRADE REPORT")
print(f"{'Rank':<5} {'Name':<8} {'Average':<8} {'Highest':<8} {'Lowest':<8} {'Remark'}")
print("-" * 50)

for rank, (avg, name, highest, lowest, remark) in enumerate(ranking, start=1):
    print(f"{rank:<5} {name:<8} {avg:<8.2f} {highest:<8.0f} {lowest:<8.0f} {remark}")

# PART E: Print class summary
total_students = len(ranking)
class_average = sum_of_averages / total_students if total_students > 0 else 0.0

print("\nCLASS SUMMARY")
print("-" * 35)
print(f"Number of Students: {total_students}")
print(f"Passed:             {passed_count}")
print(f"Failed:             {failed_count}")
print(f"Class Average:      {class_average:.2f}")

if total_students > 0:
    print(f"Highest:            {ranking[0][1]} - {ranking[0][0]:.2f}")
    print(f"Lowest:             {ranking[-1][1]} - {ranking[-1][0]:.2f}")