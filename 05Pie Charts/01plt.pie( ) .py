'''
- plt.pie() - The plt.pie() function is used to create pie charts, which show data as slices of a circle.
              Each slice represents a proportion of the whole,
              making it ideal for percentage or share comparisons.

              A pie chart shows how each category contributes to the whole.

              Important: Pie charts work best with 3–6 categories.
              If you have many categories or need precise comparisons, a bar chart is usually a better choice.

            plt.pie(value,
                    labels=[labes_for_each_value])
                    
            value - value of categories
            labels - list of categories names 

🔹 Customization Options
- plt.pie(value,
          labels=[apple, mango, grapes, banana],
          autopct="%1.1f%%",
          startangle=90,
          color=['r','b','k','g'],
          explode=[0.1, 0, 0, 0],
          counterclock=False,
          labeldistance=1.2,
          pctdistance=0.7 
          ) 

🔹 Key Parameters
    labels → Names for each slice.(Category names)
    autopct → Format for percentage labels (e.g., "%.2f%%").
    startangle → Rotates the chart for better orientation. startangle=90 is often preferred because it starts from the top.
    colors → Custom colors for slices.
    explode → Pulls slices outward for emphasis. 
    counterclock → by default is True (slices are drawn counterclockwise.)
                   If set to False: counterclock=False → slices are drawn clockwise.   
    labeldistance → labeldistance controls how far the labels (the category names) are placed from the center of the pie.
                    Default: labeldistance=1.1 → labels are placed just outside the pie slices.
    pctdistance → Move percentage text from the center


(autopct) - Display Percentages 
    This is one of the most commonly used parameters.
    What does "%1.1f%%" mean?
        Part	Meaning
        %	    Format specifier
        1	    Minimum width
        .1	    One decimal place
        f	    Floating-point number
        %%	    Display a % sign

    autopct="%1.0f%%"   # 40%, 30%, 20%, 10%
    autopct="%1.2f%%"   # 40.00%, 30.00%, 20.00%, 10.00%
'''

import matplotlib.pyplot as plt

# Data
sales = [40, 25, 20, 15]
products = ["Smartphones", "Laptops", "Tablets", "Accessories"]

colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]
explode = [0.1, 0, 0, 0]   # Emphasize first slice

plt.figure(figsize=(7,7), dpi=120, facecolor="#F8F9FA", edgecolor="black", linewidth=2)

# Pie chart
# plt.pie(sales)  #This creates a pie chart but without labels, making it difficult to understand.
plt.pie(sales,
        labels=products, 
        labeldistance=1.2 ,
        autopct="%1.1f%%", 
        colors=colors, 
        explode=explode, 
        counterclock=False, 
        startangle=180 , 
        shadow=True,
        wedgeprops={"width":1, "edgecolor":'w', "linewidth":2},   # Slices customization
        textprops={                                               # Text customization
                   'fontsize': 14,
                   'color': 'k',
                   'fontweight': 'bold',
                   'fontfamily': 'serif'                    
                  }
        )

plt.title("Company Product Sales Distribution", fontsize=16,fontfamily='serif', fontweight="bold", color="maroon", pad=20)
plt.show()


