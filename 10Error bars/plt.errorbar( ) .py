'''
Now we're entering scientific visualization, where Matplotlib is widely used in Machine Learning, Research,
Data Science, Finance, and A/B Testing.
This topic is asked less often than scatter plots or histograms, but it is extremely valuable 
when you need to communicate uncertainty in data.

Error Bars - 
    The function plt.errorbar() is used to plot data points with error bars — vertical, horizontal, or both
    — to show uncertainty, variability, or measurement error.

    plt.errorbar(x, y, yerr=None, xerr=None, fmt='', ecolor=None, capsize=None, elinewidth=None, elinestyle='-.')

        Key Parameters:
        x, y → Data points.
        yerr → Vertical error. yerr shows uncertainty in the y-values.   Ex - yerr= [2,3,2,1.2,0.8]
        xerr → Horizontal error. xerr shows uncertainty in the x-values. Ex - xerr= [3,4,2,5,1.5]
        fmt → Format string for markers/lines ('--s').  
        ecolor → Color of error bars.  
        capsize → Size of the caps at the ends of error bars.
        elinewidth → Thickness of error bar lines.
        elinestyle → error line style.
        alpha → Transparency.

   
'''

import matplotlib.pyplot as plt

days = ["Mon","Tue","Wed","Thu","Fri"]
temperature = [30,32,31,35,34]

y_error = [1,2,1.5,2,1]

fig, ax = plt.subplots(figsize=(8,5))

ax.errorbar(days, temperature,
            yerr=y_error,
            # marker="o",
            # linestyle="-",
            fmt='--s',          # Customize both line and marker
            linewidth=2,
            ecolor="red",
            capsize=6,
            capthick=2,
            )
   

ax.set_title("Weekly Temperature")
ax.set_xlabel("Day")
ax.set_ylabel("Temperature (°C)")
ax.grid(alpha=0.3)

plt.show()



