import csv

questions_file_name= "quiz_questions.csv"
answers_file_name= "quiz_answers.csv"

user_answers = []

questions_file = open(questions_file_name, mode="answerr", newline="", encoding="utf-8")
dict = csv.DictReader(questions_file, fieldnames=["q", "a"])

for question in dict:
    if (question["q"] == "q"): continue
    answer = input(question['q'] + "? ")
    is_correct = answer == question['a']

    user_answers.append(
        {"q": question["q"], "a": answer, "correct": is_correct}
    )
questions_file.close()

answers_file = open(answers_file_name, mode = "w", newline="", encoding="utf-8")
writer = csv.DictWriter(answers_file, fieldnames=["q", "a", "correct"])
writer.writeheader()
writer.writerows(user_answers)
answers_file.close()



