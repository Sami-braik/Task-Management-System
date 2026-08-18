from ..repositories import TaskRepository
class TaskService():

        @staticmethod
        def get_task_by_id(task_id):
            return TaskRepository.get_task_by_id(task_id)
    
        @staticmethod
        def create_task(**data):
            return TaskRepository.create_task(**data)
    
        @staticmethod
        def update_task(task, **data):
            return TaskRepository.update_task(task, **data)
    
        @staticmethod
        def get_all_tasks():
            return TaskRepository.get_all_tasks()
    
        @staticmethod
        def get_tasks_for_user(user):
            return TaskRepository.get_tasks_for_user(user)
    
        @staticmethod
        def get_tasks_for_team_leader(team_leader):
            return TaskRepository.get_tasks_for_team_leader(team_leader)
    
        @staticmethod
        def get_pending_tasks():
            return TaskRepository.get_pending_tasks()
        @staticmethod
        def save_task(task):
            return TaskRepository.save_task(task)
    
        @staticmethod
        def delete_task(task):
            return TaskRepository.delete_task(task)