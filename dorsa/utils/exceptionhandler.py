# from rest_framework.exceptions import NotFound
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    handlers = {
        'ValidationError': _handle_generic_error,
        'builtin_function_or_method': _handle_generic_error,
        'Http404': handle_404_error,
        'PermissionDenied': _handle_generic_error,
        'NotAuthenticated': _handle_generic_error,
    }

    response = exception_handler(exc, context)
    exception_class = exec.__class__.__name__
    if exception_class in handlers:
        return handlers[exception_class](exec, context, response)
    return response


def _handle_generic_error(exec, context, response):
    response.data = {
        'error': 'You dont\'t have permission to do this action'
    }
    return response


def handle_404_error(exec, context, response):
    response.data = {
        'error': 'this is my custom handler you\'r requested page does not exist'
    }
    return response
