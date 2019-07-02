from django.contrib import admin
from core.models import Habit, DailyRecord

# Register your models here.

class HabitAdmin(admin.ModelAdmin):
    model = Habit
    list_display = ("name", "target",)

# class DailyRecordInLine(admin.StackedInline):
#     model = DailyRecord
#     list_display = ("text",)
#     inlines = [HabitAdmin]

class DailyRecordAdmin(admin.ModelAdmin):
    model = DailyRecord
    list_display = ("achieved",)

admin.site.register(Habit, HabitAdmin)
admin.site.register(DailyRecord, DailyRecordAdmin)

