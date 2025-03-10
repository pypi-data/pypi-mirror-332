from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError as DRFValidationError
from django.core.exceptions import ValidationError as DjangoValidationError
from .exceptions import ValidationErrorProblem


def custom_exception_handler(exc, context):
    """
    Custom exception handler that formats both DRF and Django validation errors
    into RFC 7807 Problem Details.
    """
    response = exception_handler(exc, context)

    # Handle DRF ValidationError
    if isinstance(exc, DRFValidationError):
        invalid_params = [
            {"name": key, "reason": ", ".join([str(msg) for msg in value])}
            for key, value in exc.detail.items()
        ]
        return Response(
            ValidationErrorProblem(invalid_params).get_full_details(),
            status=ValidationErrorProblem([]).status_code
        )

    # Handle Django Model ValidationError
    elif isinstance(exc, DjangoValidationError):
        if hasattr(exc, "message_dict"):  # If it's a dict of field errors
            invalid_params = [
                {"name": key, "reason": ", ".join(value)}
                for key, value in exc.message_dict.items()
            ]
        else:  # If it's a simple string error
            invalid_params = [{"name": "non_field_errors", "reason": str(exc)}]

        return Response(
            ValidationErrorProblem(invalid_params).get_full_details(),
            status=ValidationErrorProblem([]).status_code
        )

    return response
