from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = RichTextField(blank=True, null=True)
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    body = models.CharField(max_length=150)
    number = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    