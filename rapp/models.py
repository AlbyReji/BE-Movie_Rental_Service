from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length= 50)
    release_date = models.DateField()
    genre = models.CharField(max_length=25)
    duration_minutes = models.IntegerField()
    rating = models.FloatField()


    def __str__(self):
        return self.title

