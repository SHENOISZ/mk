from django.db import models

# Create your models here.

class form_blog(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    comment = models.TextField()
    publish = models.CharField(max_length=200)

class contador(models.Model):
    count = models.IntegerField()