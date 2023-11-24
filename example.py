import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from PIL import Image, ImageTk  # Pillow library for handling images

# Assume you have a black hole image named "black_hole.png" in the same directory as the script
black_hole_image_path = "black_hole.png"

class LightSource:
    # ... (unchanged)

class GravitationalLens:
    # ... (unchanged)

class LensSimulator:
    def __init__(self, light_source, gravitational_lens):
        self.light_source = light_source
        self.gravitational_lens = gravitational_lens
        self.ray_positions = []

    def simulate(self, time_steps):
        for _ in range(time_steps):
            ray_position = self.light_source.emit_ray()
            deflection = self.gravitational_lens.calculate_deflection(ray_position)
            ray_position = np.add(ray_position, deflection)
            self.ray_positions.append(ray_position)
        return self.ray_positions

class GravitationalLensingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gravitational Lensing Simulation")

        # Load the black hole image
        self.black_hole_image = Image.open(black_hole_image_path)
        self.black_hole_image = self.black_hole_image.resize((500, 500), Image.ANTIALIAS)  # Resize as needed
        self.tk_black_hole_image = ImageTk.PhotoImage(self.black_hole_image)

        self.light_source = LightSource(position=(0, 0), direction=(1, 0))
        self.gravitational_lens = GravitationalLens(mass=10, position=(0, 5))
        self.simulator = LensSimulator(self.light_source, self.gravitational_lens)

        self.figure, self.ax = Figure(), self.figure.add_subplot(111)
        self.ax.imshow(self.black_hole_image, extent=[-250, 250, -250, 250])
        self.ax.set_xlim(-250, 250)
        self.ax.set_ylim(-250, 250)

        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.plot_simulation()

    def plot_simulation(self):
        self.ax.clear()
        self.ax.imshow(self.black_hole_image, extent=[-250, 250, -250, 250])

        ray_positions = np.array(self.simulator.simulate(time_steps=10))
        self.ax.plot(ray_positions[:, 0], ray_positions[:, 1], label="Light Ray", color='cyan')
        self.ax.scatter(*self.gravitational_lens.position, color='red', label="Gravitational Lens")
        self.ax.scatter(*self.light_source.position, color='blue', label="Light Source")

        self.ax.set_title("Gravitational Lensing Simulation")
        self.ax.set_xlabel("X-axis")
        self.ax.set_ylabel("Y-axis")
        self.ax.legend()

        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = GravitationalLensingApp(root)
    root.mainloop()
