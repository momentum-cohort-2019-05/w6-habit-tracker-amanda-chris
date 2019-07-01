from django.db import models

# Create your models here.

class Habit(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="What habit do you want to track?"
    )

    def __str__(self):
        return self.name

# class DailyRecord:
    