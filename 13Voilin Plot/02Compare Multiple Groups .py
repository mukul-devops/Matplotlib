'''
Compare Multiple Groups 
    One of the biggest advantages.  
    Comparing distributions across categories.

'''

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

IT = np.random.normal(60000, 4000, 300)
HR = np.random.normal(45000, 3000, 300)
Sales = np.random.normal(52000, 5000, 300)

plt.violinplot([IT, HR, Sales],
                showmedians=True,
                vert=False
               )
plt.title("Department Salary Distribution")
plt.yticks([1,2,3], ["IT","HR","Sales"])

plt.show()

# Now you can compare three salary distributions side by side.