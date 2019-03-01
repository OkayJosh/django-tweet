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

