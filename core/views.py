from django.shortcuts import render
from django.views import generic
from .models import Habit, DailyRecord
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import DetailView

# Create your views here.

# class HabitListView(generic.ListView):
#     model = Habit

def index(request):
    habits = Habit.objects.all()
    return render(request, 'core/habit_list.html', {
        "habits":habits
    })

class HabitCreate(CreateView):
    model = Habit
    fields = '__all__'
    success_url = reverse_lazy('home')

class RecordCreate(CreateView):
    model = DailyRecord
    fields = '__all__'

class ShowHabit(DetailView):
    model = Habit
    fields = '__all__'

class DailyRecordUpdate(UpdateView):
    model = DailyRecord
    fields = '__all__'
    success_url = reverse_lazy('home')

