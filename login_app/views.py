from django.shortcuts import render

def obtener_login(request):
    return render(request, 'web_app/login.html')
