# Amy Saad
# March 20th 2024
# COMP 325
# File: README.TXT 

## Overview
This python program provides a graphical user interface (GUI) for interacting with a SQLite database containing a zoo dataset. Users can execute SQL queries through the GUI and view the results.

## Dependencies
- Python 3.11.5
- Tkinter 
- SQLite3

## Database Information
- Database Name: zoo_dataset.db
- Table Name: zoo_dataset

## How to Run the Program
1. Have Python 3.10 or later installed on your system
2. Download the program
3. Run the 'preprocessing.py' file using Python. The program should run and create a database for the zoo data
3. Run the `gui.py` file using Python. The GUI window should appear, allowing you to interact with the program and enter SQL commands to read data from the database


## How to Use the GUI
1. Enter your SQL query into the text box labeled "SQL Query"
2. Click the "Execute Query" button to run the query
3. The results of the query will be displayed in the output box below
4. To close the program, close the GUI window or press Ctrl+C in the terminal where the program is running

## Important Notes
- SQL queries are read-only. Forbidden SQL commands include DELETE, ALTER, UPDATE, SET, ADD, INSERT, RENAME, and CREATE. If entered, these commands will result in an error message from the SQL query
- The 'preprocessing.py' file should run with no crashes or creating duplicates, despite running it multiple times and without commenting out any code
- Was unable to figure out the quit command. Closing the GUI should work, quit command does not

