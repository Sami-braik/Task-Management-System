from ..models import Task


class TaskRepository:

    @staticmethod
    def get_task_by_id(task_id):
        return Task.objects.filter(id=task_id).first()

    @staticmethod
    def create_task(**data):
        return Task.objects.create(**data)

    @staticmethod
    def update_task(task, **data):
        for field, value in data.items():
            setattr(task, field, value)

        task.save()
        return task

    @staticmethod
    def get_all_tasks():
        return Task.objects.all()

    @staticmethod
    def get_tasks_for_user(user):
        return Task.objects.filter(assigned_to=user)

    @staticmethod
    def get_tasks_for_team_leader(team_leader):
        return Task.objects.filter(
            assigned_to__team_leader=team_leader
        )

    @staticmethod
    def get_pending_tasks():
        return Task.objects.filter(
            approval_status=Task.ApprovalStatus.PENDING
        )

    @staticmethod
    def save_task(task):
        task.save()
        return task

    @staticmethod
    def delete_task(task):
        task.delete()