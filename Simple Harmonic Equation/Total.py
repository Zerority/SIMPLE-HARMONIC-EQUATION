import tkinter as tk
from tkinter import messagebox
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def calculate_value():
    try:
        biendo = float(entry_Amplitude.get())
        tanso = float(entry_frequency.get())
        pha = float(entry_initial_phase_angle.get())
        thoigian = float(entry_time_t.get())
        pha_rad = math.radians(pha)
        omega = 2 * math.pi * tanso
        x = biendo * math.cos(omega * thoigian + pha_rad)
        lamtron = round(x, 2)
        
        result = f"The Value of the simple harmonic equation is \n {lamtron}"
        label_show.config(text=result, fg="#2E7D32", font=("Times New Roman", 20, "bold"))
        
        # DRAWING THE GRAPH
        chu_ky_T = 1 / tanso if tanso != 0 else 1 #In case frequency = 0
        max_time = max(2 * chu_ky_T, thoigian * 1.2)
        t_plot = np.linspace(0, max_time, 1000)
        x_plot = biendo * np.cos(omega * t_plot + pha_rad)
        ax.clear()
        ax.plot(t_plot, x_plot, color="#000080", linewidth=2, label="x(t)")
        ax.plot(thoigian, x, marker='o', color='red', markersize=8, label=f"t = {thoigian}s")
        canvas.draw()
        
    except ValueError:
        messagebox.showerror("Input error", "Please enter the Amplitude, frequency, phase and time in numerical form!")

# STARTING THE TKINTER
root = tk.Tk()
root.geometry("1100x850") 
root.title("Calculating equation of simple harmonic motion")

tittle = tk.Label(root, text="Enter the values for amplitude, frequency, and time:", font=("Times New Roman", 26), fg="#000080")
tittle.pack(pady=10)

sub_tittle = tk.Label(root, text="Correct form of the simple harmonic motion equation : x(t) = a cos(ωt + φ)", font=("Times New Roman", 16), fg="#000000")
sub_tittle.pack()

# Creating the frame  
frame_enter = tk.Frame(root, bg="#FFFFFF")
frame_enter.pack(pady=10)

# Enter biendo A
tk.Label(frame_enter, text="Enter Amplitude (a):", font=("Times New Roman", 14), bg="#FFFFFF").grid(row=0, column=0, pady=5, padx=15, sticky="e") 
entry_Amplitude = tk.Entry(frame_enter, width=15, font=("Times New Roman", 14), justify="center")
entry_Amplitude.grid(row=0, column=1, pady=5, padx=15)

# Enter tanso f
tk.Label(frame_enter, text="Enter Frequency (f in Hz):", font=("Times New Roman", 14), bg="#FFFFFF").grid(row=1, column=0, pady=5, padx=15, sticky="e") 
entry_frequency = tk.Entry(frame_enter, width=15, font=("Times New Roman", 14), justify="center")
entry_frequency.grid(row=1, column=1, pady=5, padx=15)

# Enter initial phase angle
tk.Label(frame_enter, text="Enter Initial Phase Angle (φ in degrees):", font=("Times New Roman", 14), bg="#FFFFFF").grid(row=2, column=0, pady=5, padx=15, sticky="e") 
entry_initial_phase_angle = tk.Entry(frame_enter, width=15, font=("Times New Roman", 14), justify="center")
entry_initial_phase_angle.grid(row=2, column=1, pady=5, padx=15)

# Enter time t
tk.Label(frame_enter, text="Enter the time t (s):", font=("Times New Roman", 14), bg="#FFFFFF").grid(row=3, column=0, padx=15, pady=5, sticky="e")
entry_time_t = tk.Entry(frame_enter, width=15, font=("Times New Roman", 14), justify="center")
entry_time_t.grid(row=3, column=1, pady=5, padx=15)

# Creating the button
button_calulating = tk.Button(root, text="Calculate and Plot the Graph", width=40, font=("Times New Roman", 12, "bold"), bg="#000080", fg="#FFFFFF", command=calculate_value)
button_calulating.pack(pady=10)

frame_result = tk.LabelFrame(root, text=" Result ", font=("Times New Roman", 14, "italic"), bg="#F5F5F5", padx=10, pady=5)
frame_result.pack(pady=5, fill="x", padx=20)
label_show = tk.Label(frame_result, text="Please enter variables and click the button.", font=("Times New Roman", 14), bg="#F5F5F5", fg="#808080")
label_show.pack(pady=5)

# Creating a frame for the graph
fig, ax = plt.subplots(figsize=(6, 3.2), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(pady=10, fill="both", expand=True, padx=20)

root.mainloop()
