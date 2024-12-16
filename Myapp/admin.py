from django.contrib import admin
from .models import User, News, Equipment, Field, Booking

admin.site.register(User)
admin.site.register(News)
admin.site.register(Equipment)
admin.site.register(Field)
admin.site.register(Booking)
