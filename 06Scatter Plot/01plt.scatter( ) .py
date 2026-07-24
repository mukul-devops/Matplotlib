'''
- Scatter Plot:
     A scatter plot is used to visualize the relationship between two variables 
     by plotting points on a 2D plane.Each point represents one observation.
     It’s great for spotting patterns, correlations analysis, outliers detection, 
     Regression analysis, Clustering and Feature relationships.
     
     plt.scatter(x, y)
        x → Horizontal values
        y → Vertical values

     Unlike plt.plot(), scatter points are not connected by lines.

🔹 Customization Options:
     plt.scatter(x,y,
                 color='r',
                 marker='o',
                 s=20,
                 alpha=0.5,
                 edgecolor="y",
                 linewidth=1.5
                 )

     color → Point color ("red", "blue", hex codes like "#1f77b4").
     marker → Shape of points ("o", "s", "^", "*", "+").
     s → Size of points. It represents the marker area (in points²)
     alpha → Transparency (0 to 1).
     edgecolor - Set Border color of point
     linewidth - Thickness of point edges

'''

import matplotlib.pyplot as plt

hours = [2, 3, 4, 5, 6]
marks = [55, 60, 68, 75, 85]

# plt.scatter(hours, marks)
plt.scatter(hours, marks,
            color=['r','b','k','c','m'],
            marker='s',
            s=50,
            alpha=0.7,
            
            )



plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")


plt.show()