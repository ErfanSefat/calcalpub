from django.db import models

class student(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    username = models.IntegerField(unique=True)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.fname + " " + self.lname 

