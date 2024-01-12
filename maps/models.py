from django.db import models

# Create your models here.
class Location(models.Model):
    lng = models.FloatField()
    lat = models.FloatField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Image(models.Model):
    name = models.CharField('Venue name', max_length=120)
    venue_image = models.ImageField(null=True, blank=True, upload_to='.')

    def __str__(self):
        return self.name
    
class Paris(models.Model):

    address = models.CharField(max_length=255)
    lat = models.FloatField()
    lng = models.FloatField()
    location = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    subCategory = models.CharField(max_length=255)
    popularity = models.IntegerField()
    numReviews = models.IntegerField()
    def __str__(self):
        return self.name