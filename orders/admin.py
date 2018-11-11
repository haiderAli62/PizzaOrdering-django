from django.contrib import admin
from .models import Topping, Regular_Pizza , Sicilian_Pizza , Cart , Orders
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(Topping)
admin.site.register(Regular_Pizza)
admin.site.register(Sicilian_Pizza)
admin.site.register(Cart)
admin.site.register(Orders)