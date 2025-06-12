from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola desde Django")

def saludar_usuario(request, nombre):
    return HttpResponse(f"Hola, {nombre}!")

def mostrar_edad(request, edad):
    return HttpResponse(f"Tienes {edad} años.")