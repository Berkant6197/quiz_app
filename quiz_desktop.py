import tkinter as tk
from tkinter import messagebox
import random
from questions import questions  

current_question_index = 0  
score = 0  # Skor

def start_quiz():
    name = name_entry.get().strip()
    if name:
        welcome_frame.pack_forget()  
        random.shuffle(questions)   
        show_question()
    else:
        messagebox.showwarning("Eksik Bilgi", "Lütfen isminizi girin.")

def show_question():
    question_frame.pack(pady=20)
    q = questions[current_question_index]
    question_label.config(text=q["question"])
    for i in range(4):
        option_buttons[i].config(text=q["options"][i], state=tk.NORMAL)

def check_answer(selected_option):
    global current_question_index, score

    correct = questions[current_question_index]["answer"]
    if selected_option == correct:
        score += 1

    current_question_index += 1
    if current_question_index < len(questions):
        show_question()
    else:
        question_frame.pack_forget()
        messagebox.showinfo("Quiz Bitti", f"Quiz tamamlandı! Doğru sayısı: {score}/{len(questions)}")

window = tk.Tk()
window.title("Quiz Uygulaması")        
window.geometry("500x400")            
window.configure(bg="#f0f0f0")         

welcome_frame = tk.Frame(window, bg="#f0f0f0")
welcome_frame.pack(pady=40)

greeting_label = tk.Label(welcome_frame, text="🎓 Quiz Uygulamasına Hoş Geldiniz!", font=("Arial", 14), bg="#f0f0f0")
greeting_label.pack(pady=10)

name_label = tk.Label(welcome_frame, text="İsminizi giriniz:", font=("Arial", 12), bg="#f0f0f0")
name_label.pack()

name_entry = tk.Entry(welcome_frame, font=("Arial", 12))
name_entry.pack(pady=10)

start_button = tk.Button(welcome_frame, text="Başla", font=("Arial", 12), command=start_quiz)
start_button.pack(pady=10)

question_frame = tk.Frame(window, bg="#f0f0f0")

question_label = tk.Label(question_frame, text="", font=("Arial", 14), wraplength=400, bg="#f0f0f0")
question_label.pack(pady=20)

option_buttons = []
options = ['A', 'B', 'C', 'D']
for opt in options:
    btn = tk.Button(question_frame, text="", font=("Arial", 12), width=40,
                    command=lambda opt=opt: check_answer(opt))
    btn.pack(pady=5)
    option_buttons.append(btn)

window.mainloop()
