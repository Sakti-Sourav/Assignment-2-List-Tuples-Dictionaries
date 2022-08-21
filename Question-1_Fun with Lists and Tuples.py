#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

tupList =[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

print("List of Tuple before sorting : " + str(tupList))

listLen = len(tupList); 
for i in range(0, listLen):
    for j in range(0, listLen - i - 1):
        if(tupList[j][-1] > tupList[j + 1][-1]):
            swap = tupList[j]
            tupList[j] = tupList[j + 1]
            tupList[j + 1] = swap

print("List of Tuple after sorting : " + str(tupList))

