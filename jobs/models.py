from django.db import models

# Create your models here.
class Job(models.Model):
    """docstring for ."""
    """ models contains table column names """
    image= models.ImageField(upload_to='images/')
    summary= models.CharField(max_length=200)

    def __str__(self):
        return self.summary
