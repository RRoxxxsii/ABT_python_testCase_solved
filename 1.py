import os


def black_book(page: int) -> bool:
    status_code = os.system(f"./black-book -n {page}")
    return status_code == 0


def main():
    """
    Вам дали книгу, конкретное количество страниц вам не сообщили,
    но оно точно не превышает 10 000 000.
    
    Вам необходимо вычислить номер последней страницы.
    Книгу открывать нельзя - вместо этого вам выдали черный ящик, чтобы слегка усложнить задачу.
    Черному ящику (функция black_book) можно сообщить предполагаемый номер последней страницы,
    а в ответ узнать, есть ли эта страница в книге.
    
    Уточнение:
        black_book возвращает True, если страница последняя
                  возвращает False, если страница не последняя.
    
    
    Важно: написать наиболее эффективный алгоритм (по числу итераций)
    """
    last_page = None
    max_page_num = 10_000_000
    first_page = 1

    while max_page_num >= first_page:
        middle_page = (first_page + max_page_num) // 2
        if black_book(middle_page):
            last_page = middle_page
            first_page = middle_page + 1
        else:
            max_page_num = middle_page - 1

    print(last_page)


if __name__ == '__main__':
    main()

