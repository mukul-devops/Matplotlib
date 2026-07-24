'''
- plt.xlim() and plt.ylim() function is used to set or get the limits of the X-axis and Y-axis in a plot.
  It controls the visible range of values along the horizontal and vertical axis.
  Useful for zooming in/out, focusing on a region, or reversing axis direction. 
 
  plt.xlim(0, 6)   # Set X-axis limit

'''

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 5, 10]

plt.plot(x, y, marker='o')

#Zoom into a region:
plt.xlim(2, 4)   # Zoom into values between 2 and 4
plt.ylim(4, 8)   # Zoom into values between 4 and 8

#Reverse axis direction:
plt.xlim(6, 0)   # Flips X-axis
plt.ylim(12, 0)  # Flips Y-axis

plt.show()
