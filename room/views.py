
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from . models import Register,Hotel,room,desc,books
from django.core.paginator import Paginator

# Create your Register here.
def register(request):
   template = "register.html"
   return render(request,template)

#login
def login(request):
   template = "login.html"
   return render(request,template)

#user registration function
def userRegistration(request):
  
   if request.method == 'POST':
      name = request.POST.get('name')
      address = request.POST.get('address')
      password = request.POST.get('password')
      repassword = request.POST.get('repassword')
      exist = Register.objects.filter(name=name)
      if exist:
         return redirect('reg')
      else:
         if password == repassword and name != " " and password != " " and address != " ":
           Register.objects.create(name=name,address=address,password=password)
           return render(request,'login.html')
         else:
           return redirect('reg')

      
   #login function   
def userlogin(request):
   if request.method == 'POST':
      name = request.POST.get('name')
      password = request.POST.get('password')
      # request.session['name'] = name
      ids = Register.objects.filter(name=name,password=password).values()
      if ids:
         hotel = Hotel.objects.all().values()
         pagination = Paginator(hotel,7)
         page_number = request.GET.get('page')
         final_data =pagination.get_page(page_number)
         return render(request,'home.html',{'all':ids,'name':name,'hotels':final_data})
        
      # if userid:

# def alls(request):
#     hotel = Hotel.objects.all().values()
#     return render(request,'home.html',{'hotels':hotel})


def search(request):
   #  if request.method == 'GET':

      search = request.GET['search']
      if len(search)>78:
         hotel = []

      name = request.GET.get("name")
      address = request.GET.get("address")
     
      hotel = Hotel.objects.filter(hotel_name=search)
      return render(request,'search.html',{'hotels':hotel,'name':name,'address':address,'search':search})
      
 
def hotel_room(request,id,name):
   if request.method == 'GET':
        pi = Hotel.objects.filter(pk=id)
      #   user = Register.objects.filter(name=name)
        all_room = room.objects.filter(hotel_name=id)
        return render(request,'hotel_rooms.html',{'all':pi,'user':name,'all_room':all_room,'ids':id})
   

def rooms(request,user,id,ids):
   if request.method == 'GET':
        pi = Hotel.objects.filter(pk=ids)
        users = Register.objects.filter(name = user)
        all_room = room.objects.filter(id = id)
        all_desc = desc.objects.filter(room = id)
        booked = books.objects.filter(room_id=id)
        
   return render(request,'room.html',{'hotel':pi,'user':users,'room':all_room,'desc':all_desc,'name':user,'bookd':booked})
       
def book(request):
   if request.method == 'POST':
      room_id = request.POST.get('room')
      hotel_id = request.POST.get('hotel')
      user = request.POST.get('name')
      booked = books.objects.filter(room_id=room_id)
      if booked:
         hotel = Hotel.objects.filter(pk=hotel_id)
         rooms = room.objects.filter(pk=room_id)
         users = Register.objects.filter(name = user)
         return render(request,'book.html',{'hotel':hotel,'room':rooms,'user':users})
      else:
        books.objects.create(room_id=room_id,hotel_id=hotel_id,user_name=user)
        hotel = Hotel.objects.filter(pk=hotel_id)
        rooms = room.objects.filter(pk=room_id)
        users = Register.objects.filter(name = user)
        return render(request,'book.html',{'hotel':hotel,'room':rooms,'user':users})  
      


def check_book(request,user):
   all = books.objects.filter(user_name=user).order_by('-room_id')
   return render(request,'your_book.html',{'alls':all})

def check_booking(request,user,room_id,hotel_id):
         hotel = Hotel.objects.filter(pk=hotel_id)
         rooms = room.objects.filter(pk=room_id)
         users = Register.objects.filter(name = user)
   
         return render(request,'check_book.html',{'hotel':hotel,'room':rooms,'user':users})

def change_address(request,user):
   return render(request,'change_address.html',{'name':user})

def updet_address(request,user):
   if request.method == 'POST':
    updet_address = request.POST.get('address')
    Register.objects.filter(name = user).update(address=updet_address)
    return render(request,'change_address.html',{'name':user})
  
   
#  if request.method == "GET": 
#      books = books(room_id=id,hotel_id=h_id,user_name=user)
#      books.save()
#      hotel = Hotel.objects.filter(pk=h_id)
#      rooms = room.objects.filter(pk=id)
#      users = Register.objects.filter(name = user)
#      return render(request,'book.html',{'hotel':hotel,'room':rooms,'user':users})