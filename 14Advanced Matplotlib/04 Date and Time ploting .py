'''
Date & Time Plotting 
    Almost every real dataset contains dates.
    Examples: Stock prices, Weather, Website traffic, Sales, Sensor data, IoT, Automatic Date Formatting

    Instead of this,
    dates = [
        "2026-01-01",
        "2026-01-02",
        "2026-01-03",
        "2026-01-04"
    ]
    This works, but professionals usually use actual date objects.


    Use datetime:
    from datetime import datetime
    dates = [
        datetime(2026,1,1),
        datetime(2026,1,2),
        datetime(2026,1,3),
        datetime(2026,1,4)
    ]

    Now Matplotlib understands they are dates.


fig.autofmt_xdate()
    This automatically rotates and spaces date labels.
    Professionals use this constantly.


'''

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6,4))

from datetime import datetime

dates = [
    datetime(2026,1,1),
    datetime(2026,1,2),
    datetime(2026,1,3),
    datetime(2026,1,4)
]

price = [295,594,850,250]

ax.plot(dates,price,color='c', marker='s', mfc='r', mec='k')

ax.set_title('stock prices')
ax.set_xlabel('date')
ax.set_ylabel('prices')
ax.set_xticks(dates)
# ax.tick_params(
#     axis="x",
#     rotation=45
# )

fig.autofmt_xdate()

plt.show()


