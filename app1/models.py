from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=20)
    age=models.PositiveIntegerField()
    roll=models.PositiveIntegerField()
    email=models.EmailField()
    pass1=models.CharField(max_length=20, default="temporary_value")
    pass2=models.CharField(max_length=20, default="temporary_value")

    def __str__(self):
        return self.name