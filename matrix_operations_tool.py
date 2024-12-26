import numpy as np
import tkinter as tk
from tkinter import messagebox

# Function to handle matrix operations
def perform_operation():
    try:
        matrix1 = np.array(eval(entry_matrix1.get()))
        matrix2 = np.array(eval(entry_matrix2.get()))
        
        operation = operation_var.get()
        
        if operation == "Add":
            result = np.add(matrix1, matrix2)
        elif operation == "Subtract":
            result = np.subtract(matrix1, matrix2)
        elif operation == "Multiply":
            result = np.matmul(matrix1, matrix2)
        elif operation == "Transpose":
            result = np.transpose(matrix1)
        elif operation == "Determinant":
            result = np.linalg.det(matrix1)
        else:
            result = "Invalid operation"

        display_result(result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to display the result
def display_result(result):
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, str(result))

# Setting up the GUI
root = tk.Tk()
root.title("Matrix Operations Tool")

tk.Label(root, text="Enter Matrix 1:").grid(row=0, column=0)
entry_matrix1 = tk.Entry(root, width=50)
entry_matrix1.grid(row=0, column=1)

tk.Label(root, text="Enter Matrix 2 (optional):").grid(row=1, column=0)
entry_matrix2 = tk.Entry(root, width=50)
entry_matrix2.grid(row=1, column=1)

operation_var = tk.StringVar(value="Add")
tk.Label(root, text="Select Operation:").grid(row=2, column=0)
tk.OptionMenu(root, operation_var, "Add", "Subtract", "Multiply", "Transpose", "Determinant").grid(row=2, column=1)

tk.Button(root, text="Perform Operation", command=perform_operation).grid(row=3, column=0, columnspan=2)

tk.Label(root, text="Result:").grid(row=4, column=0)
result_text = tk.Text(root, height=10, width=50)
result_text.grid(row=4, column=1)

root.mainloop()
