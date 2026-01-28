class Employee:
    def __init__(self, name, age, serviceyr, salary):
        self.name = name
        self.age = age
        self.serviceyr = serviceyr
        self.salary = salary
        print("Employee object created")

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getServiceYear(self):
        return self.serviceyr

    def getSalary(self):
        return self.salary

    def __del__(self):
        print("Employee object destroyed")


# Create an Employee object
name = input("Enter name: ")
age = int(input("Enter age: "))
serviceyr = int(input("Enter years of service: "))
salary = float(input("Enter salary: "))

emp = Employee(name, age, serviceyr, salary)

print("\n--- Employee Details ---")
print("Name:", emp.getName())
print("Age:", emp.getAge())
print("Service Years:", emp.getServiceYear())
print("Salary:", emp.getSalary())