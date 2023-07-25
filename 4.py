import sys
import json


def count_questions(data: dict):

    questions_amount = 0

    rounds = data["game"]["rounds"]
    for round_data in rounds:
        questions = round_data.get("questions")
        questions_amount += len(questions)

    print(f'Количество вопросов: {questions_amount}')


def print_right_answers(data: dict):
    print('-' * 10)
    print('Вывести правильные ответы:')
    rounds = data["game"]["rounds"]
    for round_data in rounds:
        questions = round_data.get("questions")
        for question in questions:
            correct_answer = question.get("correct_answer")
            answers = question.get("answers")
            if isinstance(correct_answer, int):
                print("Правильный ответ:", answers[correct_answer])
            elif isinstance(correct_answer, list):
                correct_answers = [answers[i] for i in correct_answer]
                print("Правильные ответы:", correct_answers)
            else:
                print("Правильный ответ:", correct_answer)
    print('-' * 10)


def print_max_answer_time(data: dict):
    """
    Считается время ответа как на отдельный вопрос, так и
    время ответа в раунде в целом.
    """
    max_answer_time = 0
    for round_data in data["game"]["rounds"]:
        round_time_to_answer = round_data["settings"].get("time_to_answer", 0)
        if round_time_to_answer > max_answer_time:
            max_answer_time = round_time_to_answer

        for question_data in round_data["questions"]:
            question_time_to_answer = question_data.get("time_to_answer", 0)
            if question_time_to_answer > max_answer_time:
                max_answer_time = question_time_to_answer

    print("Максимальное время ответа раунда:", max_answer_time)


def main(filename):
    with open(filename) as f:
        data = json.load(f)  # загрузить данные из test.json файла
    count_questions(data)
    print_right_answers(data)
    print_max_answer_time(data)


if __name__ == '__main__':
    # передать имя файла из аргументов командной строки

    filename = sys.argv[1]
    main(filename)
