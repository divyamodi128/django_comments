from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from .forms import UserForm

# Create your views here.
class Register(View):

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            return HttpResponseRedirect('/user/success/')
        return HttpResponseRedirect('/user/register/', {'msg': 'Error Occured Registring'})
    
    def get(self, request):
        form = UserForm()
        return render(request, 'register.html', {'form': form})

class Login(View):

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            return HttpResponseRedirect('/user/success/')
        return HttpResponseRedirect('/fail/')
    
    def get(self, request):
        form = UserForm()
        return render(request, 'register.html', {'form': form})