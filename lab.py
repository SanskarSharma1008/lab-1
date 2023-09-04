class Employee:
    def _init_(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def _str_(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"

def sort_employees(employees, key):
    if key == 1:
        return sorted(employees, key=lambda emp: emp.age)
    elif key == 2:
        return sorted(employees, key=lambda emp: emp.name)
    elif key == 3:
        return sorted(employees, key=lambda emp: emp.salary)
    else:
        return employees

def main():
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000),
    ]

    print("Employee Sorting Options:")
    print("1. Sort by Age")
    print("2. Sort by Name")
    print("3. Sort by Salary")

    try:
        option = int(input("Enter your choice (1/2/3): "))

        if option in [1, 2, 3]:
            sorted_employees = sort_employees(employees, option)
            print("Sorted Employee Data:")
            for emp in sorted_employees:
                print(emp)
        else:
            print("Invalid option selected. No sorting performed.")
    except ValueError:
        print("Invalid input. Please enter a valid choice (1/2/3).")

if _name_ == "_main_":
    main()