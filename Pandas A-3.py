#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data = {
    "Tid": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Refund": ["Yes", "No", "No", "Yes", "No", "No", "Yes", "No", "No", "No"],
    "Marital Status": ["Single", "Married", "Single", "Married", "Divorced", "Married", "Divorced", "Single", "Married", "Single"],
    "Taxable Income": ["125K", "100K", "70K", "120K", "95K", "60K", "220K", "85K", "75K", "90K"],
    "Cheat": ["No", "No", "No", "No", "Yes", "No", "No", "Yes", "No", "Yes"]
}

df = pd.DataFrame(data)

print(df)


# In[2]:


# Q2
rows_0_4_7_8 = df.loc[[0, 4, 7, 8]]
print("Rows 0, 4, 7, 8:\n", rows_0_4_7_8, "\n")

# Q3.1
rows_3_to_7 = df.iloc[3:8]
print("Rows 3 to 7:\n", rows_3_to_7, "\n")

# Q3.2
rows_4_to_8_columns_2_to_4 = df.iloc[4:9, 2:5]
print("Rows 4 to 8 with columns 2 to 4:\n", rows_4_to_8_columns_2_to_4, "\n")

# Q3.3
all_rows_columns_1_to_3 = df.iloc[:, 1:4]
print("All rows with columns 1 to 3:\n", all_rows_columns_1_to_3)


# In[10]:


# Q4
import pandas as pd

df = pd.read_csv(r"C:\Users\ASUS\Downloads\archive\Iris.csv")
print(df.head())


# In[11]:


# Q5
df = df.drop(index=4)
df = df.drop(df.columns[3], axis=1)

print(df.head(10))


# In[13]:


# Q6
import pandas as pd

# Create sample dataset
data = {'Employee_ID': [101, 102, 103, 104, 105],
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Edward'],
        'Department': ['HR', 'IT', 'IT', 'Marketing', 'Sales'],
        'Age': [29, 34, 41, 28, 38],
        'Salary': [50000, 70000, 65000, 55000, 60000],
        'Years_of_Experience': [4, 8, 10, 3, 12],
        'Joining_Date': ['2020-03-15', '2017-07-19', '2013-06-01', '2021-02-10', '2010-11-25'],
        'Gender': ['Female', 'Male', 'Male', 'Female', 'Male'],
        'Bonus': [5000, 7000, 6000, 4500, 5000],
        'Rating': [4.5, 4.0, 3.8, 4.7, 3.5]}

df = pd.DataFrame(data)
df.to_csv("employees.csv", index=False)

# a)
print("Shape of the DataFrame:", df.shape)

# b)
print("\nSummary of the DataFrame:")
print(df.info())

# c)
print("\nDescriptive Statistics:")
print(df.describe())

# d)
print("\nFirst 5 rows:")
print(df.head())
print("\nLast 3 rows:")
print(df.tail(3))

# e)
print("\nStatistics:")
print("Average Salary:", df["Salary"].mean())
print("Total Bonus Paid:", df["Bonus"].sum())
print("Youngest Employee's Age:", df["Age"].min())
print("Highest Performance Rating:", df["Rating"].max())

# f)
print("\nDataFrame sorted by Salary:")
print(df.sort_values(by="Salary", ascending=False))

# g)
def categorize_rating(rating):
    if rating >= 4.5:
        return "Excellent"
    elif rating >= 4.0:
        return "Good"
    else:
        return "Average"

df["Rating_Category"] = df["Rating"].apply(categorize_rating)

# h)
print("\nMissing Values:")
print(df.isnull().sum())

# i)
df = df.rename(columns={"Employee_ID": "ID"})

# j)
print("\nEmployees with more than 5 years of experience:")
print(df[df["Years_of_Experience"] > 5])

print("\nEmployees from IT department:")
print(df[df["Department"] == "IT"])

# k)
df["Tax"] = df["Salary"] * 0.1

# l)
df.to_csv("modified_employees.csv", index=False)


# In[ ]:




