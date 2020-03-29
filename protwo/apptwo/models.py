from django.db import models

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField(max_length=264,unique=True)

class Friend(models.Model):
	nick_name = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
