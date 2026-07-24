'''
Multiple Line Charts: 
                Call plt.plot() Multiple Times
                Each call to plt.plot() adds another line to the same axes until you call plt.show().
                They’re perfect for trend comparison 
'''

import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May","Jun"]

iphone = [90,110,140,160,175,195]

samsung = [100,120,150,170,180,200]
plt.figure(figsize=(10,6), dpi=100, facecolor="lightyellow", edgecolor="blue", linewidth=2)

plt.plot(
    months,
    iphone,
    color="blue",
    marker="o",
    linewidth=2,
    label="iPhone",
    alpha=0.5
)

plt.plot(
    months,
    samsung,
    color="green",
    linestyle="--",
    marker="s",
    linewidth=2,
    label="Samsung",
    alpha=0.5
)

plt.title("Monthly Mobile Sales",
          fontsize=16,
          color="purple",
          fontweight="bold")

plt.xlabel("Month-->",fontsize='14', color='c',fontweight='bold')
plt.ylabel("Units Sold-->",fontsize='14', color='c',fontweight='bold')

plt.grid( color="gray",
          linestyle="--",
          linewidth=1,
          alpha=0.3)

plt.legend(loc="best", fontsize=12, title="Datasets", shadow=True, frameon=True)

plt.show()