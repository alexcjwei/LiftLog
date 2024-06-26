# Generated by Django 4.2.13 on 2024-06-26 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
        ("workouts", "0003_alter_workout_options_remove_workout_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="workout",
            name="profile",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="accounts.profile",
            ),
            preserve_default=False,
        ),
    ]
