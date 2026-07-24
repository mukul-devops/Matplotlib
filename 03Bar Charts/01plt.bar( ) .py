'''
- A bar chart is used to represent categorical data with rectangular bars.
  The height (or length) of each bar corresponds to the value of the category.

- A bar chart compares values across different categories.
  Instead of reading numbers, a bar chart makes the comparison immediately obvious.
  plt.bar(x, height)
    x → Categories
    height → Values

🔹 Customization Options

    plt.bar(categories, values,
            color="skyblue",       # Bar color
            edgecolor="black",     # Border color
            linewidth=1.5,         # Border thickness
            alpha=0.8,             # Transparency
            width=0.6)             # Bar width

        color → fill color of bars, For Multiple colors pass list of colors like this ["red", "blue", "green", "orange"]
        edgecolor → border color
        linewidth → border thickness
        alpha → transparency (0–1)
        width → thickness of bars   (Default width is 0.8.)



    
'''
import matplotlib.pyplot as plt

products = ["Laptop", "Mobile", "Tablet", "Watch"]
sales = [120, 180, 90, 70]
# plt.bar(products, sales)
plt.bar(products, sales, width=0.6, color='purple', edgecolor='black', linewidth=1.5, alpha=0.4, label='label')
plt.title("Samsung Sales Chart")
plt.xlabel("Products")
plt.ylabel("Units Sold")
plt.legend()
plt.grid(axis="y")   #Only horizontal grid lines are shown.
plt.show()