import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont


def convert_temperature():
    temp_amount = float(temp_entry.get())

    if temp_unit.get() == "Celsius":
        temp_fahrenheit.set(round(1.8 * temp_amount + 32, 2))
        temp_kelvin.set(round(temp_amount + 273.15, 2))
    elif temp_unit.get() == "Fahrenheit":
        temp_celsius.set(round((temp_amount - 32) / 1.8, 2))
        temp_kelvin.set(round((temp_amount - 32) / 1.8 + 273.15, 2))
    elif temp_unit.get() == "Kelvin":
        temp_celsius.set(round(temp_amount - 273.15, 2))
        temp_fahrenheit.set(round((temp_amount - 273.15) * 9/5 + 32, 2))

# Create the main window
root = tk.Tk()
root.title("Temp Converter")
root.geometry("475x400")
root.config(bg="light blue")

# Variables to store temperature values
temp_celsius = tk.DoubleVar()
temp_fahrenheit = tk.DoubleVar()
temp_kelvin = tk.DoubleVar()
temp_unit = tk.StringVar()

# Temperature input entry
temp_entry = tk.Entry(root, width=6, font=("Time New Roman", 27, "bold"), bg="white")
temp_entry.grid(row=0, column=0, padx=10, pady=10)

# Temperature unit selection
unit_options = ["Celsius", "Fahrenheit", "Kelvin"]
temp_unit.set(unit_options[0])
unit_menu = tk.OptionMenu(root, temp_unit, *unit_options)
unit_menu.grid(row=0, column=1, padx=10, pady=10)
unit_menu.config(font=("Time New Roman", 20, "bold"), bg="white")  # Set the font size to 16
convert_button = tk.Button(root, text="Convert", width=7, font=("Time New Roman", 17, "bold"), bg="white", command=convert_temperature)
convert_button.grid(row=0, column=2, padx=10, pady=10)

# Result labels
tk.Label(root, text="C", font=("Time New Roman", 20, "bold"), bg="light blue").grid(row=1, column=0)
tk.Label(root, text="F", font=("Time New Roman", 20, "bold"), bg="light blue").grid(row=2, column=0)
tk.Label(root, text="K", font=("Time New Roman", 20, "bold"), bg="light blue").grid(row=3, column=0)

tk.Label(root, textvariable=temp_celsius, font=("Time New Roman", 20, "bold"), bg="light blue").grid(row=1, column=1)
tk.Label(root, textvariable=temp_fahrenheit, font=("Time New Roman", 20, "bold"), bg="light blue").grid(row=2, column=1)
tk.Label(root, textvariable=temp_kelvin, font=("Time New Roman", 20, "bold"), bg="light blue").grid(row=3, column=1)

# to reset this converter
def reset():
    temp_entry.delete(0, tk.END)
    temp_celsius.set("")
    temp_fahrenheit.set("")
    temp_kelvin.set("")
    temp_unit.set(unit_options[0])

# Reset button
reset_button = tk.Button(root, text="Reset", width=7, font=("Time New Roman", 17, "bold"), bg="white", command=reset)
reset_button.grid(row=4, column=1, padx=10, pady=10)

# to add more features
def about():
    tk.messagebox.showinfo("About", "Project Name: Temperature Converter\nDeveloper: Wakil Ahmad Hamidi\nEmail: wakilahmadhamidi24@gmail.com\nPhone: +91 7991515918\n\nOther features will be added soon\nPlease give your feedbacks and suggestions\nContributions are welcomed!\n\nزما نوم وکیل احمد حمیدي دی\n زه پلان لرم چې ژر تر ژره په تخنیکي نړۍ کې \nخپلې مورنۍ ژبې پښتو ته خدمت وکړم")
# add more button
def more():
    tk.messagebox.showinfo("More", "Other Projects:\n1) Advanced Calculator\n2) Pong Game\n3) Tic Tac Toe Game\n4) Digital Clock\n5) Bio Data App\n6) Shut Down App\n7) Stop Watch App\n\nMore project are under development\n\nStay tuned!")
more_button = tk.Button(root, text="More", width=7, font=("Time New Roman", 17, "bold"), bg="white", command=more)
more_button.grid(row=4, column=0, padx=10, pady=10)


# About button
about_button = tk.Button(root, text="About", width=7, font=("Time New Roman", 17, "bold"), bg="white", command=about)
about_button.grid(row=4, column=2, padx=10, pady=10)

# # add a status bar
# status_bar = tk.Label(root, text="Project Name: Temperature Converter\nDeveloper: Wakil Ahmad Hamidi\nEmail: wakilahmadhamidi24@gmail.com\nPhone: +91 7991515918\nPlease give your feedbacks and suggestions\nContributions are welcomed!", width=6, font=("Time New Roman", 10, "bold"), bg="white", bd=1, anchor=tk.W)
# status_bar.place(x=5, y=260, height=100, width=444)

# Create the canvas
canvas = tk.Canvas(root)
canvas.grid(row=5, column=0, columnspan=3)

# Use the 'place' method to set the new coordinates for the canvas
canvas.grid(row=5, column=0, columnspan=3)
canvas.config(bg="light blue")

canvas_text = canvas.create_text(10, 10, text='', font=("Time New Roman", 10, "bold"), anchor=tk.NW)
  
test_string = "Project Name: Temperature Converter App\nDeveloper: Wakil Ahmad Hamidi\nEmail: wakilahmadhamidi24@gmail.com\nPhone: +91 7991515918\nOther features will be added soon\nPlease give your feedbacks and suggestions\nContributions are welcomed!"
# Time delay between chars, in milliseconds
delta = 100
delay = 0
for i in range(len(test_string) + 1):
    s = test_string[:i]
    update_text = lambda s=s: canvas.itemconfigure(canvas_text, text=s)
    canvas.after(delay, update_text)
    delay += delta

# give the focus to the input entry
temp_entry.focus()

# Start the main loop

root.mainloop()