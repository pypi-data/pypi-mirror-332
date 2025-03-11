import inspect
from functools import wraps

providers = {}


class auto: ...


def register_provider(fn):
    global providers
    providers[fn.__annotations__["return"]] = fn
    return fn


def inject(fn):
    global providers
    signature = inspect.signature(fn)
    to_inject = {}
    arg_indexes = {}
    counter = 0
    empty_values = [auto, inspect.Parameter.empty]

    for arg_name, parameter in signature.parameters.items():
        arg_indexes[arg_name] = counter
        counter += 1

        if parameter.default in empty_values:
            if arg_name in fn.__annotations__:
                to_inject[arg_name] = fn.__annotations__[arg_name]

    @wraps(fn)
    def wrapped(*args, **kwargs):
        for arg_name, arg_type in to_inject.items():
            if arg_name not in kwargs and arg_indexes[arg_name] >= len(args):
                kwargs[arg_name] = provide(arg_type)

        return fn(*args, **kwargs)

    return wrapped


def provide(type):
    return providers[type]()
