from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import * #Usaremos esta clase para devolver un formulario
# Create your views here.


#Procedemos a crear nuestro formulario usando la clase UserCreationForm y usando la clase render para el django view
def hola(request):
    return render(request,"signup.html",{
        'form': UserCreationForm
        
    })