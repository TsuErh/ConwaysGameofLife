#!/usr/bin/env python
# coding: utf-8

# # GameofLife

# #### Tsu Erh Lin
# ###### Mar 4, 2021

# In[1]:


import numpy as np


# In[2]:


def conway(s,p):
    'Return a board of s*s matrix'
    
    if p == 0:                                                          # If the given p is 0, then the board will be a 0 matrix
        board = np.zeros(s*s).reshape(s, s)
    elif p == 1:                                                        # If the given p is 1, then the board will be a 1 matrix
        board = np.ones(s*s).reshape(s, s)
    else:                                                               # The matrix will be created randomly by the probabilty p in 1 and 0
        board = np.where(p > np.random.rand(s*s), 1, 0).reshape(s, s)
    return board


# In[3]:


def advance(b, t):
    'The function that represent the game of life on the board'

    count = 0                                            # First assign 0 to count
    while count < t:                                     # If the count is smaller than t, then the loop will continue
        for i in range(len(b)):                          # For index i and j
            for j in range(len(b)):
                if (i == len(b)-1 and j < len(b)-1):     # If index i is equal to the lenth of matrix
                    neighbor = (b[i-1, j-1], b[i-1, j],  # Set the neighbor of b[i,j]
                                b[i-1, j+1], b[i, j-1], 
                                b[i, j+1], b[0, j-1], 
                                b[0, j], b[0, j+1])
                elif (i < len(b)-1 and j == len(b)-1):   # If the j is equal to the lenth of matrix
                    neighbor = (b[i-1, j-1], b[i-1, j],  # Set the neighbor of b[i,j]
                                b[i-1, 0], b[i, j-1], 
                                b[i, 0], b[i+1, j-1], 
                                b[i+1, j], b[i+1, 0]) 
                elif (i == len(b)-1 and j == len(b)-1):  # If both i and j are equal to the lenth of matrix
                    neighbor = (b[i-1, j-1], b[i-1, j],  # Set the neighbor of b[i,j]
                                b[i-1, 0], b[i, j-1], 
                                b[i, 0], b[0, j-1], 
                                b[0, j], b[0, 0])
                else:                                    # If both i and j are smaller than the lenth of matrix
                    neighbor = (b[i-1, j-1], b[i-1, j],  # Set the neighbor of b[i,j]
                                b[i-1, j+1], b[i, j-1], 
                                b[i, j+1], b[i+1, j-1], 
                                b[i+1, j], b[i+1, j+1])
                    
                    if b[i, j] == 1:                     # For b[i,j] which are 1/live
                        if neighbor.count(1) < 2:        # If it has less than 2 live neighbors, let b[i,j] = 0 (die)
                            b[i, j] = 0            
                        elif neighbor.count(1) > 3:      # If it has more than 3 live neighbors, let b[i,j] = 0 (die)
                            b[i, j] = 0
                        else:                            # Or b[i,j] lives on to the next generation
                            continue
                    else:                                # For b[i,j] which are 0/die
                        if neighbor.count(1) > 3:        # If it has more than 3 live nighbors, let b[i,j] = 1 (live)
                            b[i, j] = 1
                        else:
                            continue
            count += 1
                    
            return b

        


# In[4]:


b = conway(4, .5)
b


# In[5]:


advance(b, 10)


# In[ ]:




