import pandas as pd
import pyodbc

# Can't verify but I assmue this works
# con_string = 'DRIVER={SQL Server};SERVER='+ <server> +';DATABASE=' + <database>
# cnxn = pyodbc.connect(con_string)
# query = """
#   SELECT <field1>, <field2>, <field3>
#   FROM result
# """
# result_port_map = pd.read_sql(query, cnxn)
# result_port_map.columns.tolist()

# For testing, I made some dummy data
customer_sales = pd.read_csv('DataGenTools/SalesTable.csv')

customers = customer_sales.groupby('customer_id')

# Iterate over every customer. 'Customer' is just a table
for customer in customers:
    # do stuff
    pass