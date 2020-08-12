from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import  HttpResponse
from django.contrib.auth import  logout
from django.shortcuts import render, redirect
from .forms import User
from .models import *


@login_required()
def pagelogout(request):
    if request.method == "POST":
        logout(request)

    return render(request, 'webapp/login.html')


def registerpage(request):
    form = UserCreationForm
    context = {'form': form}

    if request.method == "POST":
        print(request.POST)
        username = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        try:
            user = User()
            user.name = username
            user.email = username
            if password1 == password2:
                user.password = password1
                user.save()
                request.session['user_is_authenticated'] = True
                return redirect('/')
            else:
                print('password no match')
                return render(request, 'webapp/register.html', context)

        except:
            print('exception')
            return render(request, 'webapp/register.html', context)

    return render(request, 'webapp/register.html', context)


# todo more info page



def thankyou(request):
    return HttpResponse("Thank You!!!")
def simple_checkout(request):
    return render(request, 'webapp/simplecheckout.html')




def book(request, id):
    event = Event.objects.get(pk=id)
    return render(request, 'webapp/book.html', {'event': event})


# todo build page


def home(request):
    # todo make book button beautiful Book/info
    try:
        user_is_authenticated = request.session['user_is_authenticated']
    except:
        return redirect('/loginpage')
    #GETS ALL OF THE CLASS EVENT OBJECTS
    events = Event.objects.all()
    events_sorted = []
    mini_events = []
    for event in events:
        # todo add photo link option
        if len(mini_events) == 4:
            l = []
            for m in mini_events:
                l.append(m)
            events_sorted.append(l)
            mini_events.clear()
        mini_events.append(event)
    l = []
    for m in mini_events:
        l.append(m)
    if len(mini_events) == 1:
        l.append('')
        l.append('')
        l.append('')
    if len(mini_events) == 2:
        l.append('')
        l.append('')
    if len(mini_events) == 3:
        l.append('')
    events_sorted.append(l)

    return render(request, 'webapp/home.html', {'events': events_sorted})


def loginpage(request):
    # todo sign out
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
