'''
- Stacked bar chart - 
    A stacked bar chart is used when you want to show multiple datasets stacked on top of each other for each category. 
    Instead of side-by-side (like grouped bars), the values are combined vertically (or horizontally), 
    making it easy to see total values and the contribution of each group.

'''

import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr"]

online = [30,40,35,50]
offline = [20,25,30,20]

plt.bar(months, online, label="Online")

plt.bar(months, offline, label="Offline",bottom=online)
#bottom=online
#The second bars start where the first bars end.

plt.legend()    
    
plt.show()