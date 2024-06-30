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


class WorkoutExerciseForm(forms.ModelForm):
    class Meta:
        model = models.WorkoutExercise
        fields = ["exercise"]


class SetForm(forms.ModelForm):
    class Meta:
        model = models.Set
        fields = ["weight", "weight_unit", "repetitions", "seconds"]

    sets = forms.IntegerField(min_value=1, max_value=100, initial=1)
