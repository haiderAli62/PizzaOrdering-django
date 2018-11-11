from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Topping, Regular_Pizza , Sicilian_Pizza , Cart  , Orders


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
    	return render(request , "orders/login.html" , {"message":None} )

    r_pizzas = Regular_Pizza.objects.all()
    s_pizzas = Sicilian_Pizza.objects.all()
    toppings = Topping.objects.all()	
    context = {
    "r_pizzas" : r_pizzas,
    "s_pizzas" : s_pizzas,
    "toppings" : toppings,
    "user" : request.user
    }
    return render(request , "orders/index.html" , context)

def login_view(request):
	username = request.POST["username"]
	password = request.POST["password"]
	user = authenticate(request , username=username ,password=password )
	if user is not None:
		login(request , user)
		return HttpResponseRedirect(reverse("index"))
	else:
		return render(request , "orders/login.html" , {"message":"Invalid credentials"})

def logout_view(request):
	logout(request)
	return render(request , "orders/login.html" , {"message":"Logout successfully "})

def register(request):
	return render(request , "orders/register.html")

def registered(request):
	username = request.POST.get("usernam")
	email = request.POST.get("emai")
	password = request.POST.get("passwor")
	User.objects.create_user(f"{username}" , f"{email}" , f"{password}")
	return render(request , "orders/login.html" )


# views for home page
def add_items(request , pizza_name ,small , large):
	item = pizza_name
	size_s = small
	size_l = large
	toppings = Topping.objects.all()	
	context = {
	"item" : item,
	"size_s" : size_s,
	"size_l" : size_l,
	"toppings" : toppings
	}
	return render(request , "orders/add_items.html" , context)

def add_to_cart(request , item):
	name = item
	size = request.POST.get("size")
	extras = request.POST.get("extras")
	c = Cart(item=name , size=size , extras=extras)
	c.save()
	c.user.set([request.user])
	return HttpResponseRedirect(reverse("index"))
	
def show_cart(request):
	cart = Cart.objects.filter(user=request.user)

	context = {
	"cart" : cart,
	"user" : request.user.username
	}
	return render(request , "orders/cart.html" , context)

def place_order(request , item , size ,extras , pk):
	order = Orders(item=item , size=size , extras=extras)
	order.save()
	order.user.set([request.user])
	Cart.objects.get(pk=pk).delete()
	return HttpResponseRedirect(reverse("index"))


def view_orders(request):
	orders = Orders.objects.all()
	context = {
	"orders" : orders
	}
	return render(request , "orders/view_orders.html" , context)





	





