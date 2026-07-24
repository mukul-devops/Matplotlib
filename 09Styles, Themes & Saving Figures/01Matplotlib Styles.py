'''
Matplotlib Styles: 

        Instead of manually changing colors every time, Matplotlib provides collection of predefined stylesheets 
        that instantly change the look and feel of your plots. Instantly changes the background, grid, and colors.

        You can apply them using: plt.style.use("style_name")

    Common Built-in Styles:
            default - Normal Matplotlib.
            ggplot - Good for data analysis.
            dark_background  - Perfect for presentations.
            fast - Optimized for plotting very large datasets.
            bmh - Clean statistical style.
            fivethirtyeight - Inspired by the FiveThirtyEight website.


    See All Available Styles: print(plt.style.available)
        This will show all styles you can use, including "seaborn-v0_8-darkgrid", "seaborn-v0_8-whitegrid", "seaborn-v0_8-poster", etc


    Custom Styles:
        You can also create your own .mplstyle file with custom settings (colors, fonts, linewidths) 
          load it: plt.style.use("my_custom_style.mplstyle")

          

Global Settings (rcParams):
     Matplotlib has a global configuration system called rcParams (runtime configuration parameters).
     These settings control the default appearance of all plots — things like font size, line width, colors, grid style, figure size, etc.
    
    rcParams is a dictionary-like object that stores global style settings.
    Changing a value in rcParams affects all subsequent plots until you reset or change it again.
    It’s useful for setting consistent styles across multiple plots (like a dashboard or report).

    # Change global settings
    plt.rcParams["figure.figsize"] = (10,6)
    plt.rcParams["font.size"] = 14
    plt.rcParams["axes.grid"] = True
    plt.rcParams["lines.linewidth"] = 2
    plt.rcParams["axes.titlesize"] = 16
    plt.rcParams["axes.facecolor"] = "whitesmoke"  # Background color

    Now every new figure uses these defaults.

    🔹 Commonly Used rcParams:
        Parameter	            Description	                        Example
        figure.figsize	        Default figure size	                (10,6)
        figure.dpi   	        Resolution	                        120
        font.size	            Default font size	                14
        lines.linewidth	        Line thickness                  	2.5
        lines.color	            Default line color              	"blue"
        axes.titlesize	        Title font size	                    16
        axes.labelsize	        Axis label size                 	14
        axes.grid	            Show grid by default	            True
        axes.facecolor	        Background color of plot	        "lightgray"
        xtick.color/ytick.color	Tick colors	                        "red"
        legend.loc	            Default legend position	            "upper right"


    🔹 Resetting to Defaults:
            plt.rcdefaults()   # Reset all rcParam

'''

import matplotlib.pyplot as plt

plt.style.use("ggplot")

plt.plot([1,2,3,4],[2,5,4,7])
plt.title("Sales", fontfamily="serif")
plt.show()

# print(plt.style.available)


#Check Styles:
# import matplotlib.pyplot as plt
# import numpy as np

# styles = ['Solarize_Light2', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'petroff10', 'petroff6', 'petroff8', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']

# x = np.linspace(0, 10, 100)
# y = np.sin(x)

# for style in styles:
#     plt.style.use(style)
#     plt.plot(x, y)
#     plt.title(f"Style: {style}")
#     plt.show()
