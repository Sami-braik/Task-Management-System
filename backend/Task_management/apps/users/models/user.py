from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        MANAGER = "MANAGER" , "Manager"
        TEAM_LEADER = "TEAM_LEADER" , "Team Leader"
        DEVELOPER = "DEVELOPER" , "Developer"
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

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
    
    
