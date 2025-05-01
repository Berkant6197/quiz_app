from questions import questions

def run_quiz():
    print("Hoş geldiniz! Quiz başlıyor...\n")

    for i, q in enumerate(questions, 1):
        print(f"Soru {i}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Cevabınız (A, B, C, D): ")
        if answer.upper() == q['answer']:
            print("✅ Doğru!\n")
        else:
            print("❌ Yanlış.\n")

if __name__ == "__main__":
    run_quiz()