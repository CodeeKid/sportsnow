from django.shortcuts import render, redirect
from .forms import User
from .models import User
from .models import Event
from .forms import Event


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
            return render(request, 'webapp/Login.html', {'incorrect': True})

    return render(request, 'webapp/Login.html', {'incorrect': False})


def event_detailed_view(request):

    return render(request, "webapp/home.html")

