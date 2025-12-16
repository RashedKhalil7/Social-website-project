from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
# Create your views here.
 

@login_required
def dashboard(request):
    return render(request, "account/dashboard.html" , {'section':'dashboard'})

# customize logout view to validate using another method behind POST method in request
class UserLogoutView(LogoutView):
    def get(self,request):
        logout(request)
        return redirect('login')