from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=20)

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_address = models.CharField(max_length=200)
    avelable_room = models.CharField(max_length=50)
    hotel_image = models.ImageField(upload_to='images/')
   
class room(models.Model):
    hotel_name = models.CharField(max_length=100)
    room_no = models.CharField(max_length=20)
    room_image = models.ImageField(upload_to='images/')
    room_image2 = models.ImageField(upload_to='images/')
    hotel_name = models.ForeignKey(Hotel,on_delete=models.CASCADE)



class book(models.Model):
    room_id = models.TextField
    user_name = models.CharField(max_length=50)

class books(models.Model):
    room_id = models.IntegerField(max_length=5)
    hotel_id = models.IntegerField(max_length=5)
    user_name = models.CharField(max_length=50)
    
class desc(models.Model):
    desc = models.CharField(max_length=200)
    room = models.ForeignKey(room,on_delete=models.CASCADE)
    more = models.TextField(max_length=200)

    def __str__(self):
        return self.desc
    
    class  Meta:
        ordering = ["desc"]
    

