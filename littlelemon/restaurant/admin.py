from django.contrib import admin

# Register your models here.

from restaurant.models import Booking, Menu
#from rest_framework.authtoken.models import Token

#admin.site.register(Token)
admin.site.register(Booking)
admin.site.register(Menu)

