'''
- plt.barh() - Horizontal Bar Chart
    Useful for long category names.

🔹 Customization: Same as plt.bar(), except width for bar width


- plt.grid(axis="x")   #Only vertical grid lines are shown.



'''

import matplotlib.pyplot as plt

products = ["Laptop", "Mobile", "Tablet", "Watch"]
sales = [120,180,90,70]

plt.figure(
    figsize=(8,6),
    dpi=150,
    facecolor="#F8F9FA",
    edgecolor="black",
    linewidth=2,
    constrained_layout=True
)

bars = plt.barh(products, sales,
          color="skyblue",       # Bar color
          edgecolor="black",     # Border color
          linewidth=1.5,         # Border thickness
          alpha=0.8,             # Transparency
          ) 

#Adding a text on head of bars
plt.bar_label(                                         
    bars,
    fmt="%dk",
    padding=2,
    fontsize=10,
    fontweight="normal",
    color='darkblue'
)
            
plt.title("Samsung Sales Chart",
          fontsize=18,
          fontweight='bold',
          color='darkblue',
          pad=20,
          fontfamily='serif')

plt.xlabel('Units Sold (in K)',
            fontsize=14,
            fontweight='bold',
            color='darkred',
            fontfamily='sans-serif')

plt.ylabel('Products',
            fontsize=14,
            fontweight='bold',
            color='darkred',
            fontfamily='sans-serif')

plt.yticks(rotation=45)  # To ratate y ticks
plt.grid(axis="x",alpha=0.3)   #Only vertical grid lines are shown.

plt.show()