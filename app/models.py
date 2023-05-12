from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    age=models.IntegerField()
    email=models.EmailField()



    def __str__(self):
        return self.name