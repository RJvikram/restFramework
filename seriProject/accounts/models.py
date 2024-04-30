from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    role = models.IntegerField()
    city = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name