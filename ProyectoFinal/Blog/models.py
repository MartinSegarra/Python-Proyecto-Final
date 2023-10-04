from django.db import models

# Create your models here.


class Redactor(models.Model):
    nombre = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    edad = models.IntegerField()


class Comentador(models.Model):
    nombre = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    edad = models.IntegerField()


class Moderador(models.Model):
    nombre = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
