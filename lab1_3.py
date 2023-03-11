
name = input("Please enter the student's name: ")
lab_grade = float(input("Please enter the student's lab grade : "))
midterm_grade = float(input("Please enter the student's midterm grade : "))
final_grade = float(input("Please enter the student's final grade : "))


final_score = 0.25 * lab_grade + 0.35 * midterm_grade + 0.4 * final_grade


print(f"{name}'s final score is: {final_score:.2f}")
