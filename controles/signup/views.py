from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import * #Usaremos esta clase para devolver un formulario
# Create your views here.

from django.contrib.auth.models import User #Aqui estamos importando el modelo de usuario
#En caso de que los datos de nuestro modelo no sean iguales vamos a 
from django.http import HttpResponse



#Procedemos a crear nuestro formulario usando la clase UserCreationForm y usando la clase render para el django view



def home(request): #Archivo home para el inicio
    return render(request,'C:\Sistema_log\controles\signup/templates\html\home.html')

def signup(request):
#Este simple if es para verificar si el navegador agarro el form
    if request.method == 'GET':
        print("Enviando")
    else:
            if request.POST['password1'] == request.POST['password1']:
            #Registrando al usuario 
                User.objects.create_user()#Creacion de nuestro usuario
            
            return HTTPResponse("Contraseñas")
       
       
       #django ya tiene una forma para guardar los datos 
       #print(request.POST) #Aqui obtenemos los datos del post
        #print("Obteniendo datos")
    
    
    return render(request,"signup.html",{
        'form': UserCreationForm
    })




