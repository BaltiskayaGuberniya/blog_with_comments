from django.contrib import admin
from .models import Blogpost, Comment

# Register your models here.
admin.site.register(Comment)
admin.site.register(Blogpost)