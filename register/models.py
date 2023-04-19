from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique = True)
    email = models.EmailField(unique= True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    is_subscribed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        user = User.objects.create_user(username=self.username, password=self.password)
        user.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
