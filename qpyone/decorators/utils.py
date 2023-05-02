import contextlib
import inspect
import os


def get_class_that_defined_method(fun):
    """
    Tries to find the class that defined the specified method. Will not work for nested classes
    (locals).

    Args:
        fun: Function / Method

    Returns:
        Returns the class which defines the given method / function.
    """
    if inspect.ismethod(fun):
        for cls in inspect.getmro(fun.__self__.__class__):
            if cls.__dict__.get(fun.__name__) is fun:
                return cls
        fun = fun.__func__  # fallback to __qualname__ parsing
    if inspect.isfunction(fun):
        cls = getattr(
            inspect.getmodule(fun),
            fun.__qualname__.split(".<locals>", 1)[0].rsplit(".", 1)[0],
            None,
        )
        if isinstance(cls, type):
            return cls
    return getattr(fun, "__objclass__", None)


def get_field_mro(cls, field_name):
    """Goes up the mro and looks for the specified field."""
    res = set()
    if hasattr(cls, "__mro__"):
        for _class in inspect.getmro(cls):
            values_ = getattr(_class, field_name, None)
            if values_ is not None:
                res = res.union(set(make_list(values_)))
    return res


def make_list(item_or_items):
    """
    Makes a list out of the given items.
    Examples:
        >>> make_list(1)
        [1]
        >>> make_list('str')
        ['str']
        >>> make_list(('i', 'am', 'a', 'tuple'))
        ['i', 'am', 'a', 'tuple']
        >>> print(make_list(None))
        None
        >>> # An instance of lists is unchanged
        >>> l = ['i', 'am', 'a', 'list']
        >>> l_res = make_list(l)
        >>> l_res
        ['i', 'am', 'a', 'list']
        >>> l_res is l
        True

    Args:
        item_or_items: A single value or an iterable.
    Returns:
        Returns the given argument as an list.
    """
    if item_or_items is None:
        return None
    if isinstance(item_or_items, list):
        return item_or_items
    if hasattr(item_or_items, "__iter__") and not isinstance(item_or_items, str):
        return list(item_or_items)
    return [item_or_items]


@contextlib.contextmanager
def modified_environ(*remove, **update):
    """
    Temporarily updates the `os.environ` dictionary in-place and resets it to the original state
    when finished.
    The `os.environ` dictionary is updated in-place so that the modification is sure to work in
    all situations.

    Args:
        remove: Environment variables to remove.
        update: Dictionary of environment variables and values to add/update.

    Examples:
        >>> with modified_environ(Test='abc'):
        ...     import os
        ...     print(os.environ.get('Test'))
        abc
        >>> print(os.environ.get('Test'))
        None
    """
    env = os.environ
    update = update or {}
    remove = remove or []

    # List of environment variables being updated or removed.
    stomped = (set(update.keys()) | set(remove)) & set(env.keys())
    # Environment variables and values to restore on exit.
    update_after = {k: env[k] for k in stomped}
    # Environment variables and values to remove on exit.
    remove_after = frozenset(k for k in update if k not in env)

    try:
        env.update(update)
        [env.pop(k, None) for k in remove]  # pylint: disable=expression-not-assigned
        yield
    finally:
        env.update(update_after)
        [env.pop(k) for k in remove_after]  # pylint: disable=expression-not-assigned


def auto_str(__repr__=False):
    """
    Use this decorator to auto implement __str__() and optionally __repr__() methods on classes.

    Args:
        __repr__ (bool): If set to true, the decorator will auto-implement the __repr__() method as
            well.

    Returns:
        callable: Decorating function.

    Note:
        There are known issues with self referencing (self.s = self). Recursion will be identified
        by the python interpreter and will do no harm, but it will actually not work.
        A eval(class.__repr__()) will obviously not work, when there are attributes that are not
        part of the __init__'s arguments.

    Example:
        >>> @auto_str(__repr__=True)
        ... class Demo(object):
        ...    def __init__(self, i=0, s="a", l=None, t=None):
        ...        self.i = i
        ...        self.s = s
        ...        self.l = l
        ...        self.t = t
        >>> dut = Demo(10, 'abc', [1, 2, 3], (1,2,3))
        >>> print(dut.__str__())
        Demo(i=10, l=[1, 2, 3], s='abc', t=(1, 2, 3))
        >>> print(eval(dut.__repr__()).__str__())
        Demo(i=10, l=[1, 2, 3], s='abc', t=(1, 2, 3))
        >>> print(dut.__repr__())
        Demo(i=10, l=[1, 2, 3], s='abc', t=(1, 2, 3))
    """

    def _decorator(cls):
        def __str__(self):
            items = [
                "{name}={value}".format(name=name, value=vars(self)[name].__repr__())
                for name in [key for key in sorted(vars(self))]
                if name not in get_field_mro(self.__class__, "__auto_str_ignore__")
            ]  # pylint: disable=bad-continuation
            return "{clazz}({items})".format(
                clazz=str(type(self).__name__), items=", ".join(items)
            )

        cls.__str__ = __str__
        if __repr__:
            cls.__repr__ = __str__

        return cls

    return _decorator


def auto_str_ignore(ignore_list):
    """
    Use this decorator to suppress any fields that should not be part of the dynamically created
    `__str__` or `__repr__` function of `auto_str`.

    Args:
        ignore_list: List or item of the fields to suppress by `auto_str`.

    Returns:
        Returns a decorator.

    Example:

        >>> @auto_str()
        ... @auto_str_ignore(["l", "d"])
        ... class Demo(object):
        ...    def __init__(self, i=0, s="a", l=None, d=None):
        ...        self.i = i
        ...        self.s = s
        ...        self.l = l
        ...        self.d = d
        >>> dut = Demo(10, 'abc', [1, 2, 3], {'a': 1, 'b': 2})
        >>> print(str(dut))
        Demo(i=10, s='abc')
    """

    def _decorator(cls):
        ignored = make_list(ignore_list)
        cls.__auto_str_ignore__ = ignored
        return cls

    return _decorator
