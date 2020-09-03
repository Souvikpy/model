from django.db import models

# Create your models here.

class topic(models.Model):
    topic_name = models.CharField(max_length=100,unique=True, blank=False)

class webpage(models.Model):
    topic=models.ForeignKey(topic, on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True,blank=False)
    url=models.URLField(max_length=100,unique=True,blank=False)

class accessDetails(models.Model):
    webpage=models.ForeignKey(webpage , on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)

