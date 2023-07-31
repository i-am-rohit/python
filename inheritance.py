class Employee:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show_details(self):
        print(f"The employee id is  {self.id} and Name is {self.name}")


class Programmer(Employee):
    def show_languages(self):
        print("the default language is python")




e1 = Employee("Rohit", 1)
e1.show_details()

e2 = Programmer("Mohit",2)
e2.show_details()
e2.show_languages()