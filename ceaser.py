import tkinter as tk
from tkinter import messagebox

def caesar_cipher():
    mode = mode_var.get()
    message = message_text.get("1.0", tk.END).rstrip("\n")
    shift_str = shift_entry.get()

    try:
        shift = int(shift_str) % 26
    except ValueError:
        messagebox.showerror("Error", "Shift must be an integer!")
        return

    result = ""
    for char in message:
        if char.isupper():
            result += chr((ord(char) - 65 + (shift if mode == 'e' else -shift)) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + (shift if mode == 'e' else -shift)) % 26 + 97)
        else:
            result += char

    result_text.config(state='normal')
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, result)
    result_text.config(state='disabled')

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_text.get("1.0", tk.END).rstrip("\n"))
    messagebox.showinfo("Copied", "Result copied to clipboard!")


root = tk.Tk()
root.title("Caesar Cipher")


tk.Label(root, text="Select Mode:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
mode_var = tk.StringVar(value='e')
tk.Radiobutton(root, text="Encrypt", variable=mode_var, value='e').grid(row=0, column=1)
tk.Radiobutton(root, text="Decrypt", variable=mode_var, value='d').grid(row=0, column=2)


tk.Label(root, text="Message:").grid(row=1, column=0, padx=5, pady=5, sticky="nw")
message_text = tk.Text(root, height=5, width=50)
message_text.grid(row=1, column=1, columnspan=2, padx=5, pady=5)


tk.Label(root, text="Shift (integer):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
shift_entry = tk.Entry(root)
shift_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# Run button
tk.Button(root, text="Run", command=caesar_cipher).grid(row=2, column=2, padx=5, pady=5)


tk.Label(root, text="Result:").grid(row=3, column=0, padx=5, pady=5, sticky="nw")
result_text = tk.Text(root, height=5, width=50, state='disabled')
result_text.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

# Copy button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).grid(row=4, column=1, pady=10)

# Run the GUI
root.mainloop()
