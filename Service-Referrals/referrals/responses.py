from rest_framework.response import Response
from logging import getLogger
logger = getLogger(__name__)

#------------------------------------------------------------------------------

def CREATED(serializer=None, data=None, *args, **kwargs):
    assert not (serializer and data)
    # 201 RESPONSE: CREATED
    response = Response(status_code=201)
    if serializer:
        response.data = serializer.data
    elif data:
        response.data = data
    return response