from typing import Dict, List, Union

class Database:
    def __init__(self):
        self._users: List[Dict[str, Union[int, str, bool]]] = [
            {
                'id': 1,
                'name': 'Ivan Ivanov',
                'email': 'i.i.ivanov@mail.com',
            },
            {
                'id': 2,
                'name': 'Petr Petrov',
                'email': 'p.p.petrov@mail.com',
            }
        ]

        self._id = len(self._users)

    def get_user_by_email(self, email: str):
        for user in self._users:
            if user['email'] == email:
                return user
        return None

    def create_user(self, name: str, email: str):
        self._id += 1
        self._users.append(
            {
                'id': self._id,
                'name': name,
                'email': email,
                'activated': False
            }
        )

    def delete_user_by_email(self, email: str):
        for user in self._users:
            if user['email'] == email:
                self._users.remove(user)
                return


db = Database()