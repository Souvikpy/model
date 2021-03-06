from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
# Create your models here.

class topic(models.Model):
    topic_name = models.CharField(max_length=100,unique=True, blank=False, validators=[validators.MaxLengthValidator(10)])



    def __str__(self):
        return self.topic_name
    
def validate_name(name):
    if not name.isalpha():
        raise ValidationError("{} is having characters other than alpha".format(name))

class webpage(models.Model):
    topic=models.ForeignKey(topic, on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True,validators=[validate_name], blank=False)
    url=models.URLField(max_length=100,unique=True,blank=False)

    def __str__(self):
        return self.name
    

class accessDetails(models.Model):
    webpage=models.ForeignKey(webpage , on_delete=models.CASCADE)
    datetime=models.DateTimeField()
    def __str__(self):
       return str(self.datetime).split(' ')[0]
   

