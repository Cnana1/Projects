# Arithmetic Practice Game

An interactive arithmetic practice game developed using Python and Tkinter. This application helps users practice basic arithmetic operations such as addition, subtraction, multiplication, and division. It features real-time feedback, a countdown timer, dynamic GUI updates, and a SQLite database to track user performance.

## Features

- **Interactive GUI**: Built with Tkinter, providing a user-friendly interface for practicing arithmetic problems.
- **Real-time Feedback**: Immediate feedback on answers, indicating whether the user's answer is correct or incorrect.
- **Countdown Timer**: A 60-second timer that starts and stops with a button click, adding a challenging element to the practice session.
- **Random Question Generation**: Dynamically generates arithmetic questions with operands between 0 and 12.
- **Performance Tracking**: Stores user attempts in a SQLite database, including the percentage of correct answers, math operation type, user name, and date.
- **Database Management**: Features to add new entries and delete old data from the database.
- **Multiple Operations**: Allows users to practice addition, subtraction, multiplication, and division.

GUI Setup: The main window and layout are created using Tkinter, including labels, buttons, and entry fields.
Event Handling: Functions to handle button clicks, form submissions, and real-time feedback.
Question Generation: Logic to generate random arithmetic questions based on the selected operation.
Timer Functionality: A countdown timer that updates the GUI every second.
Database Integration: SQLite database to store and manage user performance data.
Key Functions
submit(): Handles the submission of answers and provides immediate feedback.
timer(): Manages the countdown timer.
toggle_timer(): Starts and stops the timer, and resets the game state.
generate_question(): Generates new arithmetic questions.
calculate_correct_answer(): Calculates the correct answer based on the current operation.
display_results(): Displays the user's performance after the timer ends.
try_again(): Resets the game for a new session.
