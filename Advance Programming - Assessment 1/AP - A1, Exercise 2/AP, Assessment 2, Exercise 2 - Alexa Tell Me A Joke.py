import tkinter as tk # Tkinter Import
import random

# Def Function that Displays a Joke
def displayJoke():
    user_input = entry.get().strip().lower() # To Allow any Character/Whitespace Typing Combination of the Prompt
    if user_input == "alexa tell me a joke":
        try:
            with open("randomJokes.txt", "r") as file:
                jokes = file.readlines()
                if jokes:
                    selected_joke = random.choice(jokes).strip()
                    joke_label.config(text=selected_joke)
                else:
                    joke_label.config(text="No jokes available.") # If randomJokes file is Empty
        except FileNotFoundError:
            joke_label.config(text="Jokes file not found.") # Appear if randomJokes file is not in the Same Directory
    else:
        joke_label.config(text="Please enter the correct phrase.") # Make sure the User Enters the Proper Prompt to Run the Code

# Tkinter Window 
root = tk.Tk()
root.title("Alexa, Tell Me A Joke")
root.geometry("500x290")

# Frame Widget to Center Top Heading, Entry, and Button
frame = tk.Frame(root)
frame.pack(expand=True)

# Heading Text - "Alexa Tell Me A Joke"
heading = tk.Label(frame, text="Please enter “Alexa tell me a joke”", font=("Arial", 14))
heading.pack(pady=8)

# Entry Field - to Enter the "Alexa tell me a joke" Prompt
entry = tk.Entry(frame, font=("Arial", 12), width=30)
entry.pack(pady=8)
entry.focus()

# Button to "Tell a Joke"
joke_button = tk.Button(frame, text="Tell a Joke", command=displayJoke, font=("Arial", 12))
joke_button.pack(ipadx=7, ipady=2, pady=8)

# Label "Joke:" to let User know where Jokes will be Displayed
joke_prompt = tk.Label(frame, text="Joke:", font=("Arial", 12))
joke_prompt.pack(anchor="w", pady=8, padx=20)

# Label to Display the Joke
joke_label = tk.Label(frame, text="", font=("Arial", 12), wraplength=400, justify="left")
joke_label.pack(anchor="w", padx=20, pady=5)

# Run the Tkinter
root.mainloop()