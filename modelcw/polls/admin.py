from django.contrib import admin

# Register your models here.

from .models import Dog

admin.site.register(Dog)

from .models import Account

admin.site.register(Account)

# login information
# username: admin
# password: test4321
