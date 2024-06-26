from django import forms
from workouts import models


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = models.Workout
        fields = ["name", "date"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }

    def form_valid(self, form):
        self.workout = form.save(commit=False)
        self.workout.user = self.request.user
        self.workout.save()
        return super().form_valid(form)
