import sqlite3

connection = sqlite3.connect('employee.db')

cursor = connection.cursor()

done = 10


def add_employee():

    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    age = input("Enter age: ")
    salary = input("Enter salary: ")
    ssn = input("Enter SSN: ")
    dcode = input("Enter department code: ")

    cursor.execute(f"""
    INSERT INTO employee
    VALUES ('{fname}','{lname}',{age},{salary},'{ssn}');
    """)

    connection.commit()
    print("1 table created")

    add_employee_department(dcode, ssn)


def add_department():
    dname = input("Enter department name: ")
    dcode = input("Enter department code: ")
    dlocation = input("Enter department location: ")
    description = input("Enter role of department: ")

    cursor.execute(f"""
    INSERT INTO department
    VALUES ('{dname}', '{dcode}', '{dlocation}', '{description}');
    """)

    connection.commit()
    print("1 table created")


def add_employee_department(dcode, ssn):
    cursor.execute(f"""
        INSERT INTO employeeDepartment
        VALUES ('{dcode}', '{ssn}');
        """)

    connection.commit()
    print("1 table created")


def view_department():

    dcode = input("Enter department code: ")

    cursor.execute(f"""
        SELECT * FROM department WHERE dCode = '{dcode}'
    """)

    results = cursor.fetchall()

    print("===============================================================================")
    print("Dep. name     |\tDep. Code  |   \tDep. Location  |         \tDescription")
    print("===============================================================================")
    for result in results:
        print(f"{result[0]} | \t{result[1]}       |       \t{result[2]}      |    \t{result[3]}\n")


def view_employee():
    ssn = input("Enter employee's SSN: ")

    cursor.execute(f"""
        SELECT * FROM employee WHERE ssn = '{ssn}'
    """)

    results = cursor.fetchall()
    print("===========================================================================================")
    print("Name                 |   \tAge           |      \tSalary     |         \tSSN")
    print("===========================================================================================")
    for result in results:
        print(f"{result[0]} {result[1]}       |     \t{result[2]}            |     \t{result[3]}     |       {result[4]}\n")


def view_workers():
    dcode = input("Enter department code")

    cursor.execute(f"""
        SELECT fname, lname
        FROM employee, employeeDepartment
        WHERE dCode = '{dcode}' and employee.ssn = employeeDepartment.ssn;
    """)

    results = cursor.fetchall()

    print("===========================================================================================")
    print(f"WORKERS IN DEPARTMENT {dcode}")
    print("===========================================================================================")

    for result in results:
        print(f"{result[0]} {result[1]}")
        print("----------------------------------")

    print("===========================================================================================")

'''---------------Main----------------------'''

while done != 0:
    print("Welcome to employee management system")
    print("_____________________________________\n")
    print("\t1.) Add a new department")
    print("\t2.) Add a new employee")
    print("\t3.) View department information")
    print("\t4.) View employee information")
    print("\t5.) View all employees in department")
    print("\t0.) quit")

    number = input()

    if number == "1":
        add_department()

    if number == "2":
        add_employee()

    if number == "3":
        view_department()

    if number == "4":
        view_employee()

    if number == "5":
        view_workers()

    if number == "0":
        break


connection.close()

''' 
CREATE TABLES CODE

cursor.execute("PRAGMA foreign_keys = ON;")

connection.commit()

cursor.execute("""
    CREATE TABLE employee (
    fname text NOT NULL,
    lname text NOT NULL,
    age integer NOT NULL,
    salary integer NOT NULL,
    ssn text PRIMARY KEY
    );
""")

connection.commit()
print(" employee Committed")

cursor.execute("""
    CREATE TABLE department (
    dName text NOT NULL,
    dCode text PRIMARY KEY,
    dLocation text NOT NULL,
    description text NOT NULL
    );
""")

connection.commit()
print("department Committed")

cursor.execute("""
    CREATE TABLE employeeDepartment (
    dCode text NOT NULL,
    ssn text NOT NULL,
    foreign key (dCode) references department (dCode),
    foreign key (ssn) references employee (ssn)
    );

""")

connection.commit()

print(" employee department Committed")

'''
