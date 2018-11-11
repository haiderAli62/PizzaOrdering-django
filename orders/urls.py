from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login" , views.login_view , name="login"),
    path("logout" , views.logout_view , name="logout"),
    path("register" , views.register , name="register"),
    path("registration_successful" , views.registered , name="registered"),
    path("add_items/<pizza_name>/<small>/<large>/" , views.add_items , name="add_items"),
    path("add_to_cart/<item>" , views.add_to_cart , name="add_to_cart"),
    path("show_cart" , views.show_cart , name="show_cart"),
    path("place_order/<item>/<size>/<extras>/<pk>/" , views.place_order , name="place_order"),
    path("view_orders" , views.view_orders)


]
