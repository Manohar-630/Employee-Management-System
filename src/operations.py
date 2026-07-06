from database import connect_db


def add_employee(employee):
    connection = connect_db()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        sql = """
        INSERT INTO employees(name, department, salary, email)
        VALUES(%s, %s, %s, %s)
        """

        values = (
            employee.name,
            employee.department,
            employee.salary,
            employee.email
        )

        cursor.execute(sql, values)
        connection.commit()

        print("\n✅ Employee Added Successfully!\n")

    except Exception as e:
        print(f"\n❌ Error: {e}")

    finally:
        cursor.close()
        connection.close()


def view_employees():
    connection = connect_db()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM employees")

        employees = cursor.fetchall()

        if not employees:
            print("\nNo Employees Found.\n")
            return

        print("\n" + "=" * 70)

        for emp in employees:
            print(f"""
Employee ID : {emp[0]}
Name        : {emp[1]}
Department  : {emp[2]}
Salary      : ₹{emp[3]}
Email       : {emp[4]}
""")

    except Exception as e:
        print(f"\n❌ Error: {e}")

    finally:
        cursor.close()
        connection.close()


def search_employee():
    connection = connect_db()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        emp_id = input("Enter Employee ID: ")

        cursor.execute(
            "SELECT * FROM employees WHERE id=%s",
            (emp_id,)
        )

        employee = cursor.fetchone()

        if employee:
            print(f"""
Employee ID : {employee[0]}
Name        : {employee[1]}
Department  : {employee[2]}
Salary      : ₹{employee[3]}
Email       : {employee[4]}
""")
        else:
            print("\n❌ Employee Not Found!")

    except Exception as e:
        print(f"\n❌ Error: {e}")

    finally:
        cursor.close()
        connection.close()


def update_employee():
    connection = connect_db()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        emp_id = input("Enter Employee ID to Update: ")

        cursor.execute(
            "SELECT * FROM employees WHERE id=%s",
            (emp_id,)
        )

        employee = cursor.fetchone()

        if employee is None:
            print("\n❌ Employee Not Found!")
            return

        print("\nEnter New Details\n")

        name = input("Name: ")
        department = input("Department: ")
        salary = float(input("Salary: "))
        email = input("Email: ")

        cursor.execute("""
            UPDATE employees
            SET name=%s,
                department=%s,
                salary=%s,
                email=%s
            WHERE id=%s
        """, (
            name,
            department,
            salary,
            email,
            emp_id
        ))

        connection.commit()

        print("\n✅ Employee Updated Successfully!\n")

    except Exception as e:
        print(f"\n❌ Error: {e}")

    finally:
        cursor.close()
        connection.close()


def delete_employee():
    connection = connect_db()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        emp_id = input("Enter Employee ID to Delete: ")

        cursor.execute(
            "SELECT * FROM employees WHERE id=%s",
            (emp_id,)
        )

        employee = cursor.fetchone()

        if employee is None:
            print("\n❌ Employee Not Found!")
            return

        cursor.execute(
            "DELETE FROM employees WHERE id=%s",
            (emp_id,)
        )

        connection.commit()

        print("\n✅ Employee Deleted Successfully!\n")

    except Exception as e:
        print(f"\n❌ Error: {e}")

    finally:
        cursor.close()
        connection.close()