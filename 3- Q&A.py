import csv

# قائمة بالأسئلة والأجوبة
questions_and_answers = [
    {"q": "question1", "a": "answer1"},
    {"q": "question2", "a": "answer2"},
    {"q": "question3", "a": "answer3"},
    {"q": "question4", "a": "answer4"},
    {"q": "question5", "a": "answer5"},
    {"q": "question6", "a": "answer6"},
    {"q": "question7", "a": "answer7"},
    {"q": "question8", "a": "answer8"},
    {"q": "question9", "a": "answer9"},
    {"q": "question10", "a": "answer10"},
    {"q": "question11", "a": "answer11"},
    {"q": "question12", "a": "answer12"},
    {"q": "question13", "a": "answer13"},
    {"q": "question14", "a": "answer14"},
    {"q": "question15", "a": "answer15"},
    {"q": "question16", "a": "answer16"},
    {"q": "question17", "a": "answer17"},
    {"q": "question18", "a": "answer18"},
    {"q": "question19", "a": "answer19"},
    {"q": "question20", "a": "answer20"},
]

# اسم الملف
file_name = "quiz_questions.csv"

# افتح الملف للكتابة
with open(file_name, mode="w", newline="", encoding="utf-8") as file:
    # قم بإنشاء كائن writer
    writer = csv.DictWriter(file, fieldnames=["q", "a"])

    # اكتب العناوين الرئيسية للأعمدة
    writer.writeheader()

    # اكتب البيانات
    writer.writerows(questions_and_answers)

print(f"تم إنشاء ملف {file_name} بنجاح!")