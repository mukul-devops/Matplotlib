import matplotlib.pyplot as plt

experience = [1,2,3,4,5,6,7,8]

non_tech_salary = [25000,30000,34000,
          42000,50000,
          62000,71000,82000]

tech_salary = [30000,35000,40000,
          49000,70000,
          82000,100000,140000]

plt.figure(figsize=(8,5))

plt.scatter(
    experience,
    non_tech_salary,
    color="royalblue",
    s=120,
    edgecolor="black",
    alpha=0.8,
    label='Non Tech Emplooye'
)
plt.scatter(
    experience,
    tech_salary,
    color="lightgreen",
    s=120,
    edgecolor="black",
    alpha=0.8,
    label='Tech Emplooye'
)

plt.title("Experience vs Salary")

plt.xlabel("Years of Experience")

plt.ylabel("Salary")

plt.grid(alpha=0.3)

plt.legend()

plt.show()