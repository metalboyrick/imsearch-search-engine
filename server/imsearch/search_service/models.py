from django.db import models

# Create your models here.
class Image(models.Model):
    image_id = models.CharField(max_length=100,unique=True, primary_key= True, blank=False)
    image_path = models.CharField(max_length=155, unique=True, blank=False)

class Label(models.Model):
    label_id = models.CharField(max_length=100,unique=True, primary_key= True, blank=False)
    label_name = models.CharField(max_length=155, unique=False, blank=False)
    embedding = models.TextField(blank=True, default="[]")

class ImageLabels(models.Model):
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE)
    label_id = models.ForeignKey(Label, on_delete=models.CASCADE)
