import tkinter as tk

def on_click(button_value):
    current_text = entry.get()
    if current_text == "Error":
        current_text = ""

    if button_value == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_value == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_value)

# Create the main window
app = tk.Tk()
app.title("Simple Calculator")

# Entry widget for displaying and entering numbers
entry = tk.Entry(app, width=20, font=('Arial', 16), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Function to create and place buttons
row_val = 1
col_val = 0
for button in buttons:
    tk.Button(app, text=button, width=5, height=2, command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the application
app.mainloop()
