'''
- plt.legend() - The plt.legend() function adds a legend box to your plot,
                 explaining what each line, marker, or dataset represents. 
                 It’s essential when you have multiple plots in the same figure.
                 Legends identify multiple lines.
                 Without labels, the legend will be empty.

🔹 Customizing Legends

    plt.legend(loc="upper left", fontsize=12, title="Datasets", shadow=True, frameon=True)

    loc → Position ("upper left", "lower right", "center", "best")
    fontsize → Adjust text size
    title → Add a title above legend entries
    shadow → Adds a shadow effect
    frameon → Show/hide legend box border



'''
import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sales = [20,30,40,35,50]

plt.plot(days, sales, label="Sales", marker='o',linestyle='--')

# plt.legend()
plt.legend(loc="best", fontsize=12, title="Datasets", shadow=True, frameon=True)

plt.show()