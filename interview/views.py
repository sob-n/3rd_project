from django.shortcuts import render

# Create your views here.
def interview(request):
    return render(request,'interview/recording_1.html')

def interview1(request):
    return render(request,'interview/recording_2.html')

def interview2(request):
    return render(request,'interview/recording_3.html')

def interview3(request):
    return render(request,'interview/recording_4.html')

def analysis(request):
    return render(request,'interview/analysis_1.html')

def analysis1(request):
    return render(request,'interview/analysis_2.html')

def homepage(request):
    return render(request,'interview/homepage_1.html')