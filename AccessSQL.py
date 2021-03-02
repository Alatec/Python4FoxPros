import pandas as pd
import pyodbc

# May not be required for Windows, but had to install the correct odbc driver for linux
# https://docs.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server?view=sql-server-ver15

con_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=Desktop-1;DATABASE=RNU; UID=Andrew; PWD=Andrew;'
conn = pyodbc.connect(con_string)
query = """
  SELECT TOP 100 * FROM Customers;
"""
customers = pd.read_sql(query, conn)



# I don't know what you'd use this for, but here's a cool groupby example
customers_by_type = customers.groupby('CUSTOMERTYPE')

# Iterate over every customer. 'Customer' is just a table
for customer in customers:
    # do stuff
    pass