student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
exam = student_scores[0]
for num in student_scores:
  if num > exam:
    exam = num
print(exam)