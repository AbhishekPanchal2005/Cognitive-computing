#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

# Q1
arr = np.array([1, 2, 3, 4, 5])
print("Original Array:", arr)
print("Addition of 2:", arr + 2)
print("Multiplication by 3:", arr * 3)
print("Division by 2:", arr / 2)


# In[3]:


# Q2
# a)
arr = np.array([1, 2, 3, 6, 4, 5])
reversed_arr = arr[::-1]
print("Reversed Array:", reversed_arr)

# b)
x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
y = np.array([1, 1, 2, 3, 4, 2, 4, 3, 3, 3])

most_frequent_x = np.bincount(x).argmax()
most_frequent_y = np.bincount(y).argmax()
indices_x = np.where(x == most_frequent_x)[0]
indices_y = np.where(y == most_frequent_y)[0]

print("Most Frequent Value in x:", most_frequent_x, "at indices:", indices_x)
print("Most Frequent Value in y:", most_frequent_y, "at indices:", indices_y)


# In[4]:


# Q3
arr_2d = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("1st row, 2nd column:", arr_2d[0, 1])
print("3rd row, 1st column:", arr_2d[2, 0])


# In[13]:


# Q4
your_name_array = np.linspace(10, 100, 25)
print("Array:", your_name_array)
print("Dimensions:", your_name_array.shape)
print("Total Elements:", your_name_array.size)
print("Data Type:", your_name_array.dtype)
print("Total Bytes Consumed:", your_name_array.nbytes)
print("\n")

# Transpose using reshape
reshaped_array = your_name_array.reshape(5, 5)
print("Reshaped Array:\n", reshaped_array)
print("\n")
print("Transpose using .T:\n", reshaped_array.T)


# In[14]:


# Q5
ucs420_Abhishek = np.array([
    [10, 20, 30, 40], 
    [50, 60, 70, 80], 
    [90, 15, 20, 35]
])

print("Mean:", np.mean(ucs420_Abhishek))
print("Median:", np.median(ucs420_Abhishek))
print("Max:", np.max(ucs420_Abhishek))
print("Min:", np.min(ucs420_Abhishek))
print("Unique Elements:", np.unique(ucs420_Abhishek))
print("\n")

# Reshape to 4x3
reshaped_ucs420_Abhishek = ucs420_Abhishek.reshape(4, 3)
print("Reshaped to 4x3:\n", reshaped_ucs420_Abhishek)
print("\n")

# Resize to 2x3
resized_ucs420_Abhishek = np.resize(ucs420_Abhishek, (2, 3))
print("Resized to 2x3:\n", resized_ucs420_Abhishek)


# In[ ]:




