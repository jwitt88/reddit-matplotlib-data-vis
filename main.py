import pandas as pd
from sys import argv

script, file_name = argv
df = pd.read_csv(file_name)

#output the first five rows of the gathered data
print(df.head())
