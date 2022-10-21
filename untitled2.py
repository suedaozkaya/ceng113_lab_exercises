#Ask the user for their homework, midterm and final grades.
#Calculate their course grade, which is a weighted average of these grades.
#Th eweights are 10% for the homework,30% for the midterm, and 60% for the final exam.
homework_grade = float(input("Enter your homework grade: "))
midterm_exam_grade = float(input("Enter your midterm exam grade: "))
final_exam_grade = float(input("Enter your final exam grade: "))

course_grade = homework_grade*10/100 + midterm_exam_grade*30/100 + final_exam_grade*60/100

print("Your course grade:",course_grade)

