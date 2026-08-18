from django.db import models
from django.conf import settings
class Task(models.Model):

    class Status(models.TextChoices):
        TODO = "TODO" , "To Do"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        READY_FOR_TEST = "READY_FOR_TEST", "Ready for Test"
        COMPLETED = "COMPLETED", "Completed"

    class ApprovalStatus(models.TextChoices):
        PENDING = "PENDING","Pending"
        APPROVED = "APPROVED" , "Approved"
        REJECTED = "REJECTED" , "Rejected"

    class Priority(models.TextChoices):
        LOW = "LOW", "Low"
        MEDIUM = "MEDIUM", "Medium"
        HIGH = "HIGH", "High"  



    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TODO
    )

    approval_status = models.CharField(
        max_length=20,
        choices=ApprovalStatus.choices,
        default=ApprovalStatus.PENDING,
    )

    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="created_tasks",
    )

    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_tasks",
    )

    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="approved_tasks",
    )

    due_date = models.DateTimeField(
        null=True,
        blank=True,
    )

    approved_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )
    

    
    