from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'pages/home.html')

@login_required
def secret(request):
    return render(request, 'pages/secret.html')

def styled(request):
    return render(request, 'pages/styled.html')