from zotapaysdk.mg_requests.validation import default_validation_function


class MGRequestParam:
    """
    Helper object. A representation of the API argument. Takes care of
    the logic for all the different criteria there is for the param.
    """
    def __init__(self, param_name,
                 param_value,
                 max_size,
                 required,
                 assert_function=default_validation_function):
        self._param_name = param_name
        self._param_value = param_value
        self._max_size = max_size
        self._required = required
        self._assert_function = assert_function

    @property
    def param_name(self):
        """
        Getter for the param name.

        Returns:

        """
        return self._param_name

    @property
    def param_value(self):
        """
        Getter for the param value.

        Returns:

        """
        return self._param_value

    def set_value(self, value):
        """
        Setter for the param value.
        Args:
            value:

        Returns:

        """
        self._param_value = value

    @property
    def max_size(self):
        """
        Getter for the max size.

        Returns:

        """
        return self._max_size

    @property
    def required(self):
        """
        Getter for the required flag.

        Returns:

        """
        return self._required

    def validate(self):
        """
        Carries out the validation of the parameters.
        Goes over all parameters and calls their validation functions.

        Returns:

        """
        validation_result = self._assert_function(self._param_name,
                                                  self._param_value,
                                                  self._max_size,
                                                  self._required)
        validation_message = "{} passed validation".format(str(self._param_name))
        if not validation_result:
            validation_message = "{} failed validation".format(str(self._param_name))
        return validation_result, validation_message


class ArgRequestPair:
    """
    Helper object for mapping between the arg_name as expected by Python's syntax
    and the parameter name as expected by the API.
    """
    def __init__(self, arg_name, request_param_name):
        self.__arg_name = arg_name
        self.__request_param_name = request_param_name

    @property
    def arg_name(self):
        """
        Getter for the argument name.

        Returns:

        """
        return self.__arg_name

    @property
    def request_param_name(self):
        """
        Getter for the request param name.

        Returns:

        """
        return self.__request_param_name
