from django.db import models

class student(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    username = models.IntegerField(unique=True)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.fname + " " + self.lname 

class event(models.Model):
    input_username = models.IntegerField()
    input_year = models.IntegerField()
    input_month = models.IntegerField()
    input_day = models.IntegerField()
    input_text = models.CharField(max_length=100)
    input_time = models.CharField(max_length=100)
    
    def __str__(self):
        return self.input_text 
