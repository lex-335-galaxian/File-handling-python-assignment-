import os

print("Welcome to the Student GPA File")
file_name = input("Enter the name of the file: ")

# Check for file extension
if not os.path.splitext(file_name)[1]: 
    print("Error: file must have an extension (e.g., '.txt', '.doc', '.csv', '.ods').")
    print("_____________________")
    exit()

# Create the file or handle if it already exists
try:
    with open(file_name, "x") as f:
        print(f"File '{file_name}' has been created.")
        print("_____________________")
except FileExistsError:
    print(f"Error: File '{file_name}' already exists.")
    print("**********************")

# Function to calculate GPA
def add_student():
    try:
        num_courses = int(input("Number of courses offering: "))
        total_points = 0
        total_credits = 0

        for i in range(num_courses):
            print(f"\nCourse {i + 1}:")
            subject = input("Enter the name of the subject: ")
            credit_unit = float(input("Enter the credit unit for the subject: "))
            grade_alpha = input("Enter the grade for the subject (A-F): ").strip().upper()

            # Grade points mapping
            grade_points = {
                'A': 5.0,
                'B': 4.0,
                'C': 3.0,
                'D': 2.0,
                'E': 1.0,
                'F': 0.0,
            }

            if grade_alpha in grade_points:
                points = grade_points[grade_alpha] * credit_unit
                total_points += points
                total_credits += credit_unit
            else:
                print("Invalid grade entered. Please enter a valid grade (A, B, C, D, E, F).")
                continue

        # Calculate GPA
        if total_credits == 0:
            print("\nNo valid courses entered. Cannot calculate GPA.")
        else:
            gpa = total_points / total_credits
            print(f"\nYour GPA is: {gpa:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values for credit units and number of courses.")

add_student()


work = "add_student()"
f = open(file_name,"w")
f.write( work)
f.close()









'''import os 


print("welcome to the student GPA file")
file_name = input ("Enter the name of the file: ")
if not os.path.splitext(file_name)[1]: 
  print("Error: file must have an extention(e.g.,'.txt','.doc','.csv','.ods',)")
  print("_____________________")       
  cotinue

try:
  f = open(file_name, "x")
  print(f"file {file_name} has been created ")
  print("_____________________")
      
except FileExistsError:
  print(f"Error: File '{file_name}' already exists.")
  print("**********************")

def add_student():
  num = input("Number of courses offering : ")
  num_courses = int(num)
  print("Enter the name of the subject:")
  subject = input()
  print("Enter the credit unit for the subject:")
  credit_unit = input()
  print("enter the grade for the subject:")
  grade_alpha = input()

  subject_credit_dict = { subject: credit_unit}
  subject_grade_dict = { subject : grade_alpha}
  print(subject_credit_dict  )
  print(subject_grade_dict  )
  total_points = 0
  total_credits = 0
  
  for i in range(1, num_courses + 1):
        print(f"\nCourse {subject}:")
        grade = grade_alpha.isalpha().strip().upper()
        credits = float(credit_unit)
        grade_points = {
         'A': 5.0,
         'B': 4.0,
         'C': 3.0,
         'D': 2.0,
         'E': 1.0,
         'F': 0.0,
        }

        if grade in grade_points:
            points = grade_points[grade] * credits
            total_points += points
            total_credits += credits
        else:
            print("Invalid grade entered. Please enter a valid grade (A, B, C, D, F).")
            continue

  if total_credits == 0:
    print("\nNo valid courses entered. Cannot calculate GPA.")
  else:
    gpa = total_points / total_credits
    print(f"\nYour GPA is: {gpa:.2f}")
      
add_student() '''