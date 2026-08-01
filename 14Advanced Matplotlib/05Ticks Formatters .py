'''
Normally Matplotlib displays ticks like:
    1000, 2000, 3000, 4000

But in business dashboards we prefer:
    1K, 2K, 3K, 4K  Or ₹10K, ₹20K, ₹30K OR 25%, 50%, 75%

Tick formatters let us customize how axis values are displayed.

    
Ticks Formater -
        Matplotlib gives you fine control over how axis ticks (numbers along X and Y axes) are displayed.
        This is done using tick formatters from matplotlib.ticker.


🔹 Common Tick Formatters
    1. ScalarFormatter (default): Shows numbers in plain format (e.g., 1000 instead of 1e3).
   
        from matplotlib.ticker import ScalarFormatter

        ax.yaxis.set_major_formatter(ScalarFormatter())

    2. FormatStrFormatter: Use a Python format string (like %.2f for 2 decimal places).
        
        from matplotlib.ticker import FormatStrFormatter

        ax.xaxis.set_major_formatter(FormatStrFormatter("%.2f"))

    3. FuncFormatter: Define your own custom formatting function.
        
        from matplotlib.ticker import FuncFormatter

        def custom_format(x, pos):
            return f"{x} units"

        ax.yaxis.set_major_formatter(FuncFormatter(custom_format))

    4. LogFormatter: For logarithmic scales (plt.yscale("log")).
        
        from matplotlib.ticker import LogFormatter

        ax.yaxis.set_major_formatter(LogFormatter())

    5. PercentFormatter: Show ticks as percentages.

        from matplotlib.ticker import PercentFormatter
        ax.yaxis.set_major_formatter(PercentFormatter())

When to Use:
    Scientific plots → show values in scientific notation.
    Financial plots → format ticks as currency.
    Probability plots → show ticks as percentages.
    Custom dashboards → add units like "kg", "m", "₹", etc.

    
The FuncFormatter in Matplotlib is a flexible way to customize how tick labels are displayed on your axes. 
Instead of using a fixed format, you provide a function that takes the tick value and its position, 
and returns the string you want to show.

    ax.yaxis.set_major_formatter(
         FuncFormatter(lambda x, pos: f"{x/1000:.1f}K")
         )
    
    Understand function:
    parameters:
        x → the actual tick value (the number on the axis, e.g. 1000, 2000, etc.).
        pos → the position index of that tick (0 for the first tick, 1 for the second, and so on).
    Inside the f-string ( formatted string literal ):
        x/1000 → The tick value (x) is divided by 1000.
        :.1f → This is a format specifier:
                : → starts the format specification.
                .1f → means floating-point number with 1 decimal place.
        K → Just a literal character appended to the string.
    Together → 2000 becomes "2.0K".


    Some common used lambda functions in FuncFormatter:
    1. For Currency Formatting: lambda x, pos: f"₹{x:,.0f}"
    2. For Thousands (K): lambda val, pos: f"{val/1000:.1f}K"
    3. For Millions (M): lambda val, pos: f"{val/1_000_000:.1f}M"
    4. For Percent (%): lambda val, pos: f"{val:.0%}"     # here .0% means no decimal places and multiply val by 100 and add % sign
                        lambda val, pos: f"{val*100:.0f}%"
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

#Example 1: Currency Formatting

sales = [10000,20000,30000,45000]
months = ["Jan", "Feb", "Mar", "Apr"]
fig, ax = plt.subplots()

ax.plot(months,sales)


ax.yaxis.set_major_formatter(
    FuncFormatter(lambda x, pos: f"₹{x:,.0f}")    # here , add comma(,) in value and .0f mean no decimal places
    )
ax.set_title("Currency Formatting Example")

plt.show()


#Example 2: Thousands (K)
x = np.arange(0, 100, 10)
y = x**2

fig, ax = plt.subplots()
ax.plot(x, y)

ax.yaxis.set_major_formatter(
    FuncFormatter(lambda val, pos: f"{val/1000:.1f}K")
    )

plt.title("Tick Formatter: Thousands (K)")
plt.show()

