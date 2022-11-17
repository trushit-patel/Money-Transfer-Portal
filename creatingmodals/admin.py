from django.contrib import admin

# Register your models here.
from .models import Person, Transaction

admin.site.register(Person)
admin.site.register(Transaction)