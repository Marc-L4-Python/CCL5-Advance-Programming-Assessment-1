import tkinter as tk
from tkinter import ttk

# Open, Read, and Import Student Record Data
def read_student_data():
    try:
        with open("studentMarks.txt", "r") as file:
            students = []
            for line in file:
                data = line.strip().split(", ") # Gathering the Data from the Text File
                student_id = int(data[0])
                name = data[1]
                coursework_marks = list(map(int, data[2:5]))
                exam_mark = int(data[5])
                total_coursework = sum(coursework_marks)
                percentage = ((total_coursework + exam_mark) / 160) * 100 # Percentage Calculation/Equation
                grade = (
                    'A' if percentage >= 70 else # Grading System based off of Percentage Score
                    'B' if percentage >= 60 else
                    'C' if percentage >= 50 else
                    'D' if percentage >= 40 else 'F'
                )
                students.append({                       # To Organize the Data Gathered and Display them in their Respective Categories/Labels 
                    "id": student_id,                       # Student ID/Number/Code
                    "name": name,                           # Student Name
                    "coursework": total_coursework,         # Coursework Marks
                    "exam": exam_mark,                      # Examination Marks
                    "percentage": percentage,               # Percentage
                    "grade": grade                          # Grade
                })
            return students
    except FileNotFoundError: # Error Handling
        return []

# Display Function to Display Student Records in Text Area
def display_records(records):
    txtarea.delete("1.0", tk.END)
    header = f"{'#':<5}{'Name':<20}{'Code':<8}{'C. Work':<12}{'Exam':<10}{'Perc.':<10}{'Grade':<5}\n"
    txtarea.insert(tk.END, header)
    txtarea.insert(tk.END, f"{'-'*74}\n")  # Match the width of the display area
    for i, record in enumerate(records, start=1):
        txtarea.insert(
            tk.END,
            f"{i:<5}{record['name']:<20}{record['id']:<8}{record['coursework']:<12}"
            f"{record['exam']:<10}{record['percentage']:.2f}%{'':<5}{record['grade']}\n"
        )

# View All Student Records - Four (4) Different Sorting Options (Additional Challenge - Challenge 5 - from Assessment Brief)
def view_all_students():
    sort_option = sort_menu.get()
    if sort_option == "Alphabetical - A-Z":
        sorted_students = sorted(student_data, key=lambda x: x["name"])
    elif sort_option == "Alphabetical - Z-A":
        sorted_students = sorted(student_data, key=lambda x: x["name"], reverse=True)
    elif sort_option == "Highest Scores":
        sorted_students = sorted(student_data, key=lambda x: (x["coursework"], x["exam"], x["percentage"]), reverse=True)
    elif sort_option == "Lowest Scores":
        sorted_students = sorted(student_data, key=lambda x: (x["coursework"], x["exam"], x["percentage"]))
    else:
        sorted_students = student_data
    display_records(sorted_students)

def show_highest_score(): # Show All Student Records from Highest to Lowest
    highest = max(student_data, key=lambda x: (x["coursework"], x["exam"], x["percentage"]))
    display_records([highest])

def show_lowest_score(): # Show All Student Records from Lowest to Highest
    lowest = min(student_data, key=lambda x: (x["coursework"], x["exam"], x["percentage"]))
    display_records([lowest])

def view_individual_student(event): # Show/View Individual Student Record/Information
    selected_name = individual_menu.get()
    student = next((s for s in student_data if s["name"] == selected_name), None)
    if student:
        display_records([student])

# Tkinter Window
root = tk.Tk()
root.geometry("650x420")
root.title("Student Manager")

# Heading Text of Tkinter Window
heading = tk.Label(root, text="Student Manager", font=("Arial", 16, "bold"))
heading.pack(pady=12)

# All Buttons inside Tkinter
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)

btn_view_all = tk.Button(frame_buttons, text="View All Student Records", command=view_all_students, font=("Arial", 10))
btn_view_all.pack(side=tk.LEFT, padx=5)

btn_highest = tk.Button(frame_buttons, text="Show Highest Score", command=show_highest_score, font=("Arial", 10))
btn_highest.pack(side=tk.LEFT, padx=5)

btn_lowest = tk.Button(frame_buttons, text="Show Lowest Score", command=show_lowest_score, font=("Arial", 10))
btn_lowest.pack(side=tk.LEFT, padx=5)

# Sorting Dropdown Menu
sort_menu = ttk.Combobox(frame_buttons, values=[
    "Alphabetical - A-Z", "Alphabetical - Z-A", "Highest Scores", "Lowest Scores"
])
sort_menu.set("Alphabetical - A-Z")
sort_menu.pack(side=tk.LEFT, padx=5)

# View Individual Student Record User Interface
frame_individual = tk.Frame(root)
frame_individual.pack(pady=10)

lbl_individual = tk.Label(frame_individual, text="View Individual Student Record:", font=("Arial", 10, "bold"))
lbl_individual.pack(side=tk.LEFT, padx=5, pady=5)

individual_menu = ttk.Combobox(frame_individual, values=[])
individual_menu.pack(side=tk.LEFT, padx=5)
individual_menu.bind("<<ComboboxSelected>>", view_individual_student)

# Text Area for the Student Records/Information
txtarea = tk.Text(root, width=74, height=15, font=("Courier", 10))
txtarea.pack(pady=14)

# To Load Student Data
student_data = read_student_data()
individual_menu["values"] = [student["name"] for student in student_data]

root.mainloop()