from uuid import UUID
from database import users
from schemas.user import User, UserCreate, UserUpdate


class UserService:

    @staticmethod
    def get_user_by_id(user_id):
        user = users.get(str(user_id))
        if not user:
            return None
        return user

    @staticmethod
    def get_all_users():
        return users

    @staticmethod
    def create_user(user_data: UserCreate):
        user = User(id=str(UUID(int=len(users) + 1)), **user_data.model_dump())
        users[user.id] = user
        return user

    @staticmethod
    def update_user(user_id: UUID, user_data: UserUpdate):
        user = users.get(str(user_id))
        if not user:
            return None

        user.name = user_data.name
        user.email = user_data.email
        return user

    @staticmethod
    def delete_user(user_id: UUID):
        user = users.get(str(user_id))
        if not user:
            return None

        del users[user.id]
        return True


user_service = UserService()