data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu",
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine",
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977",
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker",
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader",
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee",
    },
]


wrong_answers = []


def ask_question():
    for task in data:
        print(task["question"])
        answer = input("input answer: ")
        if answer != task["answer"]:
            wrong_answers.append(task | {"user_answer": answer})


def display_information():
    print(
        f"\ncorrect: {len(data) - len(wrong_answers)}\nincorrect: {len(wrong_answers)}\n"
    )


def display_wrong_answers():
    for answer in wrong_answers:
        print(
            f"question: {answer['question']}\n"
            f"answer: {answer['answer']}\n"
            f"your answer: {answer['user_answer']}\n"
        )
    if len(wrong_answers) > 3:
        print("you have more than 3 wrong answers. try again...")


def main():
    ask_question()
    display_information()
    display_wrong_answers()


if __name__ == "__main__":
    main()
