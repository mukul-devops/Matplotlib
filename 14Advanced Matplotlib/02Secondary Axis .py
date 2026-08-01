'''
- Secondary Axis
    Suppose we wants
    Left axis:Temperature (°C)
    Right axis:Temperature (°F)

    Both represent the same data. But different units.

- secondary_xaxis() method lets you add a second X-axis (on the top of the plot) 
  that is mathematically linked to the primary X-axis. It’s especially useful 
  when you want to show the same data in two different units or scales.

    ax.secondary_xaxis(location, functions=(forward_func, inverse_func))

    location → where to place the secondary axis ('top' or 'bottom') and ('left' or 'right' for y-axis)
    functions → a pair of functions:
        forward_func → converts values from the primary axis to the secondary axis.
        inverse_func → converts values back from the secondary axis to the primary axis.



'''
# Example of secondary_yaxis() with Celsius to Fahrenheit conversion
import matplotlib.pyplot as plt

temp = [34,36,39,35,30,40,45]
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

fig, ax = plt.subplots()

ax.plot(days,temp,marker='o',color='b')
ax.set_ylabel("Temperature (°C)")

def c_to_f(c):
    return c*9/5+32

def f_to_c(f):
    return (f-32)*5/9

secax = ax.secondary_yaxis(
    "right",
    functions=(c_to_f,f_to_c)
)

secax.set_ylabel("Temperature (°F)")

plt.show()


# Example of secondary_xaxis() with kilometers to miles conversion
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 100, 100)   # distance in km
y = x**0.5

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("Distance (km)")
ax.set_ylabel("Speed")

# Conversion functions
def km_to_miles(x): return x * 0.621371
def miles_to_km(x): return x / 0.621371

# Add secondary X-axis (miles)
secax = ax.secondary_xaxis('top', functions=(km_to_miles, miles_to_km))
secax.set_xlabel("Distance (miles)")

plt.title("Secondary X-axis Example (Km ↔ Miles)")
plt.show()



'''
             secondary_yaxis() vs twinx()
             
    twinx()	                        secondary_yaxis()
    Two different datasets      	Same dataset
    Different units or metrics  	Same quantity, different units
    Sales vs Profit             	Celsius vs Fahrenheit
    Revenue vs Visitors	            Kilometers vs Miles
'''