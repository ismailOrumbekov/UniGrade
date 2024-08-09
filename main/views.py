from django.shortcuts import render




def index(request):
    print("hui")
    return render(request, 'index.html')
