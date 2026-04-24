class Student:
    def __init__(self, name, student_id, gpa):
        self.__name = name
        self.__student_id = student_id
        self.__gpa = gpa
    def get_student_info(self):
        print("Name:", self.__name)
        print("Student ID:", self.__student_id)
        print("GPA:", self.__gpa)

student1 = Student("Steph", "2023-001", 1.00)

student1.get_student_info()
#kscm