# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
total = 0
for number in range(2, 101, 2):
  total += number
print(total)

totalTwo = 0
for number in range(2, 101):
  if number % 2 == 0:
    totalTwo += number
print(totalTwo)


