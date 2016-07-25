from django.contrib import admin
from magazines.models import Magazine
from magazines.models import Purchase

# Register your models here.

admin.site.register(Magazine)
admin.site.register(Purchase)