from django.contrib.auth import login
from django.shortcuts import render, redirect
# Create your views here.

from .models import USER

#assuming the user name is passed in via get

def signin(request):
    #POST 요청 > 메인 페이지로 REDIRECT
    if request.method == 'POST':
        #EMAIL 가져와서
        username = request.POST['email']
        try:
            #USER 모델에서 일치하는 값을 찾음
            user = USER.objects.get(username=username)
        except USER.DoesNotExist:
            #해당하는 유저가 없으면 username(=email)로 새로운 계정 생성
            user = USER(username=username)
            #DB에 커밋
            user.save()
            user = USER.objects.get(username=username)
        #비밀번호가 없어서 유저를 정상적으로 인증할 수 없음 강제로 인증 후 로그인 메서드를 이용해 로그인
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        return redirect("/mainapp")
    #GET 요청 > 로그인 페이지
    else:
        return render(request,"accounts/login_page.html")

