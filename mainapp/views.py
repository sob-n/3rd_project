from django.shortcuts import render


# Create your views here.

def main(request):
    print(request.user)
    return render(request, 'mainapp/main.html')
