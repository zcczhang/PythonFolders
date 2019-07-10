"""
    Class PasswordTool
"""

from easygui import*


class PasswordTool:
    def __init__(self, pw):
        self.password = pw
        self.strength_level = 0

    def process_password(self):
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            msgbox('Password is too short!')

        if self.check_number_exist():
            self.strength_level += 1
        else:
            msgbox('Password needs number included！')

        if self.check_letter_exist():
            self.strength_level += 1
        else:
            msgbox('Password needs letter included')

    def check_number_exist(self):
        for c in self.password:
            if c.isnumeric():
                return True
        return False

    def check_letter_exist(self):
        return (c.isalpha() for c in self.password)
        # # for c in self.password:
        # #     if c.isalpha():
        # #         return True
        # return False
