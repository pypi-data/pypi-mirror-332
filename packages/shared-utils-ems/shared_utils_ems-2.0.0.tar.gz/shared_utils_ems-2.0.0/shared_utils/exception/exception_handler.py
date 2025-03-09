from rest_framework.views import exception_handler
from .exceptions import Problem


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if isinstance(exc, Problem):
            response.data = exc.get_full_details()

        response["Content-Type"] = "application/problem+json"
        response["Content-Language"] = "en"

    return response
