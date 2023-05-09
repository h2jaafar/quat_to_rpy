import tkinter as tk
from tkinter import ttk
import numpy as np

def quaternion_to_rpy(w, x, y, z):
    # Normalize quaternion
    norm = np.sqrt(w**2 + x**2 + y**2 + z**2)
    w /= norm
    x /= norm
    y /= norm
    z /= norm

    # Convert to RPY
    roll = np.arctan2(2 * (w * x + y * z), 1 - 2 * (x**2 + y**2))
    pitch = np.arcsin(2 * (w * y - z * x))
    yaw = np.arctan2(2 * (w * z + x * y), 1 - 2 * (y**2 + z**2))

    return roll, pitch, yaw

def convert():
    try:
        w, x, y, z = float(w_entry.get()), float(x_entry.get()), float(y_entry.get()), float(z_entry.get())
        roll, pitch, yaw = quaternion_to_rpy(w, x, y, z)
        roll_label.config(text=f"Roll: {np.degrees(roll):.2f}°")
        pitch_label.config(text=f"Pitch: {np.degrees(pitch):.2f}°")
        yaw_label.config(text=f"Yaw: {np.degrees(yaw):.2f}°")
    except ValueError:
        roll_label.config(text="Roll: Error")
        pitch_label.config(text="Pitch: Error")
        yaw_label.config(text="Yaw: Error")

root = tk.Tk()
root.title("Quaternion to RPY Converter")

mainframe = ttk.Frame(root, padding="10")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))



x_label = ttk.Label(mainframe, text="X:")
x_label.grid(row=0, column=0, sticky=tk.W)
x_entry = ttk.Entry(mainframe)
x_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

y_label = ttk.Label(mainframe, text="Y:")
y_label.grid(row=1, column=0, sticky=tk.W)
y_entry = ttk.Entry(mainframe)
y_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

z_label = ttk.Label(mainframe, text="Z:")
z_label.grid(row=2, column=0, sticky=tk.W)
z_entry = ttk.Entry(mainframe)
z_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

w_label = ttk.Label(mainframe, text="W:")
w_label.grid(row=3, column=0, sticky=tk.W)
w_entry = ttk.Entry(mainframe)
w_entry.grid(row=3, column=1, sticky=(tk.W, tk.E))

convert_button = ttk.Button(mainframe, text="Convert", command=convert)
convert_button.grid(row=4, column=1, sticky=tk.E)

roll_label = ttk.Label(mainframe, text="Roll:")
roll_label.grid(row=5, column=0, columnspan=2, sticky=tk.W)

pitch_label = ttk.Label(mainframe, text="Pitch:")
pitch_label.grid(row=6, column=0, columnspan=2, sticky=tk.W)

yaw_label = ttk.Label(mainframe, text="Yaw:")
yaw_label.grid(row=7, column=0, columnspan=2, sticky=tk.W)

# Set padding and column weights
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
mainframe.columnconfigure(1, weight=1)

root.mainloop()

