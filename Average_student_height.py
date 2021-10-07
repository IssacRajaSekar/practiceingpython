# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
student_height=0
for height in student_heights:
  print(height)
  student_height+=height
print(student_height)
students=0
for student in student_heights:
  students+=1
print(students)
average=round(student_height/students)
print(average)