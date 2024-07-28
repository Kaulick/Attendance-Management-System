import tkinter as tk
from tkinter import messagebox
import pandas as pd
from datetime import datetime
import os


ATTENDANCE_FILE = "attendance.csv"

def mark_attendance(name, student_id):
    if not name or not student_id:
        messagebox.showwarning("Input Error", "Please enter both Name and ID")
        return

    
    if not os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, 'w') as f:
            f.write('ID,Name,Time\n')

    
    attendance = pd.read_csv(ATTENDANCE_FILE)

   
    if student_id not in attendance['ID'].values:
        with open(ATTENDANCE_FILE, 'a') as f:
            now = datetime.now()
            dt_string = now.strftime('%Y-%m-%d %H:%M:%S')
            f.write(f'{student_id},{name},{dt_string}\n')
        messagebox.showinfo("Success", "Attendance marked successfully")
    else:
        messagebox.showwarning("Already Marked", "Attendance already marked for this ID")

def show_attendance():
    if os.path.exists(ATTENDANCE_FILE):
        attendance = pd.read_csv(ATTENDANCE_FILE)
        attendance_list.delete(0, tk.END)
        for index, row in attendance.iterrows():
            attendance_list.insert(tk.END, f"{row['ID']} - {row['Name']} - {row['Time']}")
    else:
        messagebox.showwarning("No Records", "No attendance records found")


root = tk.Tk()
root.title("Attendance Management System")


tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="ID:").grid(row=1, column=0, padx=10, pady=10)
id_entry = tk.Entry(root)
id_entry.grid(row=1, column=1, padx=10, pady=10)

mark_button = tk.Button(root, text="Mark Attendance", command=lambda: mark_attendance(name_entry.get(), id_entry.get()))
mark_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

show_button = tk.Button(root, text="Show Attendance", command=show_attendance)
show_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

attendance_list = tk.Listbox(root, width=50)
attendance_list.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()
