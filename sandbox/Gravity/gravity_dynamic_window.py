import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Gravitational constant
G = 6.674 * 10**(-11)  # N*m^2/kg^2

# Mass of objects
mass_A = 1.0  # kg
mass_B = 10000.0  # kg

# Initial conditions for object A
initial_x_A = np.random.uniform(0, 10)  # Random initial x-coordinate
initial_y_A = 0.0  # Object A starts at the bottom of the screen
initial_vx_A = 0.0  # Initial velocity in the x direction
initial_vy_A = 1.0  # Initial velocity in the y direction

# Initial conditions for object B (at the center of the screen)
x_B = 5.0
y_B = 5.0

# Time parameters
total_time = 10.0  # Total simulation time
dt = 0.1  # Time step

# Create figure and axis
fig, ax = plt.subplots()

# Scatter plot for object B
scatter_B = ax.scatter(x_B, y_B, color='red', label='Object B', marker='o')

# Line plot for object A trajectory
line_A, = ax.plot([], [], label='Object A')

# Set initial plot limits
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal', 'box')  # Set aspect ratio to be equal

# Set plot labels and legend
plt.title('Object A influenced by Gravity of Object B Animation')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.legend()

# Animation initialization function
def init():
    line_A.set_data([], [])
    return line_A,

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
    line_A.set_data(np.append(line_A.get_xdata(), initial_x_A),
                    np.append(line_A.get_ydata(), initial_y_A))

    # Adjust the plot limits to keep A in view
    ax.set_xlim(max(0, initial_x_A - 5), initial_x_A + 5)
    ax.set_ylim(max(0, initial_y_A - 5), initial_y_A + 5)

    return line_A,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=int(total_time/dt),
                              init_func=init, blit=True)

# Show the animation
plt.show()
