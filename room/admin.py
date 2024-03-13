from django.contrib import admin
from . models import Register,Hotel,book,desc,room,books


class user(admin.ModelAdmin):
    list_display = ('id','name','address','password')
    

class hotel(admin.ModelAdmin):
    list_display = ('id','hotel_name','hotel_address','avelable_room','hotel_image') 

class Room(admin.ModelAdmin):
    list_display = ('id','hotel_name','room_no','room_image','room_image2','hotel_name')

class BOOK(admin.ModelAdmin):
    list_display = ('room_id','user_name')  

class DESC(admin.ModelAdmin):
    list_display = ('desc','room','more')

class bookes(admin.ModelAdmin):
    list_display = ('room_id','hotel_id','user_name')

admin.site.register(room,Room)
admin.site.register(desc,DESC)
admin.site.register(Register,user)
admin.site.register(Hotel,hotel)

admin.site.register(book,BOOK)
admin.site.register(books,bookes)
# class hotel(admin.ModelAdmin):
#     list_display = ['id',' hotel_name',' hotel_address','avelable_room',' hotel_image']
# Register your models here.
# class hotel(admin.ModelAdmin):
#     list_display = ('id',' hotel_name',' hotel_address','avelable_room',' hotel_image')


# admin.site.register(Hotel)
# class hotel(admin.ModelAdmin):
#     list_display = ('id',' hotel_name',' hotel_address','avelable_room',' hotel_image')