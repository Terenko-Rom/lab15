import json
import tkinter as tk
data = '''
{
    "elements": {
        "Hydrogen": {"number": 1, "mass": 1.008},
        "Helium": {"number": 2, "mass": 4.0026},
        "Lithium": {"number": 3, "mass": 6.94}
    }
}
'''
elements_data = json.loads(data)["elements"]
def show_element_info():
    element_name = entry.get().capitalize()
    if element_name in elements_data:
        element = elements_data[element_name]
        message = f"Name: {element_name}\nAtomic Number: {element['number']}\nAtomic Mass: {element['mass']}"
    else:
        message = "Element not found"
    result_label.config(text=message)
root = tk.Tk()
root.geometry("410x380")
root.configure(bg="olive")
root.title("Довідник хімічних елементів")
frame = tk.Frame(root, bg="olive")
frame.pack(pady=20)
label = tk.Label(frame, text="Введіть назву елемента:", bg="olive")
label.pack(side="left")
entry = tk.Entry(frame)
entry.pack(side="left")
button = tk.Button(frame, text="Показати інформацію", command=show_element_info)
button.pack(side="left")
result_label = tk.Label(root, text="", bg="olive", font=("Arial", 12), justify="left")
result_label.pack(pady=20)
root.mainloop()