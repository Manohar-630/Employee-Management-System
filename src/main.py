from employee import Employee
from operations import (
    add_employee,
    view_employees,
    search_employee,
    update_employee,
    delete_employee
)
from auth import login


def menu():
    while True:

        print("\n" + "=" * 50)
        print("       EMPLOYEE MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        print("=" * 50)

        choice = input("Enter your choice: ")

        if choice == "1":

            while True:
                name = input("Employee Name: ").strip()
                if name:
                    break
                print("❌ Name cannot be empty.")

            while True:
                department = input("Department: ").strip()
                if department:
                    break
                print("❌ Department cannot be empty.")

            while True:
                try:
                    salary = float(input("Salary: "))
                    if salary > 0:
                        break
                    print("❌ Salary must be greater than 0.")
                except ValueError:
                    print("❌ Please enter a valid salary.")

            while True:
                email = input("Email: ").strip()

                if "@" in email and "." in email:
                    break

                print("❌ Invalid email address.")

            employee = Employee(
                name,
                department,
                salary,
                email
            )

            add_employee(employee)

        elif choice == "2":

            view_employees()

        elif choice == "3":

            search_employee()

        elif choice == "4":

            update_employee()

        elif choice == "5":

            delete_employee()

        elif choice == "6":

            print("\nThank You for using Employee Management System.")
            print("Good Bye!\n")
            break

        else:

            print("\n❌ Invalid Choice. Please try again.\n")


if __name__ == "__main__":

    if login():
        menu()