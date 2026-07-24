'''

plt.boxplot(
            [math, science, english],
            tick_labels=["Math","Science","English"],
            
            )

        data - data is also list of data to plots multiple boxs like ["Math","Science","English"]
        tick_labels - Give names for each boxs(data).  ### If tick_labels not work them replace by labels

'''

import matplotlib.pyplot as plt

math = [25,65,70,72,75,80,85,95]
science = [28,51,60,65,68,72,78,81,84]
english = [39,50,58,62,67,70,75,78,80]

# Create figure
plt.figure(figsize=(9,6), dpi=120, facecolor="whitesmoke")

plt.boxplot(
            [math, science, english],
            tick_labels=["Math","Science","English"],
            # widths=0.7,
            showmeans=True,
            patch_artist=True,   # Fill boxes with color
            boxprops=dict(facecolor="#4C72B0", color="black", linewidth=2),
            whiskerprops=dict(color="#55A868", linewidth=2, linestyle="--"),
            capprops=dict(color="black", linewidth=2),
            medianprops=dict(color="#C44E52", linewidth=2),
            flierprops=dict(marker="o", markerfacecolor="#8172B3", markersize=8, linestyle="none", alpha=0.7)
            )
            
# Title and labels
plt.title("Distribution of Marks Across Subjects", fontsize=16, fontweight="bold", color="maroon")
plt.ylabel("Marks", fontsize=13, color="darkblue")
plt.xlabel("Subjects", fontsize=13, color="darkblue")

# Grid for readability
plt.grid(axis="y", linestyle="--", alpha=0.6) 

plt.show()

#Now you can compare: Spread, Median, Outliers
#for all three subjects.





