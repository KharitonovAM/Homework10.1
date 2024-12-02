def log(filename: str = ""):
    """Автоматически логирует начало и конец выполнения функции,    ее результаты или возникшие ошибки, если
    filename задан, логи записываются в указанный файл, если не задан, логи выводятся в консоль
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
                result = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a") as f:
                        f.write(result + "\n")
                else:
                    print(result)
                return result
            except Exception as e:
                result = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a") as f:
                        f.write(result + "\n")
                else:
                    print(result)

        return wrapper

    return decorator