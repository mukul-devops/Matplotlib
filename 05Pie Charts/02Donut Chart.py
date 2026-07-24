'''
- Donut Chart: A donut chart is simply a pie chart with a hole in the center. 
  It’s often used as a stylish alternative to a pie chart, 
  making the proportions easier to read and leaving space in the middle for labels or totals.

- Understanding wedgeprops:
    The wedgeprops parameter in plt.pie() lets you customize the appearance of the slices (wedges) in a pie chart.
    It takes a dictionary of properties that control the style of each wedge.

🔹 Common wedgeprops Options
    width → Controls thickness of wedges (used to make donut charts).
            1.0 → Full pie, 0.5 → Medium hole, 0.3 → Larger hole 
    edgecolor → Color of the border around slices.
    linewidth → Thickness of the border.
    linestyle → Style of the border ("-", "--", ":").
    facecolor → Fill color of wedges (usually set via colors instead).




'''
import matplotlib.pyplot as plt
# Data
sales = [35, 30, 20, 15]
companies = ["Samsung", "Apple", "Xiaomi", "Others"]

# Colors
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]
plt.figure(figsize=(7,7))

plt.pie(sales, 
        labels=companies, 
        autopct="%1.1f%%", 
        startangle=90, 
        colors=colors, 
        wedgeprops={"width":0.3, "edgecolor":'w', "linewidth":2}, 
        pctdistance=0.85
        )



# Add text in the center
plt.text(0, 0, "Total\n100%", ha="center", va="center", fontsize=14, fontweight="bold", color='c')

plt.title("Global Smartphone Market Share (Donut Chart)", fontsize=16, fontweight="bold", color="maroon")
plt.show()
