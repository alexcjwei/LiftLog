from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "exercises"
        ordering = ["name"]

    def __str__(self):
        return self.name
