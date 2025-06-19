# This is a python program to enter students' names and grades (out of 100) (the number of students should be decided by the user) and the program will do the following:
# 1- Prints students names and grades
# 2- Prints the average grade of the class
# 3- Prints the highest grade earned (Student name and grade)
# 4- Prints the count of students who passed (grade >= 60)

# it includes loops, lists and functions.
# the code have the following functions  display_student_summary ,  get_avg_grade ,  get_heighest_grade ,  count_passed 

name = input("Enter your name: ")
print("Welcome",name,"!")

num_of_students = int(input("Please enter the number of students you have:"))
students=[]
for i in range(num_of_students):
    name= input("Enter the student's name: ")
    grade= float(input("Enter the student's grade: "))
    while grade > 100 or grade < 0:
        print("Please enter a grade between 0 and 100.")
        grade = float(input("Enter the grade: "))
    students.append((name,grade))
number = 0

while number < 5:
    print("\nKindly choose one of the options below:")
    print("A - See the students' names and grades")
    print("B - Check the average grade of the class")
    print("C - Check the highest grade earned")
    print("D - Display the count of students who passed")
    print("Q - Exit the menu early")

    case = input("Choose an option (A, B, C, D, or Q): ").upper()
  if case =="A":
     number+=1
     print(students)
     
  if case == "B":
    sum = 0
    for student in students:
        sum += student[1]  # student[1] is the grade
    average = sum / len(students)
    number+=1
    print("Average grade is:", average)

  elif case=="C":
    highest_grade=0
    student_with_highest_grade =""

    for student in students:
        __name__=student[0]
        __grade__=student[1]
        if __grade__>highest_grade:
            highest_grade= __grade__
            student_with_highest_grade=__name__
            number+=1
    print("The highest grade is:",highest_grade,"earned by:",student_with_highest_grade)

  elif case=="D":
     passed_count=0
     for student in students:
       __grade__=student[1]
       if __grade__>=60:
            passed_count+=1
            number+=1
     print("Count of students who passed the exam is:",passed_count)

  elif case == "Q":
        print("Exiting the program. Goodbye!")
        break