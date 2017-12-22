class Person():
    def __init__(self,age,name):
        self.name=name
        self.age=age
    def birthday(self):
        self.age=self.age+1

class Parent(Person):
    def __init__(self,age,name):
        Person.__init__(self,age,name)
        self.children=[]
    def add_child(self,child):
        self.children.append(child)
    def print_children(self):
        print("the children of ",self.name," are :")
        for child in self.children:
            print(child.name)

ben=Parent(31,"ben")
mark=Person(23,"Mark")
john=Person(25,"john")

print(ben.age)
ben.add_child(mark)
ben.add_child(john)
ben.print_children()




