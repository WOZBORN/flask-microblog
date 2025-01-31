# Decorator test


def save_result_in_txt(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("result.txt", "a", encoding="utf-8") as file:
            file.write(f"Результат функции {func.__name__} = {result}\n")
        return result
    return wrapper


def print_result(func):
    def wrapper(*args, **kwargs):
        print(f"Функция {func.__name__} была вызвана")
        result = func(*args, **kwargs)
        print(f"Результат функции {func.__name__} = {result}")
        return result
    return wrapper



@print_result
@save_result_in_txt
def circle_area(r: int|float):
    return 3.14 * r * r


@print_result
def square_area(a: int|float):
    return a * a


@print_result
def rectangle_area(a: int|float, b: int|float):
    return a * b


circle_area(5)
square_area(5)
rectangle_area(5, 10)

