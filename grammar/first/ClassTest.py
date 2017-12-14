class Employee:

    """
    类测试
    """
    empCount = 0

    def __init__(self, salary, name):
        self.name = name
        self.salary = salary
        Employee.empCount+=1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmp(self):
        print("Name : ", self.name, "Salary : ", self.salary)



emp1 = Employee("huang", 2000)
emp1.displayCount()
emp1.displayEmp()


