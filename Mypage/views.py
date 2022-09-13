from django.shortcuts import render

# Create your views here.
def mypage(request):
    return render(request,'Mypage/mypage.html')

def profile(request):
    return render(request,'Mypage/profile.html')