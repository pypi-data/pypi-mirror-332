# from rest_framework.views import exception_handler
# from .exceptions import Problem

from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .exceptions import ValidationErrorProblem

# def custom_exception_handler(exc, context):
#     response = exception_handler(exc, context)

#     if response is not None:
#         if isinstance(exc, Problem):
#             response.data = exc.get_full_details()

#         response["Content-Type"] = "application/problem+json"
#         response["Content-Language"] = "en"

#     return response

def custom_exception_handler(exc, context):
    """
    Custom exception handler that formats validation errors into RFC 7807 Problem Details.
    """
    response = exception_handler(exc, context)

    # Convert DRF ValidationError to our ValidationErrorProblem
    if isinstance(exc, ValidationError):
        # Convert DRF error format to a list of invalid params
        invalid_params = [
            {"name": key, "reason": ", ".join([str(msg) for msg in value])}
            for key, value in exc.detail.items()
        ]

        return Response(
            ValidationErrorProblem(invalid_params).get_full_details(),
            status=ValidationErrorProblem().status_code
        )

    return response
