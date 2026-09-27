class Employee:

    def __init__(self, employee_id, name, age, salary):
        self.__employee_id = employee_id
        self.name = name
        self.age = age
        self.__salary = salary

    def get_employee_id(self):
         print(self.__employee_id)

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_salary(self):
       print(self.__salary)

    def set_salary(self, salary):
        self.__salary = salary

    def display(self):
        print("Employee Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.__employee_id)
        print("Salary:", self.__salary)

    def __del__(self):
        print("Employee object deleted.")

    def __del__(self):
        print("Employee object deleted.")

class Manager(Employee):

    def __init__(self, employee_id, name, age, salary, department):
        super().__init__(employee_id, name, age, salary)
        self.department = department

    def display(self):
        print("Manager Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary: ", self.get_salary())
        print("Department:", self.department)

class Developer(Employee):

    def __init__(self, employee_id, name, age, salary, programming_language):
        super().__init__(employee_id, name, age, salary)
        self.programming_language = programming_language

    def display(self):
        print("Developer Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary:", self.get_salary())
        print("Programming Language:", self.programming_language)

employees = []

while True:

    print("\n   Employee Management System")
    print("1. Create an Employee")
    print("2. Create a Manager")
    print("3. Create a Developer")
    print("4. Show Details")
    print("5. Update Salary")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        employee_id = int(input("Enter Employee ID: "))
        salary = float(input("Enter Salary: "))

        employee = Employee(employee_id, name, age, salary)
        employees.append(employee)

        print("\nEmployee created successfully.")

    elif choice == "2":

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        employee_id = int(input("Enter Employee ID: "))
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")

        manager = Manager(employee_id, name, age, salary, department)
        employees.append(manager)

        print("\nManager created successfully.")

    elif choice == "3":

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        employee_id = int(input("Enter Employee ID: "))
        salary = float(input("Enter Salary: "))
        language = input("Enter Programming Language: ")

        developer = Developer(employee_id,name,age,salary,language)
        employees.append(developer)

        print("\nDeveloper created successfully.")

    elif choice == "4":

        if len(employees) == 0:
            print("\nNo employees available.")

        else:
            print("\n   Employee Details")

            for employee in employees:
                employee.display()

    elif choice == "5":

        employee_id = input("Enter Employee ID: ")
        new_salary = float(input("Enter New Salary: "))

        found = False

        for employee in employees:

            if employee.get_employee_id() == employee_id:
                employee.set_salary(new_salary)
                print("Salary updated successfully.")
                found = True
                break
              
        if found == False:
            print("Employee not found.")

    elif choice == "6":

        print("\nExiting the system. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please try again.")