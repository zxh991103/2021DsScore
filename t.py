import pandas as pd
s1 = pd.read_excel(io="/home/ubuntu/ds/19aiex.xlsx", header=0,index_col='sid')
print(s1)