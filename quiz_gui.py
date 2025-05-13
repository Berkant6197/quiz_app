import tkinter as tk

window = tk.Tk()
window.title("Quiz Uygulaması")        
window.geometry("400x300")            
window.configure(bg="#f0f0f0")         

greeting_label = tk.Label(window, text="🎓 Quiz Uygulamasına Hoş Geldiniz!", font=("Arial", 14), bg="#f0f0f0")
greeting_label.pack(pady=40)

window.mainloop()
