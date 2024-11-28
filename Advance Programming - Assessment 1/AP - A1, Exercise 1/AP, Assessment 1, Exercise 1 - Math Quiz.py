import tkinter as tk
from tkinter import messagebox
import random

class MathQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Quiz")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(expand=True)
        
        self.score = 0
        self.difficulty = ""
        self.questions = []
        self.current_question = 0
        self.tries = 0
        
        self.showStartScreen()

    def showStartScreen(self):
        self.clearFrame()
        
        heading = tk.Label(self.main_frame, text="Math Quiz", font=("Arial", 24, "bold"))
        heading.pack()
        
        start_button = tk.Button(self.main_frame, text="Start", font=("Arial", 16), command=self.displayMenu)
        start_button.pack(ipadx=9, ipady=3, pady=8)

    def displayMenu(self):
        self.clearFrame()
        
        heading = tk.Label(self.main_frame, text="Difficulty", font=("Arial", 24, "bold"))
        heading.pack()
        
        subtext = tk.Label(self.main_frame, text="Please Select a Level", font=("Arial", 14))
        subtext.pack()
        
        button_frame = tk.Frame(self.main_frame)
        button_frame.pack(pady=19)
        
        easy_button = tk.Button(button_frame, text="Easy", font=("Arial", 12), command=lambda: self.confirmDifficulty("Easy"))
        easy_button.pack(side="left", ipadx=5, ipady=3, padx=8)
        
        moderate_button = tk.Button(button_frame, text="Moderate", font=("Arial", 12), command=lambda: self.confirmDifficulty("Moderate"))
        moderate_button.pack(side="left", ipadx=5, ipady=3, padx=8)
        
        advanced_button = tk.Button(button_frame, text="Advanced", font=("Arial", 12), command=lambda: self.confirmDifficulty("Advanced"))
        advanced_button.pack(side="left", ipadx=5, ipady=3, padx=8)

    def confirmDifficulty(self, difficulty):
        self.difficulty = difficulty
        self.clearFrame()
        
        heading = tk.Label(self.main_frame, text="Continue with Selected Level?", font=("Arial", 18, "bold"))
        heading.pack()
        
        button_frame = tk.Frame(self.main_frame)
        button_frame.pack(pady=14)
        
        back_button = tk.Button(button_frame, text="Back", font=("Arial", 12), command=self.displayMenu)
        back_button.pack(side="left", ipadx=9, ipady=3, padx=9)
        
        start_button = tk.Button(button_frame, text="Start", font=("Arial", 12), command=self.startQuiz)
        start_button.pack(side="left", ipadx=9, ipady=3, padx=9)

    def startQuiz(self):
        self.generateQuestions()
        self.score = 0
        self.current_question = 0
        self.tries = 0
        self.displayProblem()

    def generateQuestions(self):
        self.questions = []
        for _ in range(10):
            num1, num2 = self.randomInt()
            operation = self.decideOperation()
            question = (num1, operation, num2)
            self.questions.append(question)

    def randomInt(self):
        """Determine the random numbers based on difficulty"""
        if self.difficulty == "Easy":
            return random.randint(1, 9), random.randint(1, 9)
        elif self.difficulty == "Moderate":
            return random.randint(10, 99), random.randint(10, 99)
        else:  # Advanced
            return random.randint(1000, 9999), random.randint(1000, 9999)

    def decideOperation(self):
        """Randomly decide if the operation is addition or subtraction"""
        return random.choice(["+", "-"])

    def displayProblem(self):
        self.clearFrame()
        if self.current_question >= 10:
            self.displayResults()
            return
        
        num1, operation, num2 = self.questions[self.current_question]
        self.current_answer = eval(f"{num1} {operation} {num2}")
        
        question_text = f"{self.current_question + 1}) {num1} {operation} {num2} = __"
        
        heading = tk.Label(self.main_frame, text=question_text, font=("Arial", 18))
        heading.pack(pady=8)
        
        self.answer_entry = tk.Entry(self.main_frame, font=("Arial", 14))
        self.answer_entry.pack()
        self.answer_entry.focus()
        
        submit_button = tk.Button(self.main_frame, text="Submit", font=("Arial", 12), command=self.isCorrect)
        submit_button.pack(ipadx=9, ipady=3, pady=14)

    def isCorrect(self):
        try:
            player_answer = int(self.answer_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return
        
        if player_answer == self.current_answer:
            if self.tries == 0:
                self.score += 10
            else:
                self.score += 5
            self.current_question += 1
            self.tries = 0
            self.displayProblem()
        else:
            self.tries += 1
            if self.tries >= 2:
                self.current_question += 1
                self.tries = 0
                self.displayProblem()

    def displayResults(self):
        self.clearFrame()

        # Calculate grade
        score_percentage = (self.score / 100) * 100
        grade = ""
        if score_percentage >= 90:
            grade = "A+"
        elif score_percentage >= 80:
            grade = "A"
        elif score_percentage >= 70:
            grade = "B"
        elif score_percentage >= 60:
            grade = "C"
        elif score_percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        # Display score and grade
        heading = tk.Label(self.main_frame, text="Your Score:", font=("Arial", 24, "bold"))
        heading.pack(pady=0)
        
        result_label = tk.Label(self.main_frame, text=f"{self.score} - {grade}", font=("Arial", 18))
        result_label.pack(pady=0)
        
        next_button = tk.Button(self.main_frame, text="Next", font=("Arial", 12), command=self.showEndScreen)
        next_button.pack(ipadx=9, ipady=3, pady=14)

    def showEndScreen(self):
        self.clearFrame()
        
        heading = tk.Label(self.main_frame, text="Solve the Quiz Again?", font=("Arial", 18, "bold"))
        heading.pack(pady=2)
        
        button_frame = tk.Frame(self.main_frame)
        button_frame.pack(pady=10)
        
        play_again_button = tk.Button(button_frame, text="Play Again", font=("Arial", 12), command=self.displayMenu)
        play_again_button.pack(side="left", padx=10, ipadx=8, ipady=3)
        
        home_button = tk.Button(button_frame, text="Home", font=("Arial", 12), command=self.showStartScreen)
        home_button.pack(side="left", padx=10, ipadx=8, ipady=3)

    def clearFrame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

# Create the application window and run the quiz
root = tk.Tk()
app = MathQuiz(root)
root.mainloop()