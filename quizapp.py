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
        
<<<<<<< HEAD
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
=======
        answer = input("Cevabınız (A/B/C/D): ").strip().upper()
        
        if answer == q['answer']:
            print("✅ Doğru!")
            score += 1
        else:
            print(f"❌ Yanlış! Doğru cevap: {q['answer']}")
>>>>>>> 0f26d0fb4733df3768dd118881afdb8395f510f9

    total_questions = len(questions)
    percentage = (score / total_questions) * 100

    print(f"\n🎯 Quiz Bitti! {name}, doğru sayın: {score}/{total_questions}")
    print(f"📊 Başarı Oranın: %{percentage:.2f}")

<<<<<<< HEAD
    if percentage >= 80:
        print(f"🏆 Harika iş çıkardın, {name}!")
    elif percentage >= 50:
        print(f"🙂 Tebrikler {name}, başarılı oldun!")
=======
    if percentage >= 50:
        print(f"🥳 Tebrikler {name}, başarılı oldun!")
>>>>>>> 0f26d0fb4733df3768dd118881afdb8395f510f9
    else:
        print(f"😢 Üzgünüz {name}, başarısız oldun. Daha iyi yapabilirsin!")

if __name__ == "__main__":
    run_quiz()
<<<<<<< HEAD

=======
>>>>>>> 0f26d0fb4733df3768dd118881afdb8395f510f9
