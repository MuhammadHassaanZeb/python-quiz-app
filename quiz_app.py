#Muhammad Hassaan Zeb - 60301901
#INFS3203 - System Implemenation and Design - Lab 04
#Python Quiz App

import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "topic": "Loops",
        "question": "What will be the output of this Python code?",
        "code": "for i in range(3):\n    print(i)",
        "options": ["0 1 2", "1 2 3", "0 1 2 3", "1 2"],
        "answer": 0  # Correct answer is "0 1 2"
    },
    {
        "topic": "Lists",
        "question": "What will be the output of this Python code?",
        "code": "my_list = [1, 2, 3]\nmy_list.append(4)\nprint(my_list)",
        "options": ["[1, 2, 3, 4]", "[1, 2, 4]", "[4, 1, 2, 3]", "[1, 2, 3]"],
        "answer": 0  # Correct answer is "[1, 2, 3, 4]"
    },
    {
        "topic": "Strings",
        "question": "What will be the output of this Python code?",
        "code": "text = 'hello'\nprint(text.upper())",
        "options": ["HELLO", "hello", "HeLLo", "None"],
        "answer": 0  # Correct answer is "HELLO"
    },
    {
        "topic": "Variables",
        "question": "What will be the value of the variable `x` after the following code runs?",
        "code": "x = 5\nx += 2\nx *= 3",
        "options": ["21", "15", "7", "12"],
        "answer": 0  # Correct answer is "21"
    },
    {
        "topic": "Functions",
        "question": "What will be the output of this Python code?",
        "code": "def add(a, b):\n    return a + b\nprint(add(3, 5))",
        "options": ["8", "35", "None", "Error"],
        "answer": 0  # Correct answer is "8"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz Generator")

        # Topic Entry
        self.topic_label = tk.Label(root, text="Enter Topic:")
        self.topic_label.pack()

        self.topic_entry = tk.Entry(root)
        self.topic_entry.pack()

        # Button to generate question
        self.generate_button = tk.Button(root, text="Generate Question", command=self.generate_question)
        self.generate_button.pack()

        # Display question and code
        self.question_label = tk.Label(root, text="Question will appear here")
        self.question_label.pack()

        self.code_label = tk.Label(root, text="Code will appear here")
        self.code_label.pack()

        # Radio buttons for answer options
        self.var = tk.IntVar()
        self.option_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.var, value=i)
            self.option_buttons.append(rb)
            rb.pack()

        # Submit button
        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack()

        # Feedback label
        self.feedback_label = tk.Label(root, text="")
        self.feedback_label.pack()

        self.current_question = None  # To store the current question for reference

    def generate_question(self):
        topic = self.topic_entry.get()
        for question in questions:
            if question["topic"].lower() == topic.lower():
                self.current_question = question
                self.display_question(question)
                return
        
        # If no question is found
        messagebox.showerror("Error", "Topic not found.")

    def display_question(self, question):
        self.question_label.config(text=question["question"])
        self.code_label.config(text=question["code"])

        # Update the options
        for i, option in enumerate(question["options"]):
            self.option_buttons[i].config(text=option)

        # Reset the selected option
        self.var.set(-1)

    def check_answer(self):
        if self.current_question is None:
            messagebox.showwarning("Warning", "Please generate a question first.")
            return

        selected_option = self.var.get()
        if selected_option == self.current_question["answer"]:
            self.feedback_label.config(text="Correct!", fg="green")
        else:
            self.feedback_label.config(text="Incorrect. Try again.", fg="red")

# Initialize Tkinter root
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
