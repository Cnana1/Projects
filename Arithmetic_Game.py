from tkinter import *
from tkinter import ttk
import random

# Define the submit function
def submit(event=None):
    if timer_running:
        user_answer = answer_var.get()
        if user_answer.isdigit():
            user_answer = int(user_answer)
            correct_answer = calculate_correct_answer()
            submitted_answers.append(user_answer)
            correct_answers.append(correct_answer)
            if user_answer == correct_answer:
                feedback_var.set(f"Correct! {current_a} {operation} {current_b} = {correct_answer}")
            else:
                feedback_var.set(f"Incorrect! {current_a} {operation} {current_b} = {correct_answer}")
            answer_var.set('')
            generate_question()
        else:
            feedback_var.set("Please enter a valid number.")

# Define the timer function
def timer(time_left):
    global timer_running
    if timer_running:
        if time_left >= 0:
            timer_label.config(text=f"Time left: {time_left} seconds")
            root.after(1000, timer, time_left - 1)
        else:
            timer_label.config(text="Time's up!")
            timer_running = False
            disable_game()
            display_results()

# Function to start/stop the timer
def toggle_timer(reset=False):
    global timer_running
    if reset or not timer_running:
        timer_running = not timer_running
        if timer_running:
            start_button.config(text="Stop Timer")
            submit_button.state(["!disabled"])
            answer_entry.state(["!disabled"])
            operations_combo.config(state="disabled")  # Disable combobox during game
            timer(60)  # Start countdown with 60 seconds
            generate_question()
        else:
            disable_game()
    else:
        timer_running = False
        disable_game()

# Function to disable the game elements
def disable_game():
    start_button.config(text="Start Timer")
    submit_button.state(["disabled"])
    answer_entry.state(["disabled"])
    operations_combo.config(state="readonly")  # Enable combobox after game ends
    timer_label.config(text="Time left: 60 seconds")
    feedback_var.set("")
    result_label.config(text="")

# Function to generate a new question based on chosen operation
def generate_question():
    global current_a, current_b, operation
    current_a = random.randint(0, 12)
    current_b = random.randint(0, 12)
    operation = operations_var.get()
    if operation == "Addition":
        question_var.set(f"What is {current_a} + {current_b}?")
    elif operation == "Subtraction":
        question_var.set(f"What is {current_a} - {current_b}?")
    elif operation == "Multiplication":
        question_var.set(f"What is {current_a} * {current_b}?")
    elif operation == "Division":
        # Ensure division is valid (b != 0 and a % b == 0)
        while current_b == 0 or current_a % current_b != 0:
            current_a = random.randint(0, 12)
            current_b = random.randint(1, 12)
        question_var.set(f"What is {current_a} / {current_b}?")

# Function to calculate the correct answer based on the current operation
def calculate_correct_answer():
    if operation == "Addition":
        return current_a + current_b
    elif operation == "Subtraction":
        return current_a - current_b
    elif operation == "Multiplication":
        return current_a * current_b
    elif operation == "Division":
        return current_a // current_b

# Function to display results after the timer ends
def display_results():
    correct_count = sum(1 for x, y in zip(submitted_answers, correct_answers) if x == y)
    total_count = len(submitted_answers)
    percent_correct = (correct_count / total_count) * 100 if total_count > 0 else 0
    result_label.config(text=f"You got {percent_correct:.2f}% correct!\nCorrect Answers: {correct_count}\nTotal Questions: {total_count}")
    try_again_button.state(["!disabled"])

# Function to restart the game
def try_again():
    global submitted_answers, correct_answers
    submitted_answers = []
    correct_answers = []
    feedback_var.set("")
    result_label.config(text="")
    answer_var.set('')
    try_again_button.state(["disabled"])
    toggle_timer(reset=True)

root = Tk()
root.title("Arithmetic Practice Game")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size and position it in the center
window_width = int(screen_width * 0.6)
window_height = int(screen_height * 0.7)
window_x = (screen_width // 2) - (window_width // 2)
window_y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Initialize global variables
answer_var = StringVar()
question_var = StringVar()
feedback_var = StringVar()
timer_running = False
submitted_answers = []
correct_answers = []
current_a = 0
current_b = 0
operation = ""

# Define operation choices
operations = ["Addition", "Subtraction", "Multiplication", "Division"]

# Create operation selection label
operations_label = ttk.Label(root, text="Choose Operation:")
operations_label.place(relx=0.05, rely=0.05)

# Create operation selection combobox
operations_var = StringVar()
operations_combo = ttk.Combobox(root, textvariable=operations_var, values=operations, state="readonly", width=15)
operations_combo.place(relx=0.2, rely=0.05)
operations_combo.current(0)  # Set default value

# Creating an entry for the answer
answer_entry = ttk.Entry(root, textvariable=answer_var, font=('calibre', 10, 'normal'))
answer_entry.place(relx=0.2, rely=0.25, width=100)

# Creating a label for the answer
answer_label = ttk.Label(root, text='Answer:', font=('calibre', 10, 'bold'))
answer_label.place(relx=0.1, rely=0.25)

# Creating the Submit button
submit_button = ttk.Button(root, text="Submit", command=submit)
submit_button.place(relx=0.32, rely=0.25, width=80)

# Creating a label for the question
question_label = ttk.Label(root, textvariable=question_var, font=('calibre', 10, 'bold'))
question_label.place(relx=0.5, rely=0.25, anchor='center')

# Creating a label for feedback
feedback_label = ttk.Label(root, textvariable=feedback_var, font=('calibre', 10, 'bold'))
feedback_label.place(relx=0.05, rely=0.35)

# Creating label for the timer
timer_label = ttk.Label(root, text='Time left: 60 seconds', font=('calibre', 10, 'bold'))
timer_label.place(relx=0.7, rely=0.05)

# Creating the Start/Stop Timer button
start_button = ttk.Button(root, text="Start Timer", command=toggle_timer)
start_button.place(relx=0.7, rely=0.1)

# Creating a label for the results
result_label = ttk.Label(root, text='', font=('calibre', 10, 'bold'))
result_label.place(relx=0.05, rely=0.45)

# Creating the Try Again button
try_again_button = ttk.Button(root, text="Try Again", command=try_again)
try_again_button.place(relx=0.7, rely=0.15)
try_again_button.state(["disabled"])

# Bind the Enter key to the submit function
root.bind('<Return>', submit)

# Disable the submit button and answer entry initially
submit_button.state(["disabled"])
answer_entry.state(["disabled"])

root.mainloop()
