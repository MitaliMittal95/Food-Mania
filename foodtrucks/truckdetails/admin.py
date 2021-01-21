from django.contrib import admin
from .models import Truck
# Register your models here.

@admin.register(Truck)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location','opentime','closetime')

