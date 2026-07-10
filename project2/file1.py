import pandas as pd
import os
data = {
    'Name':['Alic', 'Customer', 'Bob', ],
    'age':[23,34,24]
}


df = pd.DataFrame(data)

new_roc = {'Name':'GIFE', 'age':30}
df.loc[len(df.index)] = new_roc
new_roc = {'Name':'GIFE', 'age':30}
df.loc[len(df.index)] = new_roc




data_dir = 'data'
os.makedirs(data_dir, exist_ok =True)

file_path = os.path.join(data_dir, 'data.csv')

df.to_csv(file_path, index=False)

print(f"dataframe {file_path}")