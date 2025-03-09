""" Tracing utilities """

import sys
import logging
import functools

total_indent = 0

DEFAULT_INDENTATION = 2

logger = logging.getLogger(__name__)


class Indentation:
    """Indentation context manager"""

    def __init__(self, increment=DEFAULT_INDENTATION):
        self.increment = increment

    def __enter__(self):
        global total_indent
        total_indent += self.increment
        return self

    def __exit__(self, *exc_info):
        global total_indent
        total_indent -= self.increment
        return None


def print_trace(*args):
    """prints trace with indentation"""
    if total_indent > 0:
        print(" " * total_indent, end="")
    print(*args)


def trace_method(func):
    """wraps func to print trace"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print_trace(func.__name__, args, kwargs)
        with Indentation():
            result = func(*args, **kwargs)
        print_trace(func.__name__, "->", repr(result))
        return result

    return wrapper


def trace_class(cls):
    """wraps all methods of class to print trace"""

    def __getattribute__(self, item):
        result = object.__getattribute__(self, item)
        if callable(result):
            result = trace_method(result)
        return result

    cls.__getattribute__ = __getattribute__

    return cls


class CallTracer:
    """Traces calls to functions and methods"""

    def __init__(self, register=True):
        self.include_classes = tuple()
        self.include_objects = tuple()
        self.include_names = tuple()

        if register:
            self.register()

    def register(self):
        sys.settrace(self)

    def unregister(self):
        sys.settrace(None)

    def trace(self, obj):
        if isinstance(obj, str):
            logger.info("trace name %s", obj)
            self.include_names += (obj,)

        elif isinstance(obj, type):
            logger.info("trace class %s", obj.__name__)
            self.include_classes += (obj,)

        elif callable(obj) and hasattr(obj, "__name__"):
            logger.info("trace name %s", obj.__name__)
            self.include_names += (obj.__name__,)

        else:
            logger.info("trace object %s", id(obj))
            self.include_objects += (id(obj),)

    def qualify(self, frame):
        code = frame.f_code
        name = code.co_name

        if name in self.include_names:
            return True

        target = frame.f_locals.get("self", None)

        if target is None:
            return False

        if id(target) in self.include_objects:
            return True

        if isinstance(target, self.include_classes):
            return True

    def __call__(self, frame, event, result):
        code = frame.f_code
        name = code.co_name

        if event not in ("call", "return"):
            return

        if event == "call" and not self.qualify(frame):
            return

        kwargs = {k: frame.f_locals[k] for k in code.co_varnames if k in frame.f_locals}

        global total_indent

        if event == "call":
            print_trace(name, kwargs)
            total_indent += DEFAULT_INDENTATION
        elif event == "return":
            total_indent -= DEFAULT_INDENTATION
            print_trace(name, "->", repr(result))

        if event == "call":
            # return self to trace other events within the frame
            # same as frame.f_trace = self
            return self

        return
