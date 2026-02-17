from django.db import models

class RegisteredUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

# Create your models here.
