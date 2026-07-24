'''
Box Plot - A box plot (also called a whisker plot) is used to show the distribution of data.
           It highlights the median, quartiles, and potential outliers in a dataset.

           A histogram shows the distribution, but it doesn't clearly show:
           Minimum value, Q1 (25%), Median (50%), Q3 (75%), Maximum value, Outliers.


Understanding Quartiles:
        Consider the sorted data: 5 8 10 12 15 18 20 22 25
        There are 9 values.

        Median (Q2): The middle value is: 15

        Lower Half: 5 8 10 12
        Median of lower half:(8 + 10) / 2 = 9
        Q1 = 9

        Upper Half: 18 20 22 25
        Median:(20 + 22) / 2 = 21
        Q3 = 21


Every box plot is built using:
        Statistic	        Meaning
        Minimum	            Smallest value (excluding outliers)
        Q1	                25th percentile
        Median (Q2)	        50th percentile
        Q3	                75th percentile
        Maximum         	Largest value (excluding outliers)


What is IQR? (Interquartile Range)
        One of the most important interview questions.
        Formula:IQR = Q3 - Q1

        Example:
        Q1 = 20, Q3 = 40
        IQR = 20
        IQR measures the spread of the middle 50% of the data.

        
Detecting Outliers:
        Outlier limits:
        Lower Limit: Q1 - 1.5 × IQR
        Upper Limit: Q3 + 1.5 × IQR
        Any value outside these limits is considered an outlier.
        Ex - 40 + (1.5 × 20)
        = 70
        Any value greater than 70 is an outlier.

  
- plt.box(data)
    
        This shows:
        Box → Interquartile range (25th to 75th percentile).
        Line inside box → Median.
        Whiskers → Range of data (excluding outliers).
        Dots outside whiskers → Outliers.

🔹 Customization:
        plt.box(data,
                widths=0.4,
                orientation='vertical',
                showmeans=True,
                showfliers=False,
                notch=True,
                patch_artist=True,
                boxprops=dict(facecolor="#fbff00", color="black", linewidth=2),
                whiskerprops=dict(color="green", linewidth=2, linestyle="--"),
                )

       
        widths - Change Width of all Boxs
        orientation - plot boxs vertical or horizontal
        showmeans - Normally only the median is shown. This shows means also
        showfliers - Hide/Show Outliers
        notch - The notch gives a visual indication of the uncertainty around the median.
        patch_artist - patch_artist=True  , Allows the box to be filled with color.
        boxprops - Style of the box (color, fill, border thickness).
        whiskerprops → Style of whiskers (color, line style).
        capprops → Style of caps at whisker ends.
        medianprops → Style of median line (color, thickness).
        flierprops → Style of outliers (marker shape, size, color, transparency).
   
           
'''

import matplotlib.pyplot as plt

marks = [10,45,50,52,55,58,60,
         62,65,68,70,72,
         75,78,80,85,90,98,120,126]

plt.boxplot(marks,
             orientation='vertical',
             widths=0.4,
             showmeans=True,
             notch=True,
             patch_artist=True,   
             boxprops=dict(facecolor="#fbff00", color="black", linewidth=2),
             whiskerprops=dict(color="green", linewidth=2, linestyle="--"),
             capprops=dict(color="black", linewidth=2),
             medianprops=dict(color="red", linewidth=2),
             flierprops=dict(marker="*", markerfacecolor="orange", markersize=8, linestyle="none", alpha=0.7)
             )

plt.title("Student Marks Distribution")

plt.show()