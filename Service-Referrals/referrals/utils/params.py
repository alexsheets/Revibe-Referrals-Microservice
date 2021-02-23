"""
Multiple functions for obtaining and viewing parameters of requests
"""

#------------------------------------------------------------------------------

def get_url_param(params, var, default=None, type_=None, *args, **kwargs):
    """
    Grabs url params to register users and use referral system.
    """
    def perform_get_url_param(params, var, *args, **kwargs):
        param = params.get(var, None)
        if param == None:
            return None
        
        if type(param) == list:
            if len(param) > 1:
                return param
            else:
                param = param[0]
            
            return param
    
    result = perform_get_url_param(params, var, *args, **kwargs)

    # check for default, else specify
    if default != None and result == None:
        result = default
    
    if type_ != None:
        try:
            result = type_(result)
        except Exception:
            pass
    
    return result

def convert_param_to_bool(params, var, default=None, *args, **kwargs):
    # to validate arguments bool must be True or False
    if default != None:
        assert bool(default) in [True, False]
    # get params
    param = get_url_param(params, var, *args, **kwargs)
    # if the parameter is none...
    if param == None:
        return default if default != None else False
    elif isinstance(param, list):
        return True
    
    # validate HERE that parameter is currently a boolean instance [True, False]
    if isinstance(param, int):
        return bool(param)
    
    # finally, convert the strings to boolean values
    if isinstance(param, str):
        param = param.lower()
        if param in ['true', 't']:
            return True
        elif param in ['false', 'f']:
            return False
    
    # return nothing if necessary
    if default != None:
        return bool(default)
    else:
        return None


def get_request_header(request, header_name, default=None):
    # get meta value of headers
    headers = request.META
    # use get request on headers to get the request header
    header = headers.get(header_name, default)
    # return values
    return header