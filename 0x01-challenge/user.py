#!/usr/bin/python3
""" User class """


class User():
    """ define class user """

    def __init__(self):
        """ initiation """
        self.__email = None

    @property
    def email(self):
        """ property """
        return self.__email

    @email.setter
    def email(self, value):
        """ email setter """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
