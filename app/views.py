from django.shortcuts import render, redirect
from . import models


# Create your views here.
def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        gender = request.POST['gender']
        dob = request.POST['dob']
        query = models.Person(first_name=first_name,
                              last_name=last_name,
                              email=email,
                              password=password,
                              gender=gender,
                              dob=dob)
        query.save()
        return redirect(f'/login/?user={first_name}{last_name}')
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        query = models.Person.objects.filter(email=email, password=password)
        if len(query) != 0:
            query.get(email=email).active = True
            first_name = query.values('first_name')[0]['first_name']
            last_name = query.values('last_name')[0]['last_name']
            gender = query.values('gender')[0]['gender']
            dob = query.values('dob')[0]['dob']
            c = {'first_name': first_name,
                 'last_name': last_name,
                 'email': email,
                 'password': password,
                 'gender': gender,
                 'dob': dob}
            return render(request, 'home.html', context=c)
    return render(request, 'login.html')


def home(request):
    if request.method == 'POST':
        return redirect('/')
