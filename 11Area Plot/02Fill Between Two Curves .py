'''
plt.fill_between(x, y1, y2=0, color='skyblue', alpha=0.4)

                    Key Parameters:
                    x → X-axis values.
                    y1 → First curve (upper or lower boundary).
                    y2 → Second curve (default = 0, meaning baseline at y=0).
                    color → Fill color.
                    alpha → Transparency (0 = fully transparent, 1 = opaque).
                    where → Boolean mask to fill only specific regions.
'''

import matplotlib.pyplot as plt
months = ['Jan','Feb','Mar','Apr','May']
sales = [20,25,35,30,40]
target = [18,22,28,32,35]

plt.plot(months, sales)
plt.plot(months, target)

plt.fill_between(
    months,
    sales,
    target,
    alpha=0.3,
)

plt.show()
