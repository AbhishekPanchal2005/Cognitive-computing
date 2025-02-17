#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt

M = float(input("Enter a value for M: "))
x = np.linspace(-10, 10, 400)

y1 = M * x ** 2
y2 = M * np.sin(x)

plt.figure(figsize=(10, 5))
plt.plot(x, y1, label='y = M * x^2', color='blue', linestyle='-')
plt.plot(x, y2, label='y = M * sin(x)', color='green', linestyle='--')

plt.title('Plot of the Functions')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()


# In[6]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Subject': ['Math', 'Science', 'English', 'History', 'Art'],
    'Scores': [88, 92, 85, 78, 90]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 5))
bar_plot = sns.barplot(x='Subject', y='Scores', data=df, palette='muted')

for index, row in df.iterrows():
    bar_plot.text(row.name, row.Scores, round(row.Scores, 2), color='black', ha="center")

plt.title('Scores by Subject')
plt.xlabel('Subject')
plt.ylabel('Scores')
plt.grid(True)
plt.show()


# In[9]:


import numpy as np
import matplotlib.pyplot as plt

roll_number = 102317167
np.random.seed(roll_number)
data = np.random.randn(50)


fig, axs = plt.subplots(2, 2, figsize=(10, 10))

axs[0, 0].plot(data.cumsum())
axs[0, 0].set_title('Cumulative Sum')
axs[0, 0].set_xlabel('Index')
axs[0, 0].set_ylabel('Cumulative Sum')
axs[0, 0].grid(True)

axs[0, 1].scatter(np.arange(50), data)
axs[0, 1].set_title('Scatter Plot with Random Noise')
axs[0, 1].set_xlabel('Index')
axs[0, 1].set_ylabel('Random Value')
axs[0, 1].grid(True)

axs[1, 0].axis('off')
axs[1, 1].axis('off')

plt.tight_layout()
plt.show()


# In[11]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\ASUS\Downloads\company_sales_data.csv")

plt.figure(figsize=(10, 5))
sns.lineplot(x='month_number', y='total_profit', data=data)
plt.title('Total Profit of All Months')
plt.xlabel('Month')
plt.ylabel('Total Profit')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
for column in data.columns[1:-1]: 
    sns.lineplot(x='month_number', y=column, data=data, label=column)
plt.title('Product Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()

data_without_month_number = data.drop(columns=['month_number'])
total_sales = data_without_month_number.sum()

plt.figure(figsize=(10, 5))
total_sales.plot(kind='bar', color=sns.color_palette('muted'))
plt.title('Total Sales of All Products')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()


# In[ ]:




