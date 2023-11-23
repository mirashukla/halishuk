import tkinter as tk
import os

# Create the main application window
root = tk.Tk()
root.title("Image Viewer")

# Open the image file in PhotoImage format
# Note: PhotoImage has limited support for PNG; check if your image is displayed correctly
image_path = str(os.getcwd()) + "/black_hole.png"  # Replace with the path to your PNG image
tk_image = tk.PhotoImage(file=image_path)

# Create a label to display the image
image_label = tk.Label(root, image=tk_image)
image_label.pack()

# Run the Tkinter event loop
root.mainloop()