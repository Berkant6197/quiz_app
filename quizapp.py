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

    total_questions = len(questions)
    percentage = (score / total_questions) * 100

    print(f"\n🎯 Quiz Bitti! Doğru sayısı: {score}/{total_questions}")
    print(f"📊 Başarı Oranı: %{percentage:.2f}")

    if percentage >= 50:
        print("🥳 Tebrikler, başarılı oldunuz!")
    else:
        print("😢 Üzgünüz, başarısız oldunuz. Tekrar deneyin!")

if __name__ == "__main__":
    run_quiz()
