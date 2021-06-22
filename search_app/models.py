# search_app models.py
from django.db import models

# Create your models here.
class Csv(models.Model):
    file_name = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"File ID: {self.id}"

class Product(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name