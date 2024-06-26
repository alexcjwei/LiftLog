from django.db import models


class Exercise(models.Model):
    class Meta:
        db_table = "exercises"

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
