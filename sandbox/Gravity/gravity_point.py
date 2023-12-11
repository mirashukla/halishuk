import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Gravitational constant
G = 6.674 * 10**(-11)  # N*m^2/kg^2

# Mass of objects
mass_A = 500.0  # kg
mass_B = 100000000.0  # kg

# Initial conditions for object A
initial_x_A = 2.4 - 5.0     #np.random.uniform(0, 10)  # Random initial x-coordinate
initial_y_A = 0.0 -3  # Object A starts at the bottom of the screen
initial_vx_A = 0  # Initial velocity in the x direction
initial_vy_A = 0.5  # Initial velocity in the y direction

# Initial conditions for object B (at the center of the screen)
x_B = 0
y_B = 0

# Time parameters
total_time = 100.0  # Total simulation time
dt = 0.2  # Time step

# Create figure and axis
fig, ax = plt.subplots()

# Scatter plot for object B
scatter_B = ax.scatter(x_B, y_B, color='red', label='Object B', marker='o',s=30)

# Line plot for object A trajectory
scatter_A = ax.scatter(initial_x_A, initial_y_A, color='blue', label='Object A', marker='o', s=10)

# Set plot limits
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
ax.set_aspect('equal', 'box')  # Set aspect ratio to be equal

# Set plot labels and legend
plt.title('Object A influenced by Gravity of Object B Animation')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.legend()

# Animation update function
def update(frame):
    global initial_x_A, initial_y_A, initial_vx_A, initial_vy_A

    # Calculate distance between A and B
    dx = x_B - initial_x_A
    dy = y_B - initial_y_A
    r = np.sqrt(dx**2 + dy**2)

    # Calculate gravitational force components
    fx = G * (mass_A * mass_B) * dx / r**3
    fy = G * (mass_A * mass_B) * dy / r**3

    # Update velocities of A
    initial_vx_A += fx * dt
    initial_vy_A += fy * dt

    # Update the position of A
    initial_x_A += initial_vx_A * dt
    initial_y_A += initial_vy_A * dt

    # Update the trajectory of A
    scatter_A.set_offsets(np.array([[initial_x_A, initial_y_A]]))
    
    return scatter_A,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=int(total_time/dt)
                              , blit=True)

# Set plot labels and legend
plt.title('Object A influenced by Gravity of Object B Animation')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.legend()

# Show the animation
plt.show()
