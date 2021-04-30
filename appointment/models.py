from django.db import models
# Create your models here.
# python manage.py makemigrations
# python manage.py migrate

class User(models.Model):
	pass


class Item(models.Model):
	client = models.ForeignKey(User, default=None, on_delete=models.CASCADE, null=True)

	#NAME
	name = models.CharField(max_length=50, null=True)
	#EMAIL
	email = models.CharField(max_length=50, null=True)
	#CONTACT
	contact = models.CharField(max_length=50, null=True)	
	#ADDRESS
	address = models.TextField(max_length=50, null=True)
	#DATE
	date = models.DateField(null=True)
	#TIME
	clock = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.name