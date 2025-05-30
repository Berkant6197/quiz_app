import tkinter as tk
from tkinter import messagebox
import random
import time
from questions import questions

# Tema tanımları
themes = {
    "light": {
        "bg": "#e0f7fa",
        "fg": "#000000",
        "button_bg": "#ffffff",
        "button_fg": "#000000",
        "active_bg": "#B2EBF2"
    },
    "dark": {
        "bg": "#000000",
        "fg": "#ffffff",
        "button_bg": "#000000",
        "button_fg": "#ffffff",
        "active_bg": "#000000"
    }
}

current_theme = "light"

timer_id = None
time_per_question = 10
current_question_index = 0
score = 0
start_time = 0
result_frame = None
skipped_questions = 0

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
    global current_question_index, score, skipped_questions
    stop_timer()

    correct = questions[current_question_index]["answer"]

    if selected_option is None:
        feedback = f"⏭️ Atlandı! Doğru cevap: {correct}"
        skipped_questions += 1
    elif selected_option == correct:
        score += 1
        feedback = "✅ Doğru!"
    else:
        feedback = f"❌ Yanlış! Doğru cevap: {correct}"

    disable_buttons()
    timer_label.config(text=feedback)
    current_question_index += 1

    if current_question_index < len(questions):
        window.after(2000, show_question)
    else:
        end_time = time.time()
        elapsed_time = end_time - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        percentage = (score / len(questions)) * 100
        window.after(2000, lambda: question_frame.pack_forget())
        window.after(2000, lambda: show_result(score, len(questions), percentage, minutes, seconds, skipped_questions))

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

def disable_buttons():
    for btn in option_buttons:
        btn.config(state=tk.DISABLED)

def show_result(score, total, percentage, minutes, seconds, skipped):
    global result_frame
    result_frame = tk.Frame(window)
    result_frame.pack(pady=40)

    result_label = tk.Label(
        result_frame,
        text=(
            f"🎯 Quiz Tamamlandı!\n\n"
            f"✅ Doğru Sayısı: {score} / {total}\n"
            f"⏭️ Boş Bırakılan: {skipped}\n"
            f"📊 Başarı Oranı: %{percentage:.2f}\n"
            f"⏱️ Süre: {minutes} dakika {seconds} saniye"
        ),
        font=("Helvetica", 14, "bold"),
        justify="center"
    )
    result_label.pack(pady=10)

    retry_button = tk.Button(result_frame, text="🔁 Tekrar Dene", font=("Arial", 12, "bold"),
                             width=20, command=restart_quiz)
    retry_button.pack(pady=5)

    exit_button = tk.Button(result_frame, text="❌ Çıkış", font=("Arial", 12, "bold"),
                            width=20, command=window.destroy)
    exit_button.pack(pady=5)
    apply_theme()

def restart_quiz():
    global current_question_index, score, start_time, skipped_questions
    current_question_index = 0
    score = 0
    start_time = 0
    skipped_questions = 0
    result_frame.pack_forget()
    name_entry.delete(0, tk.END)
    welcome_frame.pack(pady=40)

def toggle_theme():
    global current_theme
    current_theme = "dark" if current_theme == "light" else "light"
    apply_theme()

def apply_theme():
    theme = themes[current_theme]
    window.configure(bg=theme["bg"])
    welcome_frame.configure(bg=theme["bg"])
    question_frame.configure(bg=theme["bg"])
    if result_frame:
        result_frame.configure(bg=theme["bg"])

    for widget in welcome_frame.winfo_children():
        widget.configure(bg=theme["bg"], fg=theme["fg"])

    for widget in question_frame.winfo_children():
        if isinstance(widget, tk.Button):
            widget.configure(
                bg=theme["button_bg"],
                fg=theme["button_fg"],
                activebackground=theme["active_bg"]
            )
        else:
            widget.configure(bg=theme["bg"], fg=theme["fg"])

    if result_frame:
        for widget in result_frame.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(
                    bg=theme["button_bg"],
                    fg=theme["button_fg"],
                    activebackground=theme["active_bg"]
                )
            else:
                widget.configure(bg=theme["bg"], fg=theme["fg"])

window = tk.Tk()
window.title("🎓 Quiz Uygulaması")
window.geometry("550x500")

welcome_frame = tk.Frame(window)
welcome_frame.pack(pady=40)

greeting_label = tk.Label(welcome_frame, text="🎓 Quiz Uygulamasına Hoş Geldiniz!",
                          font=("Helvetica", 16, "bold"))
greeting_label.pack(pady=10)

name_label = tk.Label(welcome_frame, text="İsminizi giriniz:", font=("Arial", 12))
name_label.pack()

name_entry = tk.Entry(welcome_frame, font=("Arial", 12), width=30)
name_entry.pack(pady=10)

start_button = tk.Button(welcome_frame, text="🚀 Başla", font=("Arial", 12, "bold"),
                         width=20, command=start_quiz)
start_button.pack(pady=10)

theme_button = tk.Button(welcome_frame, text="🌓 Tema Değiştir", font=("Arial", 10),
                         command=toggle_theme)
theme_button.pack(pady=5)

question_frame = tk.Frame(window)

question_label = tk.Label(question_frame, text="", font=("Arial", 14), wraplength=450, justify="center")
question_label.pack(pady=20)

timer_label = tk.Label(question_frame, text="", font=("Arial", 12, "bold"), fg="red")
timer_label.pack(pady=5)

option_buttons = []
for _ in range(4):
for i in range(4):
    btn = tk.Button(question_frame, text="", font=("Arial", 12), width=40,
                    relief=tk.RAISED,
                    command=lambda opt=i: check_answer(option_buttons[opt]["text"]))
    btn.pack(pady=6)
    option_buttons.append(btn)

skip_button = tk.Button(question_frame, text="⏭️ Atla", font=("Arial", 12), width=20,
                        command=lambda: check_answer(None))
skip_button.pack(pady=6)

apply_theme()
window.mainloop()

