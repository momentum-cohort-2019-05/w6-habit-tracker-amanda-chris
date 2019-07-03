from django.db import models
from datetime import date

# Create your models here.

class Habit(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="What habit do you want to track?",
        null=True
    )
    target = models.IntegerField(
        help_text="How many is your target?",
        null=True
    )
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.name

class DailyRecord(models.Model):
    entry = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='habits')
    achieved = models.IntegerField(
        help_text="How many X did you today?",
        null=True)
    date = models.DateField(default=date.today)
    
    class Meta:
        unique_together = ['entry', 'date']