#!/usr/bin/env python
# coding: utf-8

# # Week 1 Python and Data Engineering Assessment
# 
# ## Task 3: NumPy, Pandas and Matplotlib
# 
# ### Employee Data Analysis
# 
# This notebook contains employee data analysis, data cleaning, statistical summaries and visualizations.

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


employees = pd.read_csv("../data/employees.csv")

print("EMPLOYEE DATA")
display(employees)


print("\nDATASET INFORMATION")
employees.info()

print("\nSTATISTICAL SUMMARY")
display(employees.describe())


print("\nTOTAL EMPLOYEES:", len(employees))

print("\nHEADCOUNT BY DEPARTMENT")
print(employees["department"].value_counts())


# In[3]:


employees_dirty = employees.copy()

employees_dirty.loc[1, "salary"] = None
employees_dirty.loc[4, "salary"] = None

employees_dirty = pd.concat(
    [employees_dirty, employees_dirty.iloc[[0]]],
    ignore_index=True
)

median_salary = employees_dirty["salary"].median()

employees_dirty["salary"] = employees_dirty["salary"].fillna(median_salary)

employees_dirty = employees_dirty.drop_duplicates()

employees_dirty["salary"] = employees_dirty["salary"].astype(int)

display(employees_dirty)


# In[4]:


department_summary = employees_dirty.groupby("department").agg(
    headcount=("id", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max")
)

display(department_summary)


# In[5]:


departments = pd.read_csv("../Task3/departments.csv")

inner_join = pd.merge(
    employees_dirty,
    departments,
    on="department",
    how="inner"
)

display(inner_join)


# In[6]:


left_join = pd.merge(
    employees_dirty,
    departments,
    on="department",
    how="left"
)

display(left_join)


# In[7]:


outer_join = pd.merge(
    employees_dirty,
    departments,
    on="department",
    how="outer"
)

display(outer_join)


# In[8]:


get_ipython().run_line_magic('timeit', 'employees["salary"].mean()')


# In[ ]:




