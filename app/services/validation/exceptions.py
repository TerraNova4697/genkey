

class ValidationException(Exception):
    """Raises when type is incorrect
    """
    pass


class ItemNotFound(Exception):
    """Raises when item was not found in DB.
    """
    pass
