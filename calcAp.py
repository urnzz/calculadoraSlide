import tkinter as tk
from tkinter import ttk
import math

def calculate():
    try:
        number = float(number_var.get())
        percentage1 = float(percentage1_var.get().strip('%')) / 100
        percentage2 = float(percentage2_var.get().strip('%')) / 100
        result1.set(number * percentage1)
        result2.set(math.floor(number * percentage2))
        update_progress()
        calculate_profit()
    except ValueError:
        result1.set("Invalid input")
        result2.set("Invalid input")

def next_calculation():
    global count
    try:
        number = float(number_var.get())
        result2_value = float(result2.get())
        new_number = number + result2_value
        number_var.set(new_number)
        percentage2 = float(percentage2_var.get().strip('%')) / 100
        result2.set(math.floor(new_number * percentage2))
        update_progress()
        count += 1
        count_label.config(text=f"{count}/61")
    except ValueError:
        result1.set("Invalid input")
        result2.set("Invalid input")

def update_progress():
    try:
        current = float(number_var.get())
        goal = float(result1.get())
        progress = min((current / goal) * 100, 100)  # Ensure progress does not exceed 100
        progress_bar['value'] = progress
    except ValueError:
        progress_bar['value'] = 0

def calculate_profit():
    try:
        current = float(number_var.get())
        spent = current * float(robux_buy.get())
        fpro = ((((float(result1.get())/100)*70)/100)*70)*float(robux.get())
        profit_label.config(text=f"You spent $"+str(round(spent,2))+" to get "+str(current)+" robux and sold "+str(float(result1.get()))+" for $"+str(round(fpro,2)))
    except Exception as e:
        print('error'+str(e))
# Create the main window
root = tk.Tk()
root.title("Percentage Calculator")

# Styling
style = ttk.Style()
style.theme_use('clam')

# Variables for entries and results
number_var = tk.StringVar()
robux = tk.StringVar(value="0.008")
robux_buy = tk.StringVar(value="0.002293")
percentage1_var = tk.StringVar(value="256%")  # Default profit set to 256%
percentage2_var = tk.StringVar(value="1.5625%")
result1 = tk.StringVar()
result2 = tk.StringVar()
additional_result = tk.StringVar()
count = 0  # Initialize count
# Frames for layout
input_frame = ttk.Frame(root)
output_frame = ttk.Frame(root)
button_frame = ttk.Frame(root)
progress_frame = ttk.Frame(root)

# Creating the widgets
number_label = ttk.Label(input_frame, text="Bankroll")
number_entry = ttk.Entry(input_frame, textvariable=number_var)

percentage1_label = ttk.Label(input_frame, text="Desired Profit")
percentage1_entry = ttk.Entry(input_frame, textvariable=percentage1_var)

percentage2_label = ttk.Label(input_frame, text="Risk per Operation")
percentage2_entry = ttk.Entry(input_frame, textvariable=percentage2_var)

robux_label = ttk.Label(input_frame, text="Robux Price (Sell)")
robux_entry = ttk.Entry(input_frame, textvariable=robux)

robux_buy_label = ttk.Label(input_frame, text="Robux Price (Buy)")
robux_buy_entry = ttk.Entry(input_frame, textvariable=robux_buy)

result1_label = ttk.Label(output_frame, text="Goal")
result1_entry = ttk.Entry(output_frame, textvariable=result1, state='readonly')

result2_label = ttk.Label(output_frame, text="Next Bet Value")
result2_entry = ttk.Entry(output_frame, textvariable=result2, state='readonly')

calculate_button = ttk.Button(button_frame, text="Calculate", command=calculate)
next_button = ttk.Button(button_frame, text="Next", command=next_calculation)

progress_bar = ttk.Progressbar(progress_frame, orient="horizontal", length=300, mode='determinate')
count_label = ttk.Label(progress_frame, text="0/61")  # Count label
profit_label = ttk.Label(progress_frame, text="")  # Count label
# Placing frames
input_frame.grid(row=0, column=0, padx=10, pady=5)
output_frame.grid(row=1, column=0, padx=10, pady=5)
button_frame.grid(row=2, column=0, padx=10, pady=5)
progress_frame.grid(row=3, column=0, padx=10, pady=5)

# Placing widgets in frames
number_label.grid(row=0, column=0)
number_entry.grid(row=0, column=1)

percentage1_label.grid(row=1, column=0)
percentage1_entry.grid(row=1, column=1)

percentage2_label.grid(row=2, column=0)
percentage2_entry.grid(row=2, column=1)

robux_label.grid(row=3, column=0)
robux_entry.grid(row=3, column=1)
robux_buy_label.grid(row=4, column=0)
robux_buy_entry.grid(row=4, column=1)

result1_label.grid(row=0, column=0)
result1_entry.grid(row=0, column=1)

result2_label.grid(row=1, column=0)
result2_entry.grid(row=1, column=1)

calculate_button.grid(row=0, column=0, padx=5)
next_button.grid(row=0, column=1, padx=5)

progress_bar.grid(row=0, column=0, pady=10)
count_label.grid(row=1, column=0, pady=5)
profit_label.grid(row=2, column=0, pady=5)
# Running the application
root.mainloop()
