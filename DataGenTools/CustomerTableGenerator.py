import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(1234)

tax_rules = ['a','b','c','d','e']

num_customers = 1400
num_sales = rng.exponential(scale=2, size=num_customers).astype(np.int) + 1
sale_vals = np.abs(rng.normal(loc=50,scale=25,size=num_sales.sum()))

cust_tax = rng.choice(tax_rules, size=num_customers)
sales_tax = rng.choice(tax_rules, size=num_sales.sum())



rows_list = []
entry_num = 0
for i, val in enumerate(num_sales):
    for j in range(val):
        row_dict = {
            "customer_id":i,
            "price":sale_vals[entry_num],
            "customer_tax":cust_tax[i],
            "sale_tax":sales_tax[entry_num]
        }
        rows_list.append(row_dict)
        entry_num += 1

df = pd.DataFrame(rows_list)
df.to_csv("SalesTable.csv",index=False)

