import httpx


class APIExceptions(Exception):
    ERROR_CODE_MAP = {}

    def __init__(self, message: str, status_code: int, error_code: str, timestamp: str):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        self.timestamp = timestamp

    @classmethod
    def from_response(cls, response: httpx.Response):
        error_data = response.json()
        error_code = error_data.get("error_code", "UKNOWN_ERROR")
        status_code = response.status_code
        timestamp = error_data.get("timestamp", "Unknown timestamp")
        message = error_data.get("message", "Unknown error")

        exception_class = cls.ERROR_CODE_MAP.get(error_code, cls)

        return exception_class(
            message=message,
            status_code=status_code,
            timestamp=timestamp,
            error_code=error_code,
        )

    @classmethod
    def register(cls, error_code: str):
        def decorator(exception_class):
            cls.ERROR_CODE_MAP[error_code] = exception_class
            return exception_class

        return decorator


@APIExceptions.register("AMOUNT_NEGATIVE")
class AmountNegativeError(APIExceptions):
    pass


@APIExceptions.register("INSUFFICIENT_FUNDS")
class InsufficientFundsError(APIExceptions):
    pass


@APIExceptions.register("USER_DOES_NOT_EXIST")
class UserDoesNotExistError(APIExceptions):
    pass


@APIExceptions.register("CREDIT_EXPIRED")
class CreditExpiredError(APIExceptions):
    pass


@APIExceptions.register("ACTIVE_CYCLE_EXISTS")
class ExistingActiveCycleError(APIExceptions):
    pass


@APIExceptions.register("NO_ACTIVE_CYCLE")
class NoActiveCycleError(APIExceptions):
    pass
