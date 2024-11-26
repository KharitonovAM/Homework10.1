def log(filename = ''):
    '''Автоматически логирует начало и конец выполнения функции,    ее результаты или возникшие ошибки, если
    filename задан, логи записываются в указанный файл, если не задан, логи выводятся в консоль'''
    def decorator(func):
        def wrapper(*args,**kwargs):
            try:
                func(*args, **kwargs)
                result = f'{func.__name__} ok'
            except Exception as e:
                result = f'{func.__name__} error: {e}. Inputs: {args}, {kwargs}'
            if filename:
                with open(filename,'a') as f:
                    f.write(result+'\n')
            else:
                print(result)
            #return func(*args, **kwargs)
        return wrapper
    return decorator


@log('test_log.txt')
def sum(a,b):
    return a+b

z = sum(5,8)


@log('bad_test.txt')
def dived(a,b):
    return a/b

l = dived(5,1)

l = dived(5,0)

