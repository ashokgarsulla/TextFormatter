from django.db import models
from django.db.models import Model
from ckeditor.fields import RichTextField
 
 
# Create your models here.
class TextFormter(Model):
    formatter_field = RichTextField()

class Post(Model):
    title = models.CharField(max_length=50)
    body = RichTextField(blank = True , null = True )

    def __str__(self):
        return self.title
