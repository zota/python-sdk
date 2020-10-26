# pylint: disable=missing-module-docstring
from zotapaysdk.exceptions import MGException


def default_validation_function(param_name, param_value, max_size, required):
    """
    Performs the general validation as defined by ZotaPay's API

    Args:
        param_value:
        param_name:
        max_size: the max expected size as per the API
        required: whether the parameter is requried

    Returns: a boolean value showing if the parameter passed validation

    """
    if param_name is None:
        raise MGException("param_name cannot be None.")
    if param_value is None and required:
        return False

    if param_value and len(param_value) > max_size:
        return False

    return True
