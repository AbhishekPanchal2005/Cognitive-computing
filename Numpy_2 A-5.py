#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

# Q1
gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')

sum_all = np.sum(gfg)
sum_rowwise = np.sum(gfg, axis=1)
sum_colwise = np.sum(gfg, axis=0)

print("Sum of all elements:", sum_all)
print("Row-wise sum:", sum_rowwise)
print("Column-wise sum:", sum_colwise)


# In[5]:


# Q2
array = np.array([10, 52, 62, 16, 16, 54, 453])

sorted_array = np.sort(array)
sorted_indices = np.argsort(array)
smallest_4 = np.sort(array)[:4]
largest_5 = np.sort(array)[-5:]

print("Sorted array:", sorted_array)
print("Indices of sorted array:", sorted_indices)
print("4 smallest elements:", smallest_4)
print("5 largest elements:", largest_5)

array_2 = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])
integers_only = array_2[np.floor(array_2) == array_2]
floats_only = array_2[np.floor(array_2) != array_2]

print("Integer elements only:", integers_only)
print("Float elements only:", floats_only)


# In[6]:


# Q3
X = ord('A') + ord('P')
sales = np.array([X, X+50, X+100, X+150, X+200])

tax_rate = ((X % 5) + 5) / 100
sales_after_tax = sales * (1 - tax_rate)

sales_discounted = np.where(sales < X+100, sales * 0.95, sales * 0.90)

sales_matrix = np.vstack([sales] * 3)
sales_matrix = sales_matrix * (1.02 ** np.arange(3).reshape(-1, 1))

print("Sales dataset:", sales)
print("Sales after tax:", sales_after_tax)
print("Sales after discount:", sales_discounted)
print("Sales matrix for 3 weeks:", sales_matrix)


# In[13]:


# Q4

import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

y1 = x**2
y2 = np.sin(x)
y3 = np.exp(x)
y4 = np.log(np.abs(x) + 1)

fig, axs = plt.subplots(2, 2, figsize=(10, 10))

axs[0, 0].plot(x, y1)
axs[0, 0].set_title('Y = x^2')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('y')
axs[0, 0].grid(True)

axs[0, 1].plot(x, y2)
axs[0, 1].set_title('Y = sin(x)')
axs[0, 1].set_xlabel('x')
axs[0, 1].set_ylabel('y')
axs[0, 1].grid(True)

axs[1, 0].plot(x, y3)
axs[1, 0].set_title('Y = exp(x)')
axs[1, 0].set_xlabel('x')
axs[1, 0].set_ylabel('y')
axs[1, 0].grid(True)

axs[1, 1].plot(x, y4)
axs[1, 1].set_title('Y = log(|x| + 1)')
axs[1, 1].set_xlabel('x')
axs[1, 1].set_ylabel('y')
axs[1, 1].grid(True)

plt.tight_layout()
plt.show()


# In[ ]:




