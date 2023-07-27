from django.db import models

class HomePost(models.Model):
    city_location= models.CharField('City', max_length=20)
    home_location = models.CharField('Home Location',max_length=100)
    beds_rooms = models.IntegerField('Bed Rooms')
    bath_rooms = models.IntegerField('Bed Rooms')
    sqft = models.IntegerField('Square feet')
    price = models.IntegerField('Home Price')
    image = models.ImageField(upload_to='homes/')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.home_location

