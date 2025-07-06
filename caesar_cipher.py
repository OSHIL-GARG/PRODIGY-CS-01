import tkinter as tk
from tkinter import messagebox
import string

def encrypt_decrypt(text, mode, key):
    result = ''
    key = key % 26
    if mode == 'decrypt':
        key = -key

    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            new_char = chr((ord(char) - base + key) % 26 + base)
            result += new_char
        else:
            result += char
    return result

def process_text():
    text = entry_text.get()
    try:
        key = int(entry_key.get())
        if not (1 <= key <= 25):
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Key", "Key must be an integer between 1 and 25.")
        return

    mode = mode_var.get()
    result = encrypt_decrypt(text, mode, key)
    result_label.config(text=f"Result: {result}")

# Tkinter GUI setup
window = tk.Tk()
window.title("Caesar Cipher - Tkinter GUI")

tk.Label(window, text="Enter Text:").pack()
entry_text = tk.Entry(window, width=50)
entry_text.pack()

tk.Label(window, text="Enter Key (1-25):").pack()
entry_key = tk.Entry(window, width=10)
entry_key.pack()

mode_var = tk.StringVar(value="encrypt")
tk.Radiobutton(window, text="Encrypt", variable=mode_var, value="encrypt").pack()
tk.Radiobutton(window, text="Decrypt", variable=mode_var, value="decrypt").pack()

tk.Button(window, text="Submit", command=process_text).pack(pady=5)
result_label = tk.Label(window, text="Result: ")
result_label.pack()

window.mainloop()
