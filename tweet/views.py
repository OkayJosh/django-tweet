from django.shortcuts import render
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
        params = dict()
        user = user.objects.get(username=username)
        params["tweets"] = tweets
        params["user"] = user
        return render (request,'profile.htm', params)

