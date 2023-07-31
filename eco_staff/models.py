from django.db import models


class AdminTokens(models.Model):
    user = models.CharField(max_length=30)
    token = models.CharField(max_length=100)
