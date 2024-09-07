import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Connect to MySQL Database
def connect_to_database():
    try:
        # Replace 'your_username' and 'your_password' with your MySQL username and password
        con = mysql.connector.connect(
            host="localhost",
            user="your_username",  # Update this line
            password="your_password",  # Update this line
            database="registration"
        )
        return con
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error connecting to MySQL: {err}")
        return None

# Initialize Database Connection
con = connect_to_database()
if con:
    cur = con.cursor(buffered=True)

    # Create Table if Not Exists
    cur.execute("""
    CREATE TABLE IF NOT EXISTS registration_details (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age INT,
        gender VARCHAR(10),
        email VARCHAR(255),
        mobile VARCHAR(15)
    );
    """)

def Registration():
    # Get data from Entry widgets
    name = e1.get()
    age = e2.get()
    gender = e3.get()
    email = e4.get()
    mobile = e5.get()

    # Validate inputs
    if not (name and age and gender and email and mobile):
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    try:
        # SQL insert statement
        query = "INSERT INTO registration_details (name, age, gender, email, mobile) VALUES (%s, %s, %s, %s, %s)"
        values = (name, int(age), gender, email, mobile)

        # Execute the query
        cur.execute(query, values)
        con.commit()

        # Clear the entry fields after submission
        e1.delete(0, tk.END)
        e2.delete(0, tk.END)
        e3.delete(0, tk.END)
        e4.delete(0, tk.END)
        e5.delete(0, tk.END)

        messagebox.showinfo("Success", "Registration successful!")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

# Initialize the main window
win = tk.Tk()
win.geometry("500x400")
win.title("Registration Portal")

# Create Labels
l1 = tk.Label(win, text="Person Details", font=("Arial", 16))
l2 = tk.Label(win, text="Name:")
l3 = tk.Label(win, text="Age:")
l4 = tk.Label(win, text="Gender:")
l5 = tk.Label(win, text="Email:")
l6 = tk.Label(win, text="Mobile Number:")

# Place Labels using grid
l1.grid(row=0, column=1, pady=10)
l2.grid(row=1, column=0, padx=10, pady=5)
l3.grid(row=2, column=0, padx=10, pady=5)
l4.grid(row=3, column=0, padx=10, pady=5)
l5.grid(row=4, column=0, padx=10, pady=5)
l6.grid(row=5, column=0, padx=10, pady=5)

# Create Entry widgets
e1 = tk.Entry(win)
e2 = tk.Entry(win)
e3 = tk.Entry(win)
e4 = tk.Entry(win)
e5 = tk.Entry(win)

# Place Entry widgets using grid
e1.grid(row=1, column=1, padx=10, pady=5)
e2.grid(row=2, column=1, padx=10, pady=5)
e3.grid(row=3, column=1, padx=10, pady=5)
e4.grid(row=4, column=1, padx=10, pady=5)
e5.grid(row=5, column=1, padx=10, pady=5)

# Submit Button
b = tk.Button(win, text="Submit Here", command=Registration)
b.grid(row=6, column=1, pady=20)

# Start the main loop
win.mainloop()

# Close the connection after the program ends
con.close()
