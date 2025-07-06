# 🏛️ Caesar Cipher – Encryption & Decryption Tool

The Caesar Cipher is one of the earliest known and simplest encryption techniques in classical cryptography. Named after **Julius Caesar**, who used it to protect military messages, the cipher works by shifting each letter of a message by a fixed number of positions in the alphabet.

This project presents a **Caesar Cipher Tool** built using Python, offering a user-friendly **GUI (Tkinter)** to encrypt or decrypt messages with a customizable shift value. It serves as a hands-on introduction to fundamental encryption logic and GUI design.

---

## 🎯 Objectives

- ✅ Implement classical Caesar Cipher algorithm in Python
- ✅ Provide an interactive GUI for:
  - Text input
  - Key input (1–25)
  - Encryption or Decryption selection
- ✅ Support both uppercase and lowercase letters
- ✅ Preserve non-alphabetic characters (spaces, punctuation, etc.)
- ✅ Wrap around the alphabet when needed (e.g., Z → C)

---

## 🔐 How Caesar Cipher Works

The Caesar Cipher shifts each letter by a certain number of positions (**key**) in the alphabet.

### 🔁 Encryption:
- Shifts each character **forward** by the key value
- Wraps from `Z → A` when needed

### 🔁 Decryption:
- Shifts each character **backward** by the key value
- Wraps from `A → Z` when needed

### ✏️ Example (key = 3):
"HELLO" → "KHOOR"
"ZEBRA" → "CHEUD"


---

## ℹ️ Notes

- The cipher **ignores case when calculating the shift**, but **preserves the original case**
- **Non-alphabetic characters** (e.g., digits, punctuation) are **not changed**

---

## 🖥️ GUI App – Tkinter

### Features:

- Simple, lightweight Python GUI
- Textbox to enter the message
- Input field for the key (restricted to 1–25)
- Radio buttons for selecting Encrypt or Decrypt
- Output shown below after clicking “Run”

### How it Works:

- Uses `tkinter` for layout, widgets, and button actions
- Calls the Caesar logic function with text, key, and mode
- Displays result in a label

---

## 🧰 Tech Stack

- **Language**: Python  
- **Libraries**: `tkinter` (for GUI), `string` (for alphabet handling)  
- **Encryption Type**: Substitution (**Symmetric Key Cipher**)

---

## 🚀 To Run

### 🛠️ Requirements

- Python 3.x  
- No additional installations required (uses built-in libraries)

### ▶️ Run the GUI App

```bash
python caesar_gui.py
