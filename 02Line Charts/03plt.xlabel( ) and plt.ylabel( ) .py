'''
- plt.xlabel() and plt.ylabel() :
    These two functions are used to label the axes of your plot,
    making it clear what the X-axis and Y-axis values represent.

🔹 Customization Options
    You can style the labels just like titles:

    plt.xlabel("Time (s)", fontsize=14, fontfamily="serif", color="blue", fontweight="bold", labelpad=10)
    plt.ylabel("Distance (m)", fontsize=14, fontfamily="serif", color="green", fontweight="bold", labelpad=10)
     
    fontsize → Size of text
    fontfamily → Change text style. Common families: "serif", "sans-serif", "monospace"
    color → Text color
    fontweight → "bold", "normal", "light"
    labelpad → Extra spacing between label and axis


'''
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
sales = [200, 250, 300, 280, 350]

plt.plot(days, sales)

plt.xlabel("Days-->", fontsize='14',fontfamily="serif", color='b',fontweight='bold', labelpad=10)
plt.ylabel("Sales-->", fontsize='14',fontfamily="sans-serif", color='b',fontweight='bold', labelpad=10)

plt.show()