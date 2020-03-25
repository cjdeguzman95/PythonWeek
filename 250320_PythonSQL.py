import pyodbc

# these are the connecting credentials
server = "localhost,1433"
database = "Northwind"
username = "SA"
password = "Passw0rd2018"
docker_Northwind = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';'
                                  'UID='+username+';PWD='+ password)

# A cursor itself is a control structure that allows us to control and manage rows of data from a response
