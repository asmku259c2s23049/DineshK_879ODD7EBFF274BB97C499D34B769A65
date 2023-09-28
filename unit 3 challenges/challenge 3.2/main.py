class Student:
  def __init__(self,name,roll_number,cgpa):
    self.name = name
    self.roll_number =roll_number
    self.cgpa=cgpa

def sort_students(student_list):
    sorted_students =sorted(student_list,key=lambda student:student.cgpa,reverse=True)
    return sorted_students


students =[Student("Keerthi","C2S234",9.0),Student("Rajini","C2S235",6.9),Student("Ram","C2S236",7.6),Student("Raj","C2S238",9.7),Student("Karthi","C2S230",5.9)]

sorted_students=sort_students(students)

for student in sorted_students:
   print("Name : {} ,  Roll Number:  {} ,CGPA : {}".format(student.name,student.roll_number,student.cgpa))
