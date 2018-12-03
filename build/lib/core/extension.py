# -*- coding: utf-8 -*-
import importlib
import functools

def import_ext_function(entrypoint):
    """Given a function name in the form of a setuptools entry point, try to
    dynamically load and return it

    Args:
        entrypoint (str): setuptools-style entrypoint in the form
            module.submodule:function

    Returns:
        function: function loaded from entrypoint

    """
    try:
        module, funcname = entrypoint.split(":")
    except ValueError as e:
        msg = "Expected entrypoint in the form module.submodule:function"

    try:
        module = importlib.import_module(module)
    except ImportError as e:
        msg = "Error importing module {}".format(module)

    try:
        function = getattr(module, funcname)
    except AttributeError as e:
        msg = "No function named {} in {}".format(funcname, module)


    return function

def get_wrapped_response_function(ext):
    """Wraps a ext function with arguments given in the test file

    This is similar to functools.wrap, but this makes sure that 'response' is
    always the first argument passed to the function

    Args:
        ext (dict): $ext function dict with function, extra_args, and
            extra_kwargs to pass

    Returns:
        function: Wrapped function
    """
    args = ext.get("extra_args") or ()
    kwargs = ext.get("extra_kwargs") or {}
    func = import_ext_function(ext["function"])

    @functools.wraps(func)
    def inner(response):
        return func(response, *args, **kwargs)

    inner.func = func
    return inner


def get_wrapped_create_function(ext):
    """Same as above, but don't require a response
    """
    args = ext.get("extra_args") or ()
    kwargs = ext.get("extra_kwargs") or {}
    func = import_ext_function(ext["function"])

    return func(*args, **kwargs)
