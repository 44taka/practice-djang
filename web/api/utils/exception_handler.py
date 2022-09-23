from rest_framework.exceptions import server_error
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        # エラー詳細は全部出す
        response.data = {}
        response.data = exc.get_full_details()
    return response


def server_error_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is None:
        return server_error(request=context['request'])
