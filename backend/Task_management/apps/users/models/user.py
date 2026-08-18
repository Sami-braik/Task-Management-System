from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        MANAGER = "MANAGER" , "Manager"
        TEAM_LEADER = "TEAM_LEADER" , "Team Leader"
        DEVELOPER = "DEVELOPER" , "Developer"

    email = models.EmailField(unique=True)
    team_leader = models.ForeignKey(
        "self",
        on_delete = models.SET_NULL,
        null=True,
        blank=True,
        related_name="developers"
    )
    role = models.CharField(
        max_length=20,
        choices=Role.choices
    )
    
