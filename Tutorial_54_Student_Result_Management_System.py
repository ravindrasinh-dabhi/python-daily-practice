#Build a program that accepts student marks, calculates percentages,
#assigns grades, and displays a result report.
#Accepts the names of 5 students.
#Takes marks in 3 subjects for each student.
#Calculates each student's total and percentage.
#Assigns grades using these rules:

def calculate_percentage(obtained):
    p=obtained/3

    return p
def grade_calculation(x):
      if x>=90:
       return"A"
      elif x>=80 and x<90:
       return "B"
      elif x>=70 and x<80:
       return"C"
      elif x>=60 and x<70:
       return "D"
      else:
       return "F"


students={}
for i in range(1,6):
 name= input(f"Enter {i} stundet name : ")

 marks=[]

 for sub in ["Python","Maths","Electrical"]:
   mark=float(input(f"Enter the marks of {sub}"))
   if mark<0 or mark>100:
     print("Enter valid marks")
     break
   else:
      marks.append(mark)
 total_obtained=sum(marks)
 percentage=calculate_percentage(total_obtained)
 grade=grade_calculation(percentage)
 students[name] = {"marks": marks,"percentage": percentage,"grade": grade}




    

    