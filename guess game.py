import random
import tkinter as tk
from tkinter import messagebox

def reset_game():
    global random_number, attempts
    random_number = random.randint(1, 100)
    attempts = 0
    entry_guess.delete(0, tk.END)
    result_label.config(text="Game reset! Start guessing.")

def check_guess():
    global attempts
    try:
        user_guess = int(entry_guess.get())
        attempts += 1

        if user_guess < random_number:
            result_label.config(text="Too low! Try again.")
        elif user_guess > random_number:
            result_label.config(text="Too high! Try again.")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed the number {random_number} correctly in {attempts} attempts!")
            reset_game()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")

def create_gui():
    global entry_guess, result_label

    root = tk.Tk()
    root.title("Number Guessing Game")

    # Instructions
    tk.Label(root, text="I have generated a random number between 1 and 100.").pack(pady=5)
    tk.Label(root, text="Your task is to guess the number.").pack(pady=5)

    # Input field
    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)

    tk.Label(input_frame, text="Enter your guess:").grid(row=0, column=0, padx=5)
    entry_guess = tk.Entry(input_frame, width=10)
    entry_guess.grid(row=0, column=1, padx=5)

    # Buttons
    tk.Button(input_frame, text="Submit", command=check_guess).grid(row=0, column=2, padx=5)
    tk.Button(input_frame, text="Reset", command=reset_game).grid(row=0, column=3, padx=5)

    # Result label
    result_label = tk.Label(root, text="Start guessing the number!", font=("Arial", 12))
    result_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    random_number = random.randint(1, 100)
    attempts = 0
    create_gui()
