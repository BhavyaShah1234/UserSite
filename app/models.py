from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, primary_key=True, unique=True, db_index=True)
    password = models.CharField(max_length=20)
    gender = models.CharField(max_length=1)
    dob = models.DateField()
    active = models.BooleanField(default=False)
