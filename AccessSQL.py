import pandas as pd

customer_sales = pd.read_csv('DataGenTools/SalesTable.csv')

customers = customer_sales.groupby('customer_id')

for customer in customers:
    # do stuff
    pass