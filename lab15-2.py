import tkinter as tk
def calculate_average():
    numbers = entry_numbers.get()
    try:
        num_list = list(map(float, numbers.split()))
        if num_list:
            average = sum(num_list) / len(num_list)
            result_label.config(text=f"Average: {average:.2f}")
        else:
            result_label.config(text="No numbers entered")
    except ValueError:
        result_label.config(text="Please enter valid numbers")
root = tk.Tk()
root.geometry("300x200")
root.title("Average Calculator")
frame = tk.Frame(root)
frame.pack(pady=20)
label = tk.Label(frame, text="Enter numbers (space-separated):")
label.pack()
entry_numbers = tk.Entry(frame, width=30)
entry_numbers.pack()
button_calculate = tk.Button(root, text="Calculate Average", command=calculate_average)
button_calculate.pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()