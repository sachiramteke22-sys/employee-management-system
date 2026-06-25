class Employee:

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print(f"ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

employees = []

while True:
    print("\n1 Add Employee")
    print("2 View Employees")
    print("3 Exit")

    choice = input("Choice: ")

    if choice == "1":
        emp_id = input("ID: ")
        name = input("Name: ")
        salary = float(input("Salary: "))

        employees.append(Employee(emp_id, name, salary))

    elif choice == "2":
        for emp in employees:
            emp.display()

    elif choice == "3":
        break