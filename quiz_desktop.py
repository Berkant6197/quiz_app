import tkinter as tk
from tkinter import messagebox

def start_quiz():
    name = name_entry.get().strip()
    if name:
        messagebox.showinfo("Quiz Başlıyor", f"Hoş geldin, {name}! Quiz başlıyor...")
        # Burada sonraki adımlarda quiz ekranına geçiş yapılabilir
    else:
        messagebox.showwarning("Eksik Bilgi", "Lütfen isminizi girin.")

window = tk.Tk()
window.title("Quiz Uygulaması")        
window.geometry("400x300")            
window.configure(bg="#f0f0f0")         

greeting_label = tk.Label(window, text="🎓 Quiz Uygulamasına Hoş Geldiniz!", font=("Arial", 14), bg="#f0f0f0")
greeting_label.pack(pady=20)

name_label = tk.Label(window, text="İsminizi giriniz:", font=("Arial", 12), bg="#f0f0f0")
name_label.pack()


name_entry = tk.Entry(window, font=("Arial", 12))
name_entry.pack(pady=10)

start_button = tk.Button(window, text="Başla", font=("Arial", 12), command=start_quiz)
start_button.pack(pady=10)

window.mainloop()
