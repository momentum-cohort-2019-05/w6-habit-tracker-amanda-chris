from django.db import models
from datetime import date

# Create your models here.

class Habit(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="What habit do you want to track?",
        null=True
    )
    target = models.TextField(
        max_length=200,
        help_text="How many things you wanna do?",
        null=True
    )
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class DailyRecord(models.Model):
    entry = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='habits')
    text = models.TextField(
        max_length=200,
        help_text="How many things you wanna do?",
        null=True)
    date = models.DateField(default=date.today)
    
    class Meta:
        ordering = ['-date']
        unique_together = ['entry', 'date']