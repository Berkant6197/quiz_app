import tkinter as tk
from tkinter import messagebox
import random
import time  
from questions import questions

timer_id = None
time_per_question = 10  
current_question_index = 0  
score = 0  
start_time = 0  
result_frame = None 

def start_quiz():
    global start_time
    name = name_entry.get().strip()
    if name:
        welcome_frame.pack_forget()  
        random.shuffle(questions)   
        start_time = time.time() 
        show_question()
    else:
        messagebox.showwarning("Eksik Bilgi", "Lütfen isminizi girin.")

def show_question():
    global timer_id
    question_frame.pack(pady=20)
    q = questions[current_question_index]
    question_label.config(
        text=f"Soru {current_question_index + 1} / {len(questions)}\n\n{q['question']}"
    )

    for i in range(4):
        option_buttons[i].config(text=q["options"][i], state=tk.NORMAL)

    start_timer(time_per_question)

def check_answer(selected_option):
    global current_question_index, score
    stop_timer()

    correct = questions[current_question_index]["answer"]
    if selected_option == correct:
        score += 1

    current_question_index += 1
    if current_question_index < len(questions):
        show_question()
    else:
        question_frame.pack_forget()
        end_time = time.time()
        elapsed_time = end_time - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        percentage = (score / len(questions)) * 100 


        show_result(score, len(questions), percentage, minutes, seconds)

  
def start_timer(seconds_left):
    global timer_id
    if seconds_left > 0:
        timer_label.config(text=f"Kalan Süre: {seconds_left} saniye")
        timer_id = window.after(1000, start_timer, seconds_left - 1)
    else:
        timer_label.config(text="Süre doldu!")
        disable_buttons()
        window.after(1000, lambda: check_answer(None))  

def stop_timer():
    global timer_id
    if timer_id is not None:
        window.after_cancel(timer_id)
        timer_id = None

def show_result(score, total, percentage, minutes, seconds):
    global result_frame
    result_frame = tk.Frame(window, bg="#f0f0f0")
    result_frame.pack(pady=40)

    result_label = tk.Label(
        result_frame,
        text=(
            f"🎯 Quiz Tamamlandı!\n\n"
            f"✅ Doğru Sayısı: {score} / {total}\n"
            f"📊 Başarı Oranı: %{percentage:.2f}\n"
            f"⏱️ Süre: {minutes} dakika {seconds} saniye"
        ),
        font=("Arial", 14),
        bg="#f0f0f0",
        justify="center"
    )
    result_label.pack(pady=10)

    retry_button = tk.Button(result_frame, text="🔁 Tekrar Dene", font=("Arial", 12), command=restart_quiz)
    retry_button.pack(pady=5)

    exit_button = tk.Button(result_frame, text="❌ Çıkış", font=("Arial", 12), command=window.destroy)
    exit_button.pack(pady=5)

def restart_quiz():
    global current_question_index, score, start_time
    current_question_index = 0
    score = 0
    start_time = 0
    result_frame.pack_forget()
    name_entry.delete(0, tk.END)
    welcome_frame.pack(pady=40)

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

timer_label = tk.Label(question_frame, text="", font=("Arial", 12), bg="#f0f0f0", fg="red")
timer_label.pack(pady=5)


option_buttons = []
options = ['A', 'B', 'C', 'D']
for opt in options:
    btn = tk.Button(question_frame, text="", font=("Arial", 12), width=40,
                    command=lambda opt=opt: check_answer(opt))
    btn.pack(pady=5)
    option_buttons.append(btn)

window.mainloop()
