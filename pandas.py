#Author : Suman
#Date


import pandas as pd
import numpy as np

#-----------------------------------------------------------------
#df = pd.read_csv('/Users/sumangadhalapati/Downloads/mlb_players.csv', quoting=3)
#print(df.head(5))
#-----------------------------------------------------------------
"""
# Read a JSON file
df_json = pd.read_json('/Users/sumangadhalapati/Downloads/Movies100MB.json')
print(df_json)
"""
#-----------------------------------------------------------------
# Read a Parquet file
"""
df_parquet = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
df_parquet.to_parquet('df.parquet.gzip', compression='gzip')
df_parq= pd.read_parquet('df.parquet.gzip')
print(df_parq)

#df_parquet = pd.read_parquet('userdata1.parquet')
#print(df_parquet)
"""
#-----------------------------------------------------------------
"""
# Read an ORC file

First, you need to install the pyarrow library:
#pip install pyarrow

import pyarrow.orc as orc
# Read an ORC file
table = orc.read_table('your_file.orc')
df = table.to_pandas()
"""
#-----------------------------------------------------------------
"""
#First, you need to install the fastavro library:
pip install fastavro
# Read a Avro file
import fastavro
#-----------------------------------------------------------------
# Read an Avro file
with open('your_file.avro', 'rb') as avro_file:
    avro_reader = fastavro.reader(avro_file)
    records = [record for record in avro_reader]
    df = pd.DataFrame(records)
#-----------------------------------------------------------------
"""
# Combine two df's
df1 = pd.DataFrame({'a':[1,4,7], 'b':[2,5,8], 'c':[3,6,9]})
df2 = pd.DataFrame({'a':[11,14,17], 'b':[12,15,18], 'c':[13,16,19]})

merged_df = pd.concat([df1, df2], ignore_index=True)

print(df1['a'])
print(merged_df)
