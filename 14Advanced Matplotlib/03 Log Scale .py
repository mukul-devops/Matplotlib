'''
- Matplotlib allows you to plot data on a logarithmic scale instead of a linear scale. 
    plt.yscale("log")
    ax.set_yscale("log")  #Apply log scale to Y-axis

    When Is Log Scale Used?
    Population growth
    Virus spread
    Stock market
    Scientific data
    Neural network loss
    Database size
    Website users

    Whenever numbers vary by orders of magnitude, consider a log scale.

'''

import matplotlib.pyplot as plt

days = [1,2,3,4,5,6]
users = [100,300,900,2700,8100,24300]

fig, ax = plt.subplots(figsize=(8,5))

ax.plot(
    days,
    users,
    marker="o"
)

ax.set_yscale("log")
ax.set_title("User Growth (Log Scale)")
ax.set_xlabel("Day")
ax.set_ylabel("Users")
ax.grid(alpha=0.3)

plt.show()

