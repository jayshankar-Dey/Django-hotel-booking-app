
from django.urls import path
from . import views


urlpatterns = [
   path('register/', views.register,name='reg'),
   path('login', views.login),
   path('reg/',views.userRegistration,name="register"),
   path('log',views.userlogin,name="login"),
   path('search/',views.search,name="search"),
   path('all/<int:id>/<name>',views.hotel_room,name="hotel_room"),
   path('view/<user>/<int:id>/<int:ids>',views.rooms,name="room"),
   path('book/', views.book,name='book'),
   path('booking/status/<str:user>', views.check_book,name='check_book'),
   path('booking/status/user/<str:user>/<int:room_id>/<int:hotel_id>', views.check_booking,name='check_booking'),
   path('change/address/<user>', views.change_address,name='change_address'),
   path('updet/address/<user>', views.updet_address,name='updet_address'),
   
]
