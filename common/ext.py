import importlib

def import_ext_function(entrypoint):
    """Given a function name in the form of a setuptools entry point, try to
    dynamically load and return it

    Args:
        entrypoint (str): setuptools-style entrypoint in the form
            module.submodule:function

    Returns:
        function: function loaded from entrypoint

    Raises:
        InvalidExtFunctionError: If the module or function did not exist
    """
    # logger = _getlogger()
    print entrypoint
    try:
        module, funcname = entrypoint.split(":")
    except ValueError as e:
        msg = "Expected entrypoint in the form module.submodule:function"
        print(msg)
        # logger.exception(msg)
        # raise_from(exceptions.InvalidExtFunctionError(msg), e)

    try:
        module = importlib.import_module(module)
    except ImportError as e:
        msg = "Error importing module {}".format(module)
        print(msg)
        # logger.exception(msg)
        # raise_from(exceptions.InvalidExtFunctionError(msg), e)

    try:
        function = getattr(module, funcname)
    except AttributeError as e:
        msg = "No function named {} in {}".format(funcname, module)
        print(msg)

        # logger.exception(msg)
        # raise_from(exceptions.InvalidExtFunctionError(msg), e)

    return function

if __name__ == '__main__':

# $ext:
#           function: tavern.testutils.helpers:validate_jwt
#           extra_kwargs:
#             jwt_key: "token"
#             key: CGQgaG7GYvTcpaQZqosLy4
#             options:
#               verify_signature: true
#               verify_aud: false


    data = {
        "$ext":{
            "function": "common:loadFile",
            "extra_kwargs":{
                "filename": "./api_schema/api/project/auth/login.yaml"
            }
        }

    }
    print(import_ext_function(data["$ext"]["function"]))
