from django.db import models

class HomePost(models.Model):
    city_location= models.CharField('City', max_length=20)
    home_location = models.CharField('Home Location',max_length=100)
    home_choice = (
        ('For Sale', 'For Sale'),
        ('For Rent', 'For Rent'),
    )
    home_type = models.CharField(max_length=30, choices=home_choice, null=True, blank=True)
    beds_rooms = models.IntegerField('Bed Rooms')
    bath_rooms = models.IntegerField('Bath Rooms')
    sqft = models.IntegerField('Square feet')
    price = models.IntegerField('Home Price')
    image = models.ImageField(upload_to='homes/')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.home_location

