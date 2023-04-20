import tkinter as tk
from datetime import datetime
import os

# Function to append a log entry to the log file
def append_to_log_file(event=None):
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    with open(get_log_file_path(), "a") as file:
        file.write(f"{dt_string}: {text_input.get()}\n")
    text_input.delete(0, tk.END)
    display_log_contents()

# Function to read the contents of the log file and display them in the Text widget
def display_log_contents():
    with open(get_log_file_path(), "r") as file:
        log_contents = file.readlines()
    log_contents.reverse()
    log_text.delete(1.0, tk.END)
    for line in log_contents:
        log_text.insert(tk.END, line)

# Function to get the log file path for the current date
def get_log_file_path():
    now = datetime.now()
    date_string = now.strftime("%Y-%m-%d")
    log_dir = "log_file_"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    return f"{log_dir}{date_string}.txt"

# Initialize the Tkinter window
root = tk.Tk()
root.title("Troubleshooting Log Entry Program")

# Create a label for the text input box
text_label = tk.Label(root, text="Enter troubleshooting step:")

# Initialize the text input box
text_input = tk.Entry(root, width=450)

# Pack the label and text input box into the window
text_label.pack()
text_input.pack()

# Bind the <Return> event to the append_to_log_file function
text_input.bind("<Return>", append_to_log_file)

# Initialize the submit button
submit_button = tk.Button(root, text="Submit", command=append_to_log_file)

# Pack the submit button into the window
submit_button.pack()

# Initialize the Text widget to display log contents
log_text = tk.Text(root, height=20, width=80)
log_text.pack()

# Display the initial contents of the log file
display_log_contents()

# Start the Tkinter event loop
root.mainloop()
