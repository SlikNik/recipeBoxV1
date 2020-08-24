from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=80)
    bio = models.TextField()
    custom_user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=80)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=50)
    recipe_date = models.DateTimeField(default=timezone.now)
    instructions = models.TextField()

    def __str__(self):
        return self.title