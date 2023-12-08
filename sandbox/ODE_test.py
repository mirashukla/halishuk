import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the differential equations
def model(y, t):
    r, v = y
    drdt = v
    dvdt = 10 * 100000000 / r**2
    return [drdt, dvdt]

# Set initial conditions
r0 = 10
v0 = 1
y0 = [r0, v0]

# Set up time points for integration
t = np.linspace(0, 100, 100)

# Solve the system of differential equations
solution = odeint(model, y0, t)

# Extract the results
r_values, v_values = solution[:, 0], solution[:, 1]

# Plot the trajectory
plt.plot(t, r_values)
plt.xlabel('Time')
plt.ylabel('Distance from Center')
plt.title('Object Trajectory in a Gravitational Field')
plt.show()
