from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Usaremos esta clase para devolver un formulario
from django.contrib.auth.forms import *
# Create your views here.
# Aqui estamos importando el modelo de usuario
from django.contrib.auth.models import User
# En caso de que los datos de nuestro modelo no sean iguales vamos a
from django.http import HttpResponse

from django.db import IntegrityError


#*creacion de coockies


from django.contrib.auth import login, authenticate 
#!Con esto haremos que obligatoriamente el usuario deba esta logueado

# Procedemos a crear nuestro formulario usando la clase UserCreationForm y usando la clase render para el django view
from django.contrib.auth.decorators import login_required 

#Libreria con la cual usaremos los mensajes en pantalla
from django.contrib import messages 


def home(request):  # Archivo home para el inicio
    return render(request, 'home.html')


# Creacion de usuarios por parte del servidor

def signup(request):
    # Este simple if es para verificar si el navegador agarro el form
    if request.method == 'GET':
        print("Datos")
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])  # Creacion de nuestro usuario
                user.save()
                return render(request, 'login.html', {
                    'success': "Usuario creado"
                    
                })
                # Con esta funcion vamos a guardar nuestro usuario
                login(request, user)
                return redirect('login')
            except:
                return render(request, "signup.html", {
                    'form': UserCreationForm,
                    'error': 'Elige otro nombre de usuario'
                })

   # django ya tiene una forma para guardar los datos
   # print(request.POST) #Aqui obtenemos los datos del post
        #print("Obteniendo datos")

    return render(request, "signup.html", {
        'form': UserCreationForm
    })

@login_required
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if User is None:
             return render(request, 'login.html', {
            'form': AuthenticationForm,
            'error': 'Username or password are incorrect'
        }) 
        print(request.POST)
        
