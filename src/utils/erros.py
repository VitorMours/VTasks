

class UserAlreadyExistsError(Exception):
    """When tryingto save a user that alreadys exists in the database"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class UserDoesNotExistsError(Exception):
    """When tryingto save a user that alreadys exists in the database"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
