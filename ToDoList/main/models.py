from django.db import models


# Create your models here.
class Tasks(models.Model):
    title = models.CharField("Task's name", max_length=100)
    done = models.BooleanField(default=False)
    date = models.DateTimeField("Task's date")
    color = models.CharField("Pick category", default='blue')
    star_task = models.BooleanField(default=False)

    def __str__(self):
        return f"Task: {self.title}"

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
