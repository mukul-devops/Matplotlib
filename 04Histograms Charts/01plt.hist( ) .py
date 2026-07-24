'''
- Histogram Chart - 
    A histogram is a type of chart that shows the distribution of numerical data
    by grouping values into ranges (called bins) and plotting the frequency of values in each bin.
    It’s one of the most common ways to visualize how data is spread out.

- Key Features of Histograms
    X-axis (horizontal): Represents the bins (intervals of values).
    Y-axis (vertical): Represents the frequency (count of values in each bin).
    Bars: Each bar’s height shows how many data points fall into that bin. 
          The taller the bar, the more values fall into that interval.

    Unlike a bar chart:
    Bar Chart → compares categories (e.g., Laptop, Mobile, Tablet).
    Histogram → shows how continuous numerical values are distributed.
                Bars Touch each other (continuous intervals)
                Each bar represents a range, not a single value.

    plt.hist(data,
             bins= no_of_bins)
                
🔹 Customization Options:

    plt.hist(data,
             bins=5,
             color='c',
             edgecolor='b',
             linewidth=1.5,
             density=True,
             range=(40,100),
             cumulative=True,
             orientation="horizontal",
             align=''left',
             bottom=2,	
             rwidth=0.9,
             alpha=0.7,
             label='Exam Scores'
             )

🔹 Key Parameters :
    Data - The data you want to plot
    bins - Number of intervals or exact bin edges
    color - Set Bar color 
    edgecolor - Set Border color of bars
    linewidth - Thickness of bar edges
    density - Normalize histogram (probability density) , by default density=False
              density=True	, Heights show probability density instead of counts.
    range - Lower and upper range of bins. Values outside are ignored.
    comulative - It shows cumulative counts. Useful in statistics. By default comulative=false
    orientation - Horizontal or vertical. 	Default is vertical. orientation='horizontal' like h bar chart
    align -	Bin alignment	Options: 'left', 'mid', 'right'.
    bottom - Shift bars vertically.	bottom=2 , Moves bars upward by given value.
    rwidth	- Relative bar width.	1.0 = full bin width.
    alpha - Transparency (0 = invisible, 1 = solid)
    label - Name for dataset (used in legend)

'''

import matplotlib.pyplot as plt

marks = [45,55,60,62,65,68,70,72,
         75,78,80,82,85,88,90,92,99]

# plt.hist(marks, bins=5)
plt.hist(marks,
         bins=5, 
         color='skyblue', 
         edgecolor='k',
         alpha=0.6,
         linewidth=1.5,
         label='Exam Scores',
         
         )



plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.legend()

plt.show()