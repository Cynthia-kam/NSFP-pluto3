from __future__ import annotations

from .user import User
from typing import List


class UserManagement:
    """Main class to manage the user accounts

    Attributes:
        users: A list of users
        status_file: file where log ins are recorded
    """

    def __init__(self, status_file: str = 'data/.logged_in', users: List[User] = []) -> None:
        self.users = users
        self.status_file = status_file

    def get_logged_in_user(self) -> User:
        """Returns the logged in user
        """
        try:
            with open(self.status_file, 'r') as f:
                logged_in_user_name = (f.readline()).strip()
                user_details = self.get_user_details(logged_in_user_name)
                if user_details:
                    return user_details
                else:
                    raise Exception(f"{logged_in_user_name} is not logged in")
        except FileNotFoundError:
            print("File not found")

    def get_user_details(self, username: str) -> User:
        """Returns the account of a user
        
        Args:
            username: the target username
        """
        for user in self.users:
            if user.username == username:
                return user

    @staticmethod
    def load(infile: str = 'data/credentials.txt') -> UserManagement:
        """Loads the accounts from a file"""
        # open the file and retrieve the relevant fields to create the objects.
        # TODO: Nothing
        with open(infile, 'r') as f:
            users = [User(elements[0], elements[3], elements[4], bool(elements[5])) for line in f.readlines() if
                     (elements := line.strip().split(':'))]
            return UserManagement(users=users)
