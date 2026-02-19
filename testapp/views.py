from django.db.transaction import commit
from django.http import HttpResponseRedirect
from django.shortcuts import render
from testapp.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def home_view(request):
    return render(request, "testapp/home.html")

@login_required
def python_view(request):
    return render(request, "testapp/python.html")

@login_required
def java_view(request):
    return render(request, "testapp/java.html")

@login_required
def aptitude_view(request):
    return render(request, "testapp/aptitude.html")

def logout_view(request):
    logout(request)
    return render(request, "testapp/logout.html")

def signup_view(request):
    form= SignUpForm()
    if request.method == "POST":
        form= SignUpForm(request.POST)
        user= form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, "testapp/signup.html", {'form': form})