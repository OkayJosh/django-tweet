from django.contrib import admin
from .models import Tweet
from .models import HashTag

admin.site.register(Tweet)
admin.site.register(HashTag)