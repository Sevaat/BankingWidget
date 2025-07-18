import typing


def log(filename: str = "") -> typing.Any:
    """
    Декоратор для логирования функции
    :param filename: наименование файла для записи лога, иначе вывод лога в консоль
    :return: результат работы функции
    """

    def log_decorator(func: typing.Any) -> typing.Any:
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> typing.Any:
            func_log = f"{func.__name__}"
            try:
                result = func(*args, **kwargs)  # Вызов исходной функции
                func_log = f"{func_log} ok"
                return result
            except Exception as e:
                func_log = f"{func_log} error: {str(e)}. Inputs: {args}, {kwargs}"
            finally:
                if filename != "":
                    with open(filename, "w") as file:
                        file.write(func_log)
                else:
                    print(func_log)

        return wrapper

    return log_decorator
