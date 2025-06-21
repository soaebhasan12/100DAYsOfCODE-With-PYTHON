# EXERCISE : HIGHEST SCORE IN THE LIST

student_scores = input("Input a list of student scores : ").split()

# This loop is use for taking input and store them into list
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    
print(student_scores)

max_score = 0

for score in student_scores:
    if max_score < score:
        max_score = score

print(f"The Highest Score in the List is : {max_score}")