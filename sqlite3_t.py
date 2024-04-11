import sqlite3
from employee import Employee


# Creating employee instances
employee1 = Employee("Asfr", "Hassan", 400000)
employee2 = Employee("Anwr", "Amr", 100000)
employee3 = Employee("Ahmgd", "Hany", 600000)
employee4 = Employee("Ali", "Ashraf", 600000)



def insert_emp(employee: Employee):
    # with sqlite3.connect("employee.db") as conn:
    #     cursor = conn.cursor()
    #     cursor.execute("INSERT INTO employees VALUES (?,?,?)", (employee.first, employee.last, employee.salary))
    #     conn.commit()
    with connection:
        cursor.execute("INSERT INTO employees VALUES (:first, :last, :salary)", employee.__dict__)

def get_emps_by_name(lastname: str):
    # with sqlite3.connect("employee.db") as conn:
    #     cursor = conn.cursor()
    #     cursor.execute("SELECT * FROM employees WHERE last=?", (lastname,))
    #     return cursor.fetchall()
    try:
        with connection:
            cursor.execute("SELECT * FROM employees WHERE last=?", (lastname,))
            return cursor.fetchall()
    except Exception as e:
        print("The name does not exist in the database.")
        print(e)


def update_salary(emp: Employee, salary: int):
    # with sqlite3.connect("employee.db") as conn:
    #     cursor = conn.cursor()
    #     cursor.execute("UPDATE employees SET salary=? WHERE emp_id=?", (pay, emp_id))
    #     conn.commit()
    with connection:
        cursor.execute("UPDATE employees SET salary=? WHERE first=? AND last=?", (salary, emp.first, emp.last))

def remove_emp(emp: Employee):
    # with sqlite3.connect("employee.db") as conn:
    #     cursor = conn.cursor()
    #     cursor.execute("DELETE FROM employees WHERE emp_id=?", (emp_id,))
    #     conn.commit()
    with connection:
        cursor.execute("DELETE FROM employees WHERE first=? AND last=?", (emp.first, emp.last))


# Init the connection
# connection = sqlite3.connect(":memory:")
connection = sqlite3.connect("employee.db")
# print(connection)

# Secondly init the executor [cursor]
cursor = connection.cursor()

# Create a db then add it to the connection object
# cursor.execute("CREATE DATABASE IF NOT EXISTS employee")

# Create a tables then add it to the connection object
cursor.execute("CREATE TABLE IF NOT EXISTS employees (first TEXT, last TEXT, salary INTEGER)")

# # Insert data into the person table
# #! NOT RECOMMENDED dynamically input
# cursor.execute("""
# INSERT INTO employees VALUES
#     ('Amr', 'Hassan', 40000),
#     ('Hassan', 'Amr', 50000),
#     ('Ali', 'Hassan', 60000),
#     ('{}', '{}', '{}'),
#     ('{}', '{}', '{}')
#
# """.format(employee1.first, employee1.last, employee1.salary, employee2.first, employee2.last, employee2.salary))
#
# # Insert data into the person table
# # ? RECOMMENDED WITH PREPARED STATEMENT [TUPLES]
# cursor.execute("INSERT INTO employees VALUES (?, ?, ?)", (employee3.first, employee3.last, employee3.salary))
# # ? RECOMMENDED WITH PREPARED STATEMENT [DICT]
# cursor.execute("INSERT INTO employees VALUES (:first, :last, :salary)", employee4.__dict__)
#
# # Fetch[Query] data from person
# cursor.execute("SELECT * FROM employees")
# results = cursor.fetchall()
# for row in results:
#     print(row)


# Manipulate data in the table with using functions

insert_emp(employee1)
insert_emp(employee2)
insert_emp(employee3)


emp = get_emps_by_name("Hassan")
print(emp)

update_salary(employee3, 7000000)
remove_emp(employee1)

emp = get_emps_by_name("Hassan")
print(emp)

# Commit the query
connection.commit()

# Close the connection
connection.close()
