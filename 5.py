import os
import re


def task1():
    # в папке test найти все файлы filenames вывести количество

    """
    В случае, если под условие должны попадать файлы, строго равные 'filenames.txt',
    тогда на 21 строке вместо file = re.match(pattern, file) необходимо проводить
    проверку на равенство и на 22 строке убрать проверку на то, что файл не None, где 'file == filenames.txt'.
    Если условию удовлетворяет файл, который начинается с filenames и, например, может быть
    равен filenames gggggg.txt и т.д., то код ниже выполняет задачу.
    """
    pattern = r'^filenames.*\.txt$'

    amount = 0
    for item in os.walk('./test'):
        path, files = item[0], item[-1]
        for file in files:
            file = re.match(pattern, file)
            if file:
                amount += 1

    print(amount)


def task2():
    # в папке test найти все email адреса записанные в файлы

    email_pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    email_address_arr = []
    for item in os.walk('./test'):
        path, files = item[0], item[-1]
        for file in files:
            with open(path + '/' + file, 'r') as opened_file:
                opened_file = opened_file.read().split('\n')
                for text in opened_file:
                    email = re.match(email_pattern, text)
                    if email:
                        email_address_arr.append(email.group())
    print(*email_address_arr, sep=', ')


def main():
    task1()
    task2()
    # дополнительно: придумать над механизмом оптимизации 2-й задачи (параллелизация)


if __name__ == '__main__':
    main()
