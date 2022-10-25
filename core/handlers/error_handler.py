from rest_framework.response import Response
from rest_framework.views import exception_handler

from core.enums.error_enum import ErrorEnum
from core.exceptions.jwt_exception import JwtException


def custom_error_handler(exc: Exception, content: dict) -> Response:
    handlers = {
        'JwtException': _jwt_validate_error
    }

    response = exception_handler(exc, content)
    exc_class = exc.__class__.__name__

    if exc_class in handlers:
        return handlers[exc_class](exc, content)

    return response


def _jwt_validate_error(exc: JwtException, content: dict) -> Response:
    return Response(ErrorEnum.JWT.msg, ErrorEnum.JWT.code)
