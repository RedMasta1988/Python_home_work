import functools

login = input("Введите login: ")


def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        if "admin" in args:
            print("На Вашем счёте 10 byn")
        else:
            print("Доступ запрещён")
        value = func(*args, **kwargs)
        return value

    return wrapper_decorator


@decorator
def new_func(name):
    return name


new_func(login)
