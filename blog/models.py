from django.db import models

# Create your models here.
class Blog(models.Model):
    """docstring for ."""
    Description = models.CharField(max_length=200)
    WhenExactly = models.DateTimeField()
    image= models.ImageField(upload_to='blog/images/')

    def __str__(self):
        return self.Description

    def time_prety(self):
        return self.WhenExactly.strftime('%b %e %Y')
