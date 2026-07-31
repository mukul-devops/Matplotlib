'''
- A violin plot is a powerful visualization tool in statistics and data science.
  It combines the features of a box plot and a kernel density plot, giving you both summary statistics
  and the distribution shape of the data.

    plt.violinplot(data)
    
- It shows: Median, Quartiles (Q1 & Q3), Distribution shape, Spread, Peaks (multiple modes)
  Unlike a box plot, it also tells you where data values are concentrated.
  The wider the violin, the more data points are concentrated there.
  The narrower the violin, the fewer data points exist there.

- Components:
        Kernel Density Estimation (KDE)
            Smooth curve that estimates the probability distribution of the data.
            Wider sections = higher data density.
            Narrow sections = fewer data points.

        Box Plot Elements (inside the violin)
            Median line.
            Interquartile range (IQR).
            Sometimes whiskers and outliers.

        Symmetry
            The density curve is mirrored on both sides for visual clarity.

    Customization:
        plt.violinplot(
                       data,
                       showmedians=True,
                       showmeans=True
                       showextrema=False,
                       widths=0.3,
                       vert=False
                       )

            showmedians - This adds a median line. By default, Matplotlib doesn't always draw the median.
            showmeans - If True, shows the mean of each dataset. Useful when comparing average values.
            showextrema - This displays horizontal lines which shows minimum and maximum values. By defaults it is True.
            widths - Controls the width of each violin. Default: 0.5.
            vert - If True (default), violins are vertical.
                   If False, violins are horizontal. Useful for dashboards with long category labels



    Customize Colors:
    Matplotlib returns a dictionary of artists.

    parts = plt.violinplot(
        salary,
        showmedians=True
    )

    for body in parts["bodies"]:
        body.set_facecolor("skyblue")
        body.set_edgecolor("black")
        body.set_alpha(0.7)

    This is a common customization pattern.

                       
'''

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

salary = np.random.normal(50000, 5000, 300)

parts =  plt.violinplot(salary,
                        showmedians=True,
                        # facecolor='c',
                        widths=0.2
                        )


for body in parts["bodies"]:
    body.set_facecolor("skyblue")
    body.set_edgecolor("black")
    body.set_alpha(0.7)
#This is a common customization pattern.

plt.show()

# One violin is drawn for the salary distribution.