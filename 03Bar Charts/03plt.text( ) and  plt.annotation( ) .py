'''
Add Values on Top of Bars with plt.text():
- plt.text() - The plt.text() function lets you place custom text annotations anywhere on your plot. 
               It’s useful for highlighting specific points, adding notes, or labeling data.

               plt.text(x, y, s, fontsize=12, color="blue", ha="center", va="bottom")

               🔹 Parameters:
                    x, y → Coordinates where text appears
                    s → String (the text itself)
                    fontsize → Size of text
                    color → Text color
                    ha → Horizontal alignment ("left", "center", "right")
                    va → Vertical alignment ("top", "center", "bottom")


- plt.annotation() - The function plt.annotate() is used to add annotations (text + optional arrows) to a plot. 
                     It’s perfect for highlighting specific points, trends, or outliers in your visualization.

                   - plt.annotate(text, xy, xytext, arrowprops)

                    text → The annotation text you want to display.
                    xy → Coordinates of the point you want to annotate (target point).
                    xytext → Coordinates where the text should appear.
                    arrowprops → Dictionary to customize the arrow style (optional).

        🔹 Customization:
                plt.annotate(text,xy=(4,5),xytext=(6,7),
                             fontsize=12, 
                             color="darkred", 
                             fontweight="bold",
                             rotation=45
                             ha="center", va="bottom",
                             arrowprops=dict(arrowstyle="->", facecolor="black", edgecolor='green', shrink=0.05,
                                             width=2, headwidth=10, linestyle="--"),
                             bbox=dict(boxstyle="round,pad=0.3", fc="yellow", ec="black", alpha=0.7)
                            )

                    arrowprops → arrowstyle → Define Arrow style. "->" - Simple arrow, "-|>" - Filled arrow,
                                              "<->" - Double arrow, "fancy" - Fancy arrow, "simple" - Simple filled arrow
                                 facecolor → arrow color
                                 edgecolor → Boarder color of arrow
                                 shrink → shorten arrow length
                                 width → arrow line width
                                 headwidth → size of arrow head
                                 linestyle → "--", ":", etc. 

                    fontsize → size of text
                    color → text color
                    fontweight → "bold", "light", etc.
                    rotation → rotate text
                    ha → horizontal alignment ("left", "center", "right")
                    va → vertical alignment ("top", "center", "bottom")
                    bbox → Background box for text
                           boxstyle → "round", "square", "circle", "rarrow", etc.
                           fc → fill color of box
                           ec → edge color of box
                           alpha → transparency    



Each bar is a rectangle object:

    bar.get_x() → left edge of the bar.
    bar.get_width() → width of the bar.
    bar.get_height() → height (value) of the bar.


'''

import matplotlib.pyplot as plt

products = ["Laptop","Mobile","Tablet","Watch"]
sales = [120,180,90,70]

plt.figure(figsize=(10,6), dpi=100, facecolor="lightyellow", edgecolor="blue", linewidth=2)
bars = plt.bar(products, sales, width=0.5, color='purple', edgecolor='black', linewidth=1.5, alpha=0.4)
plt.title("Samsung Sales Chart Of A Day",
          fontsize=16,
          color="purple",
          fontweight="bold")

plt.xlabel('Products-->',fontsize='14', color='c',fontweight='bold')
plt.ylabel('Units Sold(in K)-->',fontsize='14', color='c',fontweight='bold')
plt.grid(axis="y")

#We are adding a text annotations(Data Point) at head of each bar  
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2, bar.get_height(),   # To place the text in the center and at head of bar
        str(bar.get_height())+("K"),
        color='b',
        ha="center",
        va="bottom"
    )

plt.annotate(
    "Peak",
    xy=('Mobile',190),
    xytext=('Tablet',200),
    color='purple',
    fontsize=14,
    ha="center", va="bottom",
    rotation=5,
    arrowprops=dict(
          facecolor="c",     # arrow color
          edgecolor='green', #Boarder color of arrow
          shrink=0.05,       # shrink arrow length
          width=5,           # arrow width
          headwidth=10,      # size of arrow head
          linestyle="--"     # dashed arrow 
        ),
    bbox=dict(boxstyle="round,pad=0.3", fc="yellow", ec="black", alpha=0.5)
    )

plt.ylim(0,230)

plt.show()