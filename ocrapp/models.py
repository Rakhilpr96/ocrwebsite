from django.db import models

# Create your models here.

class Image(models.Model): 
	name = models.CharField(max_length=50, default='photo') 
	Upload_Img = models.ImageField(upload_to='images/') 
