import os
import typing


def log(filename: str = "") -> typing.Any:
    def log_decorator(func: typing.Any) -> typing.Any:
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> None:
            func_log = f"{func.__name__}"
            try:
                func(*args, **kwargs)  # Вызов исходной функции
                func_log = f"{func_log} ok"
            except Exception as e:
                func_log = f"{func_log} error: {str(e)}. Inputs: {args}, {kwargs}"
            finally:
                if os.path.isfile(filename):
                    with open(filename, "w") as file:
                        file.write(func_log)
                else:
                    print(func_log)

        return wrapper

    return log_decorator
