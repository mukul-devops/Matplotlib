'''
Data Point - A data point is a single observation or value in your dataset. like (3, 15)
             It usually consists of an x-value (horizontal axis) and a y-value (vertical axis).
             Together, multiple data points form a dataset visualization (line, bar, scatter, etc.).
             
X-axis/Y-axis - X-axis (Horizontal Axis)
                Runs left to right across the plot.
                Represents the independent variable (the input or category).

                Y-axis (Vertical Axis)
                Runs bottom to top on the plot.
                Represents the dependent variable (the output or measured value).


How Matplotlib Works Internally
Python Data
      │
      ▼
Matplotlib
      │
      ▼
Figure
      │
      ▼
Axes
      │
      ▼
Plot
      │
      ▼
Display   


Figure   - The entire canvas or window.

Axes     - The area where data is plotted.

Plot     - The visual representation (line, bar, scatter, etc.).

Line style - Controls how the line connecting data points looks. 
             You can choose solid('-'), dashed('--'), dotted(':'),Dash-dot line('-.'), 
             or custom styles to make plots clearer and more visually appealing.

Marker   - A symbol used to represent individual data points in a plot.
           Common markers: "o" (circle), "s" (square), "^" (triangle), "*" (star).

Color - You can apply colors to lines, markers, bars, text, and backgrounds.
        Color is used to make plots visually distinct and easier to interpret. 

Title - A title is the heading displayed at the top of your plot.
        It describes what the visualization is about,
        making it easier for viewers to understand the context of the data.

Label - A Text that explain axes and data
        A label is the descriptive text you assign to elements in your plot, such as axes or data series.

Legend - A legend is the box that explains what different lines, colors, or markers in your plot represent.
        It’s like a key on a map—it helps the viewer understand which dataset corresponds to which visual element.
        Purpose: Distinguish multiple plots in the same figure.

Grid - A grid is a set of horizontal and vertical lines drawn across the plot area. 
       It helps you read values more easily by aligning data points with the axes.

DPI (Dots Per Inch) - It refers to the resolution of your figure. 
                      It controls how sharp or detailed your plot looks when displayed or saved.
                      Number of pixels per inch in the figure.
                      Higher DPI → Sharper image (but larger file size).
                      Lower DPI → Blurry image (but smaller file size).



'''