import tkinter as tk
from tkinter import messagebox
import re

# Function to evaluate password strength
def check_password_strength(password):
    criteria = {
        "Length (at least 8 characters)": len(password) >= 8,
        "Presence of lowercase letters": bool(re.search(r"[a-z]", password)),
        "Presence of uppercase letters": bool(re.search(r"[A-Z]", password)),
        "Presence of numbers": bool(re.search(r"[0-9]", password)),
        "Presence of special characters": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }

    strength = sum(criteria.values())
    return strength, criteria

# Function to display password strength
def display_strength():
    password = entry.get()
    strength, criteria = check_password_strength(password)

    # Display strength based on the number of criteria met
    if strength == 5:
        strength_label.config(text="Password Strength: Strong", fg="green")
    elif strength >= 3:
        strength_label.config(text="Password Strength: Medium", fg="orange")
    else:
        strength_label.config(text="Password Strength: Weak", fg="red")

    # Display criteria feedback
    feedback = "\n".join([f"{criterion}: {'✔' if met else '✘'}" for criterion, met in criteria.items()])
    criteria_label.config(text=feedback)

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x300")

# Label
label = tk.Label(root, text="Enter a password to check its strength:", font=("Helvetica", 12))
label.pack(pady=10)

# Password Entry Field
entry = tk.Entry(root, show="*", font=("Helvetica", 14), width=30)
entry.pack(pady=10)

# Button to check password strength
check_button = tk.Button(root, text="Check Password Strength", command=display_strength, font=("Helvetica", 12))
check_button.pack(pady=10)

# Label to display password strength
strength_label = tk.Label(root, text="", font=("Helvetica", 12))
strength_label.pack(pady=10)

# Label to display criteria results
criteria_label = tk.Label(root, text="", font=("Helvetica", 10), justify="left")
criteria_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
