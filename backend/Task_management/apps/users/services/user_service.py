from rest_framework.exceptions import (
    PermissionDenied,
    ValidationError,
)

from ..models import User
from ..repositories import UserRepository


class UserService:

    @staticmethod
    def ensure_manager(user):
        if user.role != User.Role.MANAGER:
            raise PermissionDenied(
                "Only managers can perform this operation."
            )

    @staticmethod
    def validate_user_data(employee=None, **data):
        if employee is None:
            current_role = None
            current_team_leader = None
        else:
            current_role = employee.role
            current_team_leader = employee.team_leader

        role = data.get("role", current_role)
        team_leader = data.get(
            "team_leader",
            current_team_leader,
        )

        if employee is not None and employee == team_leader:
            raise ValidationError(
                "An employee cannot be their own team leader."
            )

        if role != User.Role.DEVELOPER and team_leader is not None:
            raise ValidationError(
                "Only developers can have a team leader."
            )

        if (
            team_leader is not None
            and team_leader.role != User.Role.TEAM_LEADER
        ):
            raise ValidationError(
                "The assigned user must be a team leader."
            )

    @staticmethod
    def create_employee(current_user, **data):
        UserService.ensure_manager(current_user)
        UserService.validate_user_data(**data)

        return UserRepository.create_employee(**data)

    @staticmethod
    def update_employee(current_user, employee, **data):
        UserService.ensure_manager(current_user)

        UserService.validate_user_data(
            employee=employee,
            **data,
        )

        return UserRepository.update_employee(
            employee,
            **data,
        )

    @staticmethod
    def deactivate_employee(current_user, employee):
        UserService.ensure_manager(current_user)

        if current_user == employee:
            raise ValidationError(
                "A manager cannot deactivate their own account."
            )

        return UserRepository.deactivate_employee(employee)

    @staticmethod
    def get_employee_by_username(username):
        return UserRepository.get_employee_by_username(username)

    @staticmethod
    def get_employee_by_id(employee_id):
        return UserRepository.get_employee_by_id(employee_id)   
    @staticmethod
    def get_employee_by_email(email):
        return UserRepository.get_employee_by_email(email)

    @staticmethod
    def get_all_employees():
        return UserRepository.get_all_employees()

    @staticmethod
    def get_team_leaders():
        return UserRepository.get_team_leaders()

    @staticmethod
    def get_employees_by_team_leader(team_leader):
        return UserRepository.get_employees_by_team_leader(team_leader)
        
    @staticmethod
    def email_exists(email):
        return UserRepository.email_exists(email)
        


    
