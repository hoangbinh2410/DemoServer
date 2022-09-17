
from contextlib import contextmanager
from datetime import datetime
from typing import Dict, Union, Tuple, Callable, Optional, Type

from django.utils.encoding import force_str
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.request import Request
from rest_framework.serializers import ModelSerializer

# from core.exceptions import InstanceTypeDoesNotExist
# from .exceptions import RequestBodyValidationException


def custom_response(res, response_code=200, response_msg='SUCCESS', msg_display=''):
    data = res
    response = {
        'data': data,
        'response_code': response_code,
        'response_msg': response_msg
    }
    if msg_display != '':
        response['msg_display'] = msg_display
    return response