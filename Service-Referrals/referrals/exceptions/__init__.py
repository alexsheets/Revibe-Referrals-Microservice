from rest_framework.exceptions import APIException
from rest_framework.status import *

# -----------------------------------------------------------------------------

# 2xx Errors

# 3xx Errors

# 4xx Errors
class BadRequestError(APIException):
    # 400 BAD REQUEST
    status_code = 400
    default_detail = "Bad request exception occurred."
    default_code = 'bad_request'

class NotFoundError(APIException):
    # 404 NOT FOUND
    status_code = 404
    default_detail = "Couldn't find specified resource."
    default_code = 'not_found'

class ConflictError(APIException):
    # 409 CONFLICT
    status_code = 409
    default_detail = "Data conflict occurred. Try again."
    default_code = 'conflict'

# 5xx Errors
class BadEnvironmentError(APIException):
    # 503 SERVICE UNAVAILABLE
    status_code = 503
    default_detail = "The request cannot be made in the current environment."
    default_code = "bad_environment"

class ProgramError(APIException):
    # 512 PROGRAM ERROR
    status_code = 512
    default_detail = "Server error, please try again later."
    default_code = 'program_error'