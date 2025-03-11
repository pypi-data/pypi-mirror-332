class JKitError(Exception):
    pass


class InvalidIdentifierError(JKitError):
    pass


class RatelimitError(JKitError):
    pass


class ValidationError(JKitError):
    pass


class APIUnsupportedError(JKitError):
    pass


class ResourceUnavailableError(JKitError):
    pass


class CredentialError(JKitError):
    pass


class InvalidCredentialError(JKitError):
    pass


class ExpiredCredentialError(JKitError):
    pass


class AssetsActionError(JKitError):
    pass


class BalanceNotEnoughError(AssetsActionError):
    pass


class WeeklyConvertLimitExceededError(AssetsActionError):
    pass
