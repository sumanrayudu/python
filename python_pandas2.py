#Author: Suman
#Date

import numpy as np
import pandas as pd
"""
Create Dataframe
dataFrame 
# from_records
# from_dict
"""
print("-------------------------------------------------------------")
data_list = [[1,'parvati',1,50000],
             [2,'durga',2,510000],
             [3,'ram',2,5110000],
             [4,'lakshman',1,250000],
             [5,'seeta',3,150000],
             [6,'shiva',4,350000],
             [7,'vishnu',5,1150000],
             [8,'hanuman',5,950000],
             [9,'laxmi',6,850000],
             [10,'saraswati',4,450000],
             [None,'saibaba',None,450000]            
             ]
df_emp = pd.DataFrame(data_list,columns=['emp_id','emp_name','dept_no','salary'])

print("-------------------------------------------------------------")
print(df_emp.groupby(['dept_no']).sum())
print(df_emp.groupby(['dept_no','emp_id'],dropna=False).sum())

print("-------------------------------------------------------------")
print(df_emp.info(verbose=True))
print("df shape", df_emp.shape)
print("df size",df_emp.size)

print("-------------------------------------------------------------")
dept_dict = {'dept_no':[1,2,3,4,5,6],
             'dept_name':['hr','it','sales','finance','marketing',None]
            }
df_dept = pd.DataFrame(dept_dict, index = None)
#print(df_dept)
df_dept['dept_rank'] = df_dept['dept_no'].max()

print(df_dept)
print("df dropped nulls", df_dept.dropna(subset=['dept_name']))
print(df_dept.dropna(subset=['dept_name']))
print(df_dept.notna())
print(df_dept.fillna('No department'))
print("-------------------------------------------------------------")
"""
###
print("-------------------------------------------------------------")
Merge :
    - left_on
    - right_on
    - how = 'inner','left','right','cross'
    - suffixes 
    Ex : 
Concat :
    - join = inner","left","right"
    - pd.concat([df1, df3], join="inner") returns only matched 
    - merged_df = pd.concat([df1, df2], ignore_index=True)
Join :
    - df.join(other.set_index('key'), on='key')

combine
    - df2.combine(df1, take_smaller, overwrite=False)
print("-------------------------------------------------------------")
loc
    - 
iloc
    -
agg() or aggregrate()
    - df_emp.agg(['sum', 'min'])
groupby
    - df_emp.groupby(['dept_no'],dropna=False).min()
    - df_emp.groupby(['dept_no','emp_id'],dropna=False).sum()
dropna()
    - df_dept.dropna(subset=['dept_name'])
fillna()
    - df_dept.fillna('No department'))
drop_duplicates
    - df.drop_duplicates()
    - df.drop_duplicates(subset=['brand', 'style'], keep='last')

value_counts
    - df.value_counts(dropna=False)
print("-------------------------------------------------------------")      
"""


print(df_emp.merge(df_dept, how= 'inner', on='dept_no'))
#print(df_emp.combine(df_dept,))
print(df_emp.join(df_dept.set_index('dept_no'), on='dept_no', validate='m:1'))
print("concated ",pd.concat([df_emp, df_dept], join="inner"))
print("-------------------------------------------------------------")
string_data = 'this is python'
words = string_data.split(' ')
print(words)
df_string = pd.DataFrame(words,columns=['word'])
print(df_string)
print("-------------------------------------------------------------")
