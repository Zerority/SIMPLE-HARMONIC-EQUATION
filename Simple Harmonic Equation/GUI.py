import tkinter as tk

root = tk.Tk()
root.geometry("1000x700")
root.title("Calculating equation of simple harmonic motion")

tittle = tk.Label(root, text="Enter the values for amplitude, frequency, and time:", font = ("Times New Roman", 30), fg = "#000080")
tittle.pack(pady = 15)

sub_tittle = tk.Label(root, text = "Correct form of the simple harmonic motion equation : x(t) = a cos(ωt + φ)", font = ("Times New Roman", 20), fg = "#000000")
sub_tittle.pack()

#Creating the frame  
frame_enter = tk.Frame(root, bg = "#FFFFFF")
frame_enter.pack(pady = 15)
#Enter biendo A
tk.Label(frame_enter, text = "Enter Amplitude :", font = ("Times New Roman", 17), bg = "#FFFFFF").grid(row = 0, column = 0, pady = 15, padx = 15) 
entry_Amplitude = tk.Entry(frame_enter, width = 15, font = ("Times New Roman", 17), justify = "center")
entry_Amplitude.grid(row = 0, column = 1, pady = 15, padx = 15)
#Enter tanso f
tk.Label(frame_enter, text = "Enter Frequency :", font = ("Times New Roman", 17), bg = "#FFFFFF").grid(row = 1, column = 0, pady = 15, padx = 15) 
entry_frequency = tk.Entry(frame_enter, width = 15, font = ("Times New Roman", 17), justify = "center")
entry_frequency.grid(row = 1, column = 1, pady = 15, padx = 15)
#Enter initial phase angle
tk.Label(frame_enter, text = "Enter Initial Phase Angle :", font = ("Times New Roman", 17), bg = "#FFFFFF").grid(row = 2, column = 0, pady = 15, padx = 15) 
entry_initial_phase_angle = tk.Entry(frame_enter, width = 15, font = ("Times New Roman", 17), justify = "center")
entry_initial_phase_angle.grid(row = 2, column = 1, pady = 15, padx = 15)
#Enter time t
tk.Label(frame_enter, text = "Enter the time t :", font = ("Times New Roman", 17), bg = "#FFFFFF").grid(row = 3, column = 0, padx = 15, pady = 15)
entry_time_t = tk.Entry(frame_enter, width = 15 , font = ("Times New Roman", 17), justify = "center")
entry_time_t.grid(row = 3, column = 1, pady = 15, padx = 15 )
#Creating the button
button_calulating = tk.Button(root, text = "Calculate the value of the simple harmonic equation", width = 40
, font = ("Times New Roman", 12), bg = "#FFFFFF" , fg = "#000080")
button_calulating.pack(padx = 20)
#Creating the fram
frame_result = tk.LabelFrame(root, text=" Value ", font=("Times New Roman", 20, "italic"), bg="#F5F5F5", padx=10, pady=10)
frame_result.pack(pady=10, fill="both", expand=True, padx=20)
label_show = tk.Label(label_result, text="Please enter variables and click the button.", font=("Times New Roman", 15), bg="#F5F5F5", fg="#808080")
label_show.pack(pady=20)
root.mainloop()