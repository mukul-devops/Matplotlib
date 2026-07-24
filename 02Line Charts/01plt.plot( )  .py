'''
- matplotlib.pyplot.plot() is a fundamental function used to create 2D line and marker plots.
  It takes coordinates (usually x and y), connects the data points with lines by default.
        plt.plot(x, y)
        x → values for the horizontal (X) axis.
        y → values for the vertical (Y) axis.


- Color: Change Line color
  plt.plot(x, y, color="red")

    Available colors:               
                        
    "red"                       
    "blue"
    "green"
    "black"
    "yellow"
    "orange"
    "purple"
    "pink"
    "cyan"
    "magenta"
    "brown"

    By short code:
    'r' → red
    'g' → green
    'b' → blue
    'w' → white
    'k' → black
    'y' → yellow
    'c' → cyan
    'm' → magenta

    By Hex code:
    plt.plot(x, y, color="#FF5733")   # orange-red

    By RGB / RGBA Tuple:
    plt.plot(x, y, color=(0.1, 0.5, 0.8))        # RGB
    plt.plot(x, y, color=(0.1, 0.5, 0.8, 0.7))   # RGBA (with transparency)


- Line Width:
    plt.plot(x, y, linewidth=4)
    Default width is 1.5.


- Line Style:
    plt.plot(x, y,linestyle="--")

    Available styles: 

    "-"	  -  Solid
    "--"  -  Dashed
    ":"	  -  Dotted
    "-."  -	 Dash-dot     


- Markers: Markers highlight each data point.

    plt.plot(x, y, marker="o")
   
    Common Marker Styles:
    Marker	Shape
    "o"	Circle
    "s"	Square
    "^"	Triangle
    "v"	Down triangle
    "*"	Star
    "+"	Plus
    "x"	Cross
    "D"	Diamond
    "."	Point
    "p"	Pentagon


- Marker Size:
    plt.plot(x, y,
            marker="o",
            markersize=12)

    Default size is around 6.

    
- Marker Color:
    plt.plot(x, y,
            marker="o",
            markerfacecolor="red",
            markeredgecolor="black")

    Result:
    Red-filled circle
    Black border    

    
- Label: Name for dataset (used in legend)	
    plt.plot(x, y, label="Sales")   


- Alpha: Transparency (0 = invisible, 1 = solid)
    plt.plot(x, y, alpha=0.5)

    Controls opacity. Useful when plotting multiple lines.

'''

import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
price = [120, 123, 121, 130, 128]

plt.plot(days, price,
         color="g",
         linewidth=2,
         linestyle="--",
         marker="o",
         markersize=8,
         markerfacecolor="y",
         markeredgecolor="black",
         alpha=0.3,
         label="Stocks Price Per Day")

plt.show()