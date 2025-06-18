

class UserAlreadyExistsError(Exception):
    """When trying to save a user that alreadys exists in the database"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class UserDoesNotExistsError(Exception):
    """When the user does not exists in the database"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)



class IncorrectCredentialsToLoginError(Exception):
    """When used the incorrect credentials to log in the site"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
