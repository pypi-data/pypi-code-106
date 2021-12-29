#!/usr/bin/env python
# coding: utf-8

# In[2]:
import pkgutil


def func():
    text = pkgutil.get_data(__name__, "example.txt").decode()
    print("Output of the function is : " + text)


# In[ ]:




