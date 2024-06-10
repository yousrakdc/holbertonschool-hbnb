from app.models.user import User

class UserService:

    @staticmethod
    def create_user(data):
        email = data.get('email')
        if not email or '@' not in email:
            raise ValueError("Invalid email")

        if not data.get('first_name') or not data.get('last_name'):
            raise ValueError("First name and last name are required")

        for user in User.storage.values():
            if user['email'] == email:
                raise ValueError("Email already exists")

        return User.create(data)

    @staticmethod
    def get_user(user_id):
        user = User.read(user_id)
        if not user:
            raise ValueError("User not found")
        return user

    @staticmethod
    def update_user(user_id, data):
        user = User.read(user_id)
        if not user:
            raise ValueError("User not found")

        if 'email' in data:
            email = data['email']
            if not email or '@' not in email:
                raise ValueError("Invalid email")

            for other_user in User.storage.values():
                if other_user['email'] == email and other_user['id'] != user_id:
                    raise ValueError("Email already exists")

        return User.update(user_id, data)

    @staticmethod
    def delete_user(user_id):
        user = User.delete(user_id)
        if not user:
            raise ValueError("User not found")
        return user

    @staticmethod
    def get_all_users():
        return User.all()
