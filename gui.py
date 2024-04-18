
# Amy Saad
# March 20th, 2024
# COMP 325
# Project 1
# File: gui.py
# Overview: creates a GUI popup window using Tkinter, allowing users to enter SQL queries, 
# execute them on the connected SQLite database, and display the results in an output box

# Part 2 & 3:
# ---------------------------------------------------------

import tkinter as tk
from tkinter import messagebox
import sqlite3

def execute_query():                                                                     # function to execute the SQL query 
    query = query_entry.get()                                                            # gets the SQL query from the input 

    try:                                                                                 # connects to the SQLite database
        connection = sqlite3.connect("zoo_dataset.db")
        cursor = connection.cursor()
                                                                                         # executes the SQL query
        cursor.execute(query)
        rows = cursor.fetchall()                                                         # fetches all results from query

                                                                                         # displays the query results in the output box
        output_box.delete(1.0, tk.END)                                                   # clears previous results
        for row in rows:
            output_box.insert(tk.END, str(row) + "\n")

                                                                                         # commits changes and close the connection
        connection.commit()
        connection.close()
        
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Failed to execute SQL query: {e}")

 
def create_popup():                                                                      # function to create the GUI window
    popup = tk.Tk()
    popup.title("Characterisitcs of Zoo Animals")                                        # GUI window title
    popup.geometry("700x300")                                                            # size of window
 
                                                                                         # ceates a frame for the GUI components
    main_frame = tk.Frame(popup)
    main_frame.pack(padx=10, pady=10)

                                                                                         # SQL query text box
    global query_entry                                                                   # makes query_entry accessible from other functions
    query_label = tk.Label(main_frame, text="SQL Query:")
    query_label.grid(row=0, column=0, sticky="w")

    query_entry = tk.Entry(main_frame, width=50)
    query_entry.grid(row=0, column=1, padx=5)    

                                                                                         # execute query button
    execute_button = tk.Button(main_frame, text="Execute Query", command=execute_query)
    execute_button.grid(row=0, column=2, padx=5)

                                                                                         # output box
    global output_box                                                                    # makes output_box accessible from other functions
    output_box = tk.Text(main_frame, height=10, width=50)
    output_box.grid(row=1, column=0, columnspan=3, pady=10)

    popup.mainloop()

if __name__ == "__main__":
    create_popup()
