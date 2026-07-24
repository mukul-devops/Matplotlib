import matplotlib.pyplot as plt
#matplotlib is the library.
#pyplot is the plotting module.
#plt is the common alias.

x = ['Mon','Tue','Wed','Thur','Fri','Sat','Sun']
y = [10, 20, 15, 30, 14, 50, 57]


#Understanding plt.plot()
plt.plot(x, y)
#x → values for the horizontal (X) axis.
#y → values for the vertical (Y) axis.
#Matplotlib draws a line joining each (x, y) pair.

plt.title('Bakery Sale Of This Week')
plt.xlabel('Day')
plt.ylabel('Sale per day')

plt.show()
#This tells Matplotlib to display the figure.


