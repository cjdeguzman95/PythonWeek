import pyodbc

# these are the connecting credentials
server = "localhost,1433"
database = "Northwind"
username = "SA"
password = "Passw0rd2018"
docker_Northwind = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';'
                                  'UID='+username+';PWD='+ password)

# A cursor itself is a control structure that allows us to control and manage rows of data from a response
# A cursor is a container - it manages the rows fetched from DBMS - everything is controlled by the cursor
cursor = docker_Northwind.cursor()

cursor.execute("SELECT @@version;")
row = cursor.fetchone() # this retrieves just one record, fetchall retrieves all records
print("The row is", row)

cust_rows = cursor.execute("SELECT * FROM Customers;").fetchone()
print("Customer rows are", cust_rows)

# the following code lists the unit prices for ALL RECORDS
rows = cursor.execute("SELECT * FROM Products;").fetchall()
print("Unit price")
for record in rows:
    print(record.UnitPrice) # the variable after 'record' has to MATCH the variable name in the database

# the following code lists the surnames for ALL EMPLOYEES
rows = cursor.execute("SELECT LastName FROM Employees;").fetchall()
print("Employee Surnames")
for surname in rows:
    print(surname.LastName)

# the following code lists all the employees living in London or Seattle
rows = cursor.execute(
    "SELECT CONCAT_WS(' ', FirstName, LastName) AS Full_Name FROM Employees WHERE City IN ('London', 'Seattle');"
).fetchall()
print("Employees living in London or Seattle:")
for employee in rows:
    print(employee.Full_Name)
