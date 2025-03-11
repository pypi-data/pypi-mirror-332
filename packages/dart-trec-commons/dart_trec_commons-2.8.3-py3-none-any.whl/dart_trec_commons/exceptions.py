class TRECException(Exception):
    """"
    Root of all exceptions related to the core business of the current application.
    Differently of Runtime Exceptions, the Business Exceptions should be predictable, catched and handled.
    They may also offer convenient application utilities, like support for i18n and serialization.
    """

    def __init__(
            self,
            message="Oh no! T-REC is angry and made an unexpected error. Bad, bad T-REC :/",
            cause: Exception = None):
        super().__init__(message)
        self.code = type(self).__name__
        self.message = message
        self.cause = cause

    def to_dict(self, ):
        response = {"code": self.code, "message": self.message}
        if self.cause:
            response["cause"] = {
                "code": type(self.cause).__name__,
                "message": str(self.cause),
            }
        return response


class NotFoundException(TRECException):
    def __init__(self, message="The resource does not exist"):
        super().__init__(message)


class IssueNotFoundException(NotFoundException):
    def __init__(self, document_id):
        super().__init__(f'The issue \'{document_id}\' does not exist.')


class TGNotFoundException(NotFoundException):
    def __init__(self, tg_id):
        super().__init__(f'The TG \'{tg_id}\' does not exist.')


class UnexpectedException(TRECException):
    def __init__(self, message="An unexpected error."):
        super().__init__(message)


class NotImplementException(TRECException):
    def __init__(self, message="This fuction is not available"):
        super().__init__(message)


class InvalidParameterException(TRECException):
    def __init__(self, name: str, value: str):
        super().__init__(
            f'The parameter "{name}" has an invalid value of "{value}')


class InvalidValueException(TRECException):
    def __init__(self, name: str, value: str, values: list):
        message = f'The parameter "{value}" has an invalid value of "{value}"'
        if values:
            message += f', but should be one of {values}'
        super().__init__(message)


class InvalidKeyException(TRECException):
    def __init__(self, message="Key is invalid in the current factory."):
        super().__init__(message)
