'''
- plt.grid() - The plt.grid() function is used to add or remove grid lines in your plot.
               Grid lines make it easier to read values by aligning data points with the axes.
                plt.grid(True) → Show grid
                plt.grid(False) → Hide grid

🔹 Customizing Grid

    plt.grid(True, 
            color='gray',      # Line color
            linestyle='--',    # Dashed style
            linewidth=0.7,     # Thickness
            alpha=0.7)         # Transparency

    color → sets grid line color
    linestyle → '-', '--', ':', '-.'
    linewidth → thickness of grid lines
    alpha → transparency (0 = invisible, 1 = solid)

'''
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
sales = [200, 250, 300, 280, 350]

plt.plot(days, sales)
# plt.grid()
plt.grid(
    color="gray",
    linestyle="--",
    linewidth=1,
    alpha=0.5
)

plt.show()