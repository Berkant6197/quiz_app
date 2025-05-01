from questions import questions

def run_quiz():
    print("🎓 Quiz'e Hoş Geldiniz!")
    score = 0

    for index, q in enumerate(questions):
        print(f"\nSoru {index + 1}: {q['question']}")
        for option in q['options']:
            print(option)
        
        answer = input("Cevabınız (A/B/C/D): ").strip().upper()
        
        if answer == q['answer']:
            print("✅ Doğru!")
            score += 1
        else:
            print(f"❌ Yanlış! Doğru cevap: {q['answer']}")

    print(f"\nQuiz bitti. Toplam skorunuz: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()
