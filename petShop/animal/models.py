from django.db import models

class Animal(models.Model):
	nome = models.CharField(max_length=50)
	raca = models.CharField(max_length=50)
	dono = models.CharField(max_length=100)
	porte = models.CharField(max_length=15)
		