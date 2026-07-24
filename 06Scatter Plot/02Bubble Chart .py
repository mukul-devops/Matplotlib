'''
- Bubble Chart :
    A bubble chart is a scatter plot where marker size represents a third variable.

'''

import matplotlib.pyplot as plt

hours = [2,3,4,5,6]
marks = [55,60,68,75,85]
attendance = [50,80,120,160,220]

plt.scatter(
    hours,
    marks,
    s=attendance,
    color='r',
    label='size of bubbles represent attandance'
)
#Larger attendance values produce larger bubbles.

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.legend()
plt.show()