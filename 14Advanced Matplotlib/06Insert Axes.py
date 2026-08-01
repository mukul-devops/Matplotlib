'''
Sometimes one region deserves a closer look.
Instead of Entire Graph


- Inset axes are smaller plots placed inside a main plot. They’re useful for zooming into a region of interest,
  showing a different scale, or adding a secondary visualization.

- Methods to Create Inset Axes:
    1. Using `inset_axes` from `mpl_toolkits.axes_grid1.inset_locator`:
        - This method allows you to specify the size and location of the inset axes relative to the parent axes.
        - Example:
            from mpl_toolkits.axes_grid1.inset_locator import inset_axes
            ax_inset = inset_axes(ax, width="30%", height="30%", loc="upper left")

    2. Using `add_axes`:
        - You can manually define the position and size of the inset axes using normalized coordinates.
        - Example:
            ax_inset = fig.add_axes([0.6, 0.6, 0.25, 0.25])  # [left, bottom, width, height]

            
Real-World Uses of inset_axes()
    1. Financial Data (Stock Prices)
    2. Scientific Experiments
    3. Medical imaging
    4. Satellite images
'''


import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Simulated stock price data
np.random.seed(42)
days = np.arange(1, 101)
price = np.cumsum(np.random.randn(100)) + 100  # random walk

fig, ax = plt.subplots(figsize=(8,5))
ax.plot(days, price, label="Stock Price")
ax.set_title("Stock Price Trend with Inset Zoom")
ax.set_xlabel("Days")
ax.set_ylabel("Price")
ax.legend()

# Create inset axes (30% width/height of parent)
ax_inset = inset_axes(ax, width="30%", height="30%", loc="upper left")

# Plot zoomed region (days 40–60)
ax_inset.plot(days, price, color="red")
ax_inset.set_xlim(40, 60)
ax_inset.set_ylim(min(price[39:60]), max(price[39:60]))    # min(price[39:60]) - min value of price from index 39 to 60 (days 40 to 60). This is python slicing.
ax_inset.set_title("Zoomed Volatility", fontsize=8)

plt.show()



import matplotlib.pyplot as plt
import numpy as np

# Simulated stock price data
np.random.seed(42)
days = np.arange(1, 101)
price = np.cumsum(np.random.randn(100)) + 100  # random walk

fig, ax = plt.subplots(figsize=(8,5))
ax.plot(days, price, label="Stock Price")
ax.set_title("Stock Price Trend with fig.add_axes()")
ax.set_xlabel("Days")
ax.set_ylabel("Price")
ax.legend()

# Add inset axes manually (coordinates: [left, bottom, width, height])
# Values are relative to the figure (0–1 range)
ax_inset = fig.add_axes([0.5, 0.55, 0.3, 0.3])  
ax_inset.plot(days, price, color="red")

# Zoom into days 40–60
ax_inset.set_xlim(40, 60)
ax_inset.set_ylim(min(price[39:60]), max(price[39:60]))
ax_inset.set_title("Zoomed Volatility", fontsize=8)

plt.show()
