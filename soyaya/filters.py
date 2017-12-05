from telegram.ext import BaseFilter

class Set_me_is_active(BaseFilter):
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def del_user(self, user):
        # the functional approach deletes all instances
        self.users = list(filter(lambda u: u != user, self.users))
        
    def filter(self, message):
        return (message.from_user.id in self.users) if \
            (message.from_user is not None) else False
