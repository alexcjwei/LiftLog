from django.contrib import admin
from workouts import models


class SetInline(admin.TabularInline):
    model = models.Set
    extra = 1


class WorkoutExerciseInline(admin.TabularInline):
    model = models.WorkoutExercise
    extra = 1


class WorkoutExerciseAdmin(admin.ModelAdmin):
    inlines = [SetInline]


class WorkoutAdmin(admin.ModelAdmin):
    inlines = [WorkoutExerciseInline]


admin.site.register(models.Workout, WorkoutAdmin)
admin.site.register(models.WorkoutExercise, WorkoutExerciseAdmin)
