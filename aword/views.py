from django.shortcuts import render




def home(request):
    return render(request, 'all-pages/index.html')


# Create your views here.
