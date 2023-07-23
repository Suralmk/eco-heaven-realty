from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Profile(models.Model):
    forget_password_token = models.CharField(max_length=100)
    reset_email = models.EmailField(max_length=100, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.User.get_username
