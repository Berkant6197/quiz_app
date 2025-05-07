from questions import questions

def run_quiz():
    print("🎓 Quiz'e Hoş Geldiniz!")
    name = input("Lütfen isminizi girin: ").strip().capitalize()
    print(f"\nHoş geldin, {name}! Quiz başlıyor...\n")

    score = 0

    for index, q in enumerate(questions):
        print(f"Soru {index + 1}: {q['question']}")
        for option in q['options']:
            print(option)
        
        while True:
            answer = input("Cevabınız (A/B/C/D): ").strip().upper()
            if answer in ['A', 'B', 'C', 'D']:
                break
            else:
                print("⚠️ Lütfen sadece A, B, C veya D giriniz.")
        
        if answer == q['answer']:
            print("✅ Doğru!\n")
            score += 1
        else:
            print(f"❌ Yanlış! Doğru cevap: {q['answer']}\n")

    total_questions = len(questions)
    percentage = (score / total_questions) * 100

    print(f"\n🎯 Quiz Bitti! {name}, doğru sayın: {score}/{total_questions}")
    print(f"📊 Başarı Oranın: %{percentage:.2f}")

    if percentage >= 80:
        print(f"🏆 Harika iş çıkardın, {name}!")
    elif percentage >= 50:
        print(f"🙂 Tebrikler {name}, başarılı oldun!")
    else:
        print(f"😢 Üzgünüz {name}, başarısız oldun. Daha iyi yapabilirsin!")

if __name__ == "__main__":
    run_quiz()

