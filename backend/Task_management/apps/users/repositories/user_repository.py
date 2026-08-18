from ..models import User
class UserRepository():


    def get_employee_by_id(self , id):
        return User.objects.filter(id = id).first()

    def get_employee_by_username(self , username):
        return User.objects.filter(username = username).first()

    def get_employee_by_email(self , email):
        return User.objects.filter(email = email).first()

    def get_all_employees(self):
        return User.objects.all()

    def get_team_leaders(self):
        return User.objects.filter(
            role = User.role.TEAM_LEADER,
            is_active=True
        )


    def get_employees_by_team_leader(self , team_leader):
        return User.objects.filter(
            role=User.role.DEVELOPER,
            team_leader = team_leader,
            is_active=True
            )


    def create_employee(self , **data):
        user = User.objects.create_user(**data)
        return user


    # def update_employee(self , obj):
    #     user = User.objects.update()
    #     return user

    def deactivate_employee(self, user):
        user.is_active = False
        user.save(update_fields=["is_active"])
        

    def email_exists(self, email):
        return User.objects.filter(email__iexact=email).exists()


