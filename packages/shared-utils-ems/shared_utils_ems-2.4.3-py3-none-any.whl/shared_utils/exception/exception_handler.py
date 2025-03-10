from rest_framework.views import exception_handler
from rest_framework.response import Response
from django.core.exceptions import ValidationError as DjangoValidationError
from django.http import Http404
from .exceptions import (
    ValidationErrorProblem,
    UnauthorizedProblem,
    ForbiddenProblem,
    NotFoundProblem,
    ConflictProblem,
    InternalServerProblem,
)
from rest_framework.exceptions import (
    ValidationError as DRFValidationError,
    NotAuthenticated,
    PermissionDenied,
    AuthenticationFailed,
    NotFound,
)

    
def custom_exception_handler(exc, context):
    """
    Custom exception handler that formats all errors into RFC 7807 Problem Details.
    """
    response = exception_handler(exc, context)

    if isinstance(exc, Http404):
        exc = NotFound(detail="The requested resource was not found.")

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
    if isinstance(exc, DjangoValidationError):
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

        # Handle Authentication Errors
    if isinstance(exc, (NotAuthenticated, AuthenticationFailed)):
        return Response(
            UnauthorizedProblem(str(exc)).get_full_details(),
            status=UnauthorizedProblem().status_code
        )

    # Handle Permission Denied Errors
    if isinstance(exc, PermissionDenied):
        return Response(
            ForbiddenProblem(str(exc)).get_full_details(),
            status=ForbiddenProblem('').status_code
        )

    # Handle Not Found Errors (404) from DRF
    if isinstance(exc, NotFound):
        return Response(
            NotFoundProblem().get_full_details(),
            status=NotFoundProblem().status_code
        )

    # Handle Not Found Errors (404) from Django's Http404
    # if isinstance(exc, Http404):
    #     return Response(
    #         NotFoundProblem().get_full_details(),
    #         status=NotFoundProblem().status_code
    #     )

    # # Handle Resource Not Found Errors
    # if response and response.status_code == 404:
    #     return Response(
    #         NotFoundProblem(context.get("view", "resource")
    #                         ).get_full_details(),
    #         status=NotFoundProblem("").status_code
    #     )

    # Handle Conflict Errors (409)
    if response and response.status_code == 409:
        return Response(
            ConflictProblem(str(exc)).get_full_details(),
            status=ConflictProblem().status_code
        )

    # Handle Any Other Errors (500 Internal Server Errors)
    if response is None:
        return Response(
            InternalServerProblem(str(exc)).get_full_details(),
            status=InternalServerProblem().status_code
        )

    return response
