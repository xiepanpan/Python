# import copy
#
# a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象
#
# b = a  # 赋值，传对象的引用
# c = copy.copy(a)  # 对象拷贝，浅拷贝
# d = copy.deepcopy(a)  # 对象拷贝，深拷贝
#
# a.append(5)  # 修改对象a
# a[4].append('c')  # 修改对象a中的['a', 'b']数组对象
#
# print("a=",a)
# print("b=",b)
# print("c=",c)
# print("d=",d)

student_data=[["Ben",{"Maths":66,"English":77}],["Mark",{"Art":55,"Maths":33}],["Paul",{"History":66,"Science":88}]]
# tuple
grades=((0,"fall"),(50,"D"),(60,"C"),(70,"B"),(80,"A"),(101,"cheat"))
class Student():
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark

    def print_report_card (self,report_student=None):
        for student in students :
            if(student[0]==report_student) or (report_student==None):
                print("Report card for student",student[0])
                for subject ,mark in student[1].items():
                    for grade in grades:
                        if mark <grade[0]:
                            print(subject,":",prev_grade)
                            break
                        prev_grade=grade[1]
            else:
                print("student not found")
                break

    def add_student (student_name):
        global students
        for student in students:
            if student[0]==student_name:
                return "student aleardy in database"
            students.append([student_name,{}])
            return "student added successfully"

    def add_mark(self,student_name ,subject ,mark):
        global  students
        for student in students :
            if student[0] == student_name:
                if subject in student[1].keys():
                    print(student_name,"aleardy has a mark for ", subject)
                    user_input=input("overwrite Y/N?")
                    if user_input=="y" or user_input=="Y":
                        student[1][subject]=mark
                        return "student's mark updated"
                    else :
                        return "student's mark not updated"
                else :
                    student[1][subject]=mark
                    return "student's mark added"

while True:
    print("Enter 1 to view all report cards")
    print("Enter 2 to view the report card for a student")
    print("Enter 3 to add a student ")
    print("Enter 4 to add a mark to a student ")
    print("Enter 5 to exit")

    try:
        user_chioce =int(input("choice:"))
    except ValueError:
        print("that is not a number i recognise")
        user_chioce=0

    if user_chioce==1:
        print_report_card();
    elif user_chioce==2:
        enter_student=input("which student?")
        print_report_card(enter_student)
    elif user_chioce==3:
        enter_student=input("student name?")
        print(add_student(enter_student))
    elif user_chioce==4:
        enter_student=input("which student?")
        enter_subject=input("subject?")
        num_error=True
        while num_error:
            num_error=False
            try:
                enter_mark=int(input("mark:"))
            except ValueError:
                print("I don't recognise that as a number")
                num_error=True
        print(add_mark(enter_student,enter_subject,enter_mark))
    elif user_chioce==5:
        break
    else:
        print("unknown choice")
    input("press enter to continue")
print("GoodBye")
