import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Image Viewer")

# Open the image file in PhotoImage format
# Note: PhotoImage has limited support for PNG; check if your image is displayed correctly
image_path = "black_hole.png"  # Replace with the path to your PNG image
tk_image = tk.PhotoImage(file=image_path)

# Create a label to display the image
image_label = tk.Label(root, image=tk_image)
image_label.pack()

# Run the Tkinter event loop
root.mainloop()