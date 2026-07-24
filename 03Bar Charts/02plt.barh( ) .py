'''
- plt.barh() - Horizontal Bar Chart
    Useful for long category names.

🔹 Customization: Same as plt.bar()


- plt.grid(axis="x")   #Only vertical grid lines are shown.



'''

import matplotlib.pyplot as plt

products = ["Laptop", "Mobile", "Tablet", "Watch"]
sales = [120,180,90,70]

plt.barh(products, sales)
plt.title("Samsung Sales Chart")
plt.xlabel('Products')
plt.ylabel('Units Sold')
plt.grid(axis="x")   #Only vertical grid lines are shown.
plt.show()