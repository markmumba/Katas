class Employee:
    comp_population = 0
    raise_amount = 1.04

    def __init__(self, first, second, third):
        self.firstname = first
        self.secondname = second
        self.pay = third
        Employee.comp_population += 1

    def full_name(self):
        return'{} {}'.format(self.firstname, self.secondname)

    def increase_pay(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def remove_dash(cls, name_string):
        first, second, third = name_string.split('-')
        return cls(first, second, third)


class Develpoer(Employee):
    raise_amount=1.05

    def __init__(self,first,second,third,language):
        Employee.__init__(self,first,second, third)
        self.prog_language=language

class Manager(Employee):

    def __init__(self,first,second,third, employees=None):
        Employee.__init__(self,first,second,third)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees

    def add_employee(self):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_all(self):
        for employee in self.employees:
            print ("-->",employee.full_name())


employee1 = Employee("john", "mwangi", 95902)
employee2 = Employee("markian", "mumba", 100000)
employee1 = Employee("samuel", "munene", 40000)
employee4 = Employee("nazarine", "njoki", 50000)
employee5 = Employee("christine", "wambui", 59020)
employee6 = Develpoer("maradona","messi",120000,"Python")
manger_1=Manager("Walter","O,Brian",150000,[employee1,employee2,employee4,employee5,employee6])

manger_1.print_all()


# print(employee6.prog_language)




# print(employee1.pay)
# print(employee1.full_name())
# print(employee1.pay)
# employee1.increase_pay()
# print(employee1.pay)
# print(Employee.comp_population)
