from django.shortcuts import render
from django.views import generic
from .models import Habit

# Create your views here.

# class HabitListView(generic.ListView):
#     model = Habit

def index(request):
    habits = Habit.objects.all()
    return render(request, 'core/habit_list.html', {
        "habits":habits
    })