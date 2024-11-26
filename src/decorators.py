def log(filename = ''):
    '''Автоматически логирует начало и конец выполнения функции,    ее результаты или возникшие ошибки, если
    filename задан, логи записываются в указанный файл, если не задан, логи выводятся в консоль'''
    def decorator(func):
        def wrapper(*args,**kwargs):
            try:
                func(*args, **kwargs)
                result = f'{func.__name__} ok'
            except Exception as e:
                x = arg_func()
                a, k = (x[0] if len(x) else []), (x[1] if len(x) > 1 else {})
                result = f'{func.__name__} error: {e}. Inputs: {a}, {k}'
            if filename:
                with open(filename,'a') as f:
                    f.write(result)
            else:
                print(result)
        return wrapper
    return decorator
