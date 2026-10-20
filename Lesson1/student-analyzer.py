# First we need to display the student scores
scores = [85, 72, 91, 64, 78]

# Then calculate the scores
total_score = sum(scores)
average_score = total_score / len(scores) if len(scores) > 0 else 0
highest_score = max(scores)
lowest_score = min(scores)

# Then display the initial scores
print("Student Scores:")
for score in scores:
    print(score)

print()

passed_count = 0
failed_count = 0

# the logic 

for index in range(len(scores)):
    x = scores[index]

    if x >= 75:
        if x >= 90:
            remark = "Excellent"
        elif x >= 80: 
            remark = "Very Good"
        else:
            remark = "Good"
        
        print(f"Student {index + 1}: {x} - {remark} - Passed")
        passed_count += 1
    else:
        print(f"Student {index + 1}: {x} - Failed")
        failed_count += 1

print()

# Display the summaries using the variables 

print(f"Total score: {total_score}")
print(f"Average score: {int(average_score) if average_score.is_integer() else average_score}")
print(f"Highest score: {highest_score}")
print(f"Lowest score: {lowest_score}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")