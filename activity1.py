import tkinter as tk
from tkinter import messagebox

# Function to check login credentials
def login():
    username = entry_username.get()
    password = entry_password.get()

    # Simple validation for username and password
    if username == "admin" and password == "password123":
        messagebox.showinfo("Login Success", "You have logged in successfully!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Create the main window
window = tk.Tk()
window.title("Login Page")

# Create username label and entry field
label_username = tk.Label(window, text="Username:")
label_username.pack(pady=5)

entry_username = tk.Entry(window)
entry_username.pack(pady=5)

# Create password label and entry field
label_password = tk.Label(window, text="Password:")
label_password.pack(pady=5)

entry_password = tk.Entry(window, show="*")  # Hide the password characters
entry_password.pack(pady=5)

# Create login button
login_button = tk.Button(window, text="Login", command=login)
login_button.pack(pady=10)

# Run the application
window.mainloop()
