from django.shortcuts import render

from user_profile.models import User
from .models import Tweet
from django.views import View

# Create your views here.

class Index(View):
    def get(self, request):
        params = {}
        params["name"] = 'Django Big Boys'
        return render (request,'base.htm', params)
    # def post(self, request):
    #     return HttpResponse ()

class Profile(View):
    """
    user profile page reachable through /user/<username>
    """
    def get (self, request, username):
        tweets = Tweet.objects.filter(user__username=username)
        return render (request,'profile.htm',{'tweets': tweets})




