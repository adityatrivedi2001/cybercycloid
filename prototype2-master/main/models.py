from django.db import models

# Create your models here.
class contactus(models.Model):
    email = models.CharField(max_length=50)
    text = models.TextField(null = True,default = 'null')

    def __str__(self):
        return self.email

class Teammates(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to = 'static/img')
    about = models.TextField()

    def __str__(self):
        return self.name
    