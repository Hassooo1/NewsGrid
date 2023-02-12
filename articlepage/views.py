from django.shortcuts import render

# Create your views here.

def article(request):
    return render(request, 'articlepage/article.html')

def createarticle(request):
    return render(request, 'articlepage/createarticle.html')

def dashboard(request):
    return render(request, 'articlepage/dashboard.html')