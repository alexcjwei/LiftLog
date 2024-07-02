from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import Profile
from workouts.models import Workout, WorkoutExercise, Set
from exercises.models import Exercise


class ExerciseDetailViewTests(TestCase):
    def setUp(self):
        self.test_user = User.objects.create(username="testuser")
        self.test_profile = Profile.objects.create(user=self.test_user)

    def test_sets_with_none_weight_does_not_throw_error(self):
        # Login
        self.client.force_login(self.test_user)

        # Setup
        exercise = Exercise.objects.create(name="Test Exercise")
        workout = Workout.objects.create(
            profile=self.test_profile, name="Test Workout", date="2024-01-01"
        )
        workout_exercise = WorkoutExercise.objects.create(
            workout=workout, exercise=exercise
        )
        set_ = Set.objects.create(
            workout_exercise=workout_exercise,
            repetitions=10,
        )

        # Check response
        response = self.client.get(f"/exercises/{exercise.pk}/")
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "TypeError")
