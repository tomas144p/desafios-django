from django.shortcuts import render

def inicio(request):
    contexto = {"nombre": "quien quiera que seas"}
    return render(request, 'index.html', contexto)
def curriculum(request):
    return render(request, 'curriculum.html')