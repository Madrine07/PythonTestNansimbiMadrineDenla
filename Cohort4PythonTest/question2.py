# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F

# SOLUTION
def student_grades():
    
   subject_score = int(input("Enter the subject score: "))

   if subject_score >= 90:
       print(f"The student grade is Grade A")
   elif subject_score >= 80:
       print(f"The student grade is Grade B")
   elif subject_score >= 70:
       print(f"The student grade is Grade C")
   elif subject_score >= 60:
       print(f"The student grade Grade D")
   elif subject_score >= 40:
       print(f"The student grade is Grade E")
   else:
       print(f"The student grade is Grade F")
       
student_grades()