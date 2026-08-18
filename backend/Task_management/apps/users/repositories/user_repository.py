from ..models import User

class UserRepository():

    @staticmethod
    def get_employee_by_id(user_id):
        return User.objects.filter(id = user_id).first()

    @staticmethod
    def get_employee_by_username(username):
        return User.objects.filter(username = username).first()

    @staticmethod
    def get_employee_by_email(email):
        return User.objects.filter(email__iexact = email).first()

    @staticmethod
    def get_all_employees():
        return User.objects.all()

    @staticmethod
    def get_team_leaders():
        return User.objects.filter(
            role = User.Role.TEAM_LEADER,
            is_active=True
        )

    @staticmethod
    def get_employees_by_team_leader(team_leader):
        return User.objects.filter(
            role=User.Role.DEVELOPER,
            team_leader = team_leader,
            is_active=True
            )

    @staticmethod
    def create_employee(**data):
        user = User.objects.create_user(**data)
        return user

    @staticmethod
    def update_employee(user, **data):
        password = data.pop("password", None)

        for field, value in data.items():
            setattr(user, field, value)

        if password:
            user.set_password(password)

        user.save()
        return user

    @staticmethod
    def deactivate_employee(user):
        user.is_active = False
        user.save(update_fields=["is_active"])
        return user
        
    @staticmethod
    def email_exists(email):
        return User.objects.filter(email__iexact=email).exists()


