from django.contrib import admin

# Register your models here.
from .models import *

# register task model
admin.site.register(Task)
