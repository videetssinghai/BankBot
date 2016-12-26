from django.contrib import admin

# Register your models here.
from models import User,Accounts

admin.site.register(User)
admin.site.register(Accounts)
