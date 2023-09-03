import functools

login = input("Введите login: ")


def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        if "admin" not in args:
            print("Доступ запрещён")
        value = func(*args, **kwargs)
        if value == "admin":
            print("На Вашем счёте 10 byn")
        return value

    return wrapper_decorator


@decorator
def new_func(name):
    return name


new_func(login)
