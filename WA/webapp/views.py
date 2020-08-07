from django.shortcuts import render, redirect
from .forms import User
from .models import User
from .models import Event
from .forms import Event
from .models import *
from django.contrib.auth.forms import UserCreationForm


def registerpage(request):
    form = UserCreationForm
    context = {'form': form}

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password'],
        try:
            user = User.objects.get(email=email, password=password)
            request.session['user_is_authenticated'] = False
            return redirect('webapp/register.html')
        except:
            return render(request, 'webapp/register.html', context)
    return render(request, 'webapp/register.html', context)

def home(request):
    try:
        user_is_authenticated = request.session['user_is_authenticated']
    except:
        return redirect('/loginpage')

    return render(request, 'webapp/home.html')


def loginpage(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email, password=password)
            request.session['user_is_authenticated'] = True
            return redirect('/')
        except:

            return render(request, 'webapp/Login.html', {'incorrect': False})
    return render(request, 'webapp/Login.html', {'incorrect': False})
# def event_detailed_view(request):
#
#     return render(request, "webapp/home.html")
