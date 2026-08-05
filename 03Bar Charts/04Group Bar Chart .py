'''
- A grouped bar chart (also called a clustered bar chart) -Compare multiple categories side by side.
  It is used when you want to compare multiple datasets side by side across the same categories.

  
'''


import matplotlib.pyplot as plt
import numpy as np

months = ["Jan","Feb","Mar","Apr"]

A = [20,25,30,28]
B = [18,22,28,35]

x = np.arange(len(months))
'''
Understanding np.arange
If there are 4 months: len(month) = 4
x = np.arange(0,4) 
x becomes: [0,1,2,3]

'''

width = 0.35

plt.bar( x - width/2, A,
        width=width,
        label="Product A")


plt.bar( x + width/2, B,
        width=width,
        label="Product B")
    
   
plt.xticks(x, months)

plt.legend()

plt.show()