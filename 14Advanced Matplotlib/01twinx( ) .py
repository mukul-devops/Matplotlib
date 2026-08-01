'''
- plt.twinx() is used when you want to plot two different datasets that share the same x-axis
  but have different y-axes. It creates a second y-axis on the right side of the plot, 
  allowing you to compare variables with different scales in one figure.

- fig, ax1 = plt.subplots()

    ax2 = ax1.twinx()

    Now you have:
    Figure
    │
    ├── ax1 (Left Y-axis) 
    │           The first plot with its own x-axis and y-axis.
    └── ax2 (Right Y-axis) 
                Shares the same x-axis as ax1.
                Has its own independent y-axis on the right side.


'''

import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr"]

sales = [100,150,200,250]

profit = [10,12,15,18]

fig, ax1 = plt.subplots(figsize=(8,5))

# Left axis
ax1.plot(
    months,
    sales,
    color="blue",
    marker="o"
)

ax1.set_ylabel("Sales (₹)")

# Right axis
ax2 = ax1.twinx()

ax2.plot(
    months,
    profit,
    color="red",
    marker="s"
)

ax2.set_ylabel("Profit (%)")

#Customization of ticks
ax1.tick_params(axis="y", colors="blue")
ax2.tick_params(axis="y", colors="red")

plt.show()