from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import USER

# Create your views here.

@login_required
def interview1(request):
    return render(request,'interview/recording_1.html')

@login_required
def interview2(request):
    return render(request,'interview/recording_2.html')

@login_required
def interview3(request):
    return render(request,'interview/recording_3.html')

@login_required
def interview4(request):
    return render(request,'interview/recording_4.html')

@login_required
def interview(request,page_num):
        question=["자기소개 해주세요.",
                  "우리회사에 왜 지원했나요?",
                  "본인의 장점을 말해주세요.",
                  "살면서 가장 어려웠던 일과 그것을 어떻게 극복했는지 말해주세요."]
        return render(request,'interview/recording.html',{"question":f"Q{page_num}. {question[page_num - 1]}","page_num":page_num+1,"max_page":len(question)})

#
# @login_required
# def analysis(request):
#     ##face > 눈깜빡임, 고개움직임, 표정
#     ##voice > 말빠르기, 톤, 추임새, 길이
#     face=face_model.object.filter(id=request.user)[::-1][:4]
#     voice=voice_model.object.filter(id=request.user)[::-1][:4]
#     blink=list(map(lambda x: int(x["blink_stat"]),face.values()))
#     blink_stat=sum(blink)/len(face)
#     blink_score=sum(map(lambda x: 25 if 15<x<20 else 20 if 10<x<25 else 15 if 5<x<30 else 10 if x<35 else 5,blink))
#
#     direction=list(map(lambda x: int(x["direction"]),face.values()))
#     direction_stat=sum(direction)/len(face)
#     direction_score=sum(map(lambda x: 25 if x==0 else 15 if x<5 else 5,direction))
#
#     # emotion=list(map(lambda x: int(x["emotion_stat"]),face.values()))
#     # emotion_stat=sum(direction)/len(face)
#     # emotion_score
#
#     rate=sum(map(lambda x: int(x["rate_stat"]),voice.values()))/len(voice)
#     rate_stat=sum(rate)/len(face)
#     rate_score=sum(map(lambda x: 25 if 5<x<7 else 20 if 4.5<x<7.5 else 15 if 4<x<8 else 10 if 3<9 else 5, rate))
#
#     # filler=sum(map(lambda x: int(x["filler_stat"]),voice.values()))/len(voice)
#
#
#     time=list(map(lambda x: int(x["time"]),voice.values()))
#     time=sum(time)/len(face)
#     time_score=sum(map(lambda x: 25 if 35<x<59 else 15 if 20<x else 5,direction))
#
#
#
#
#     return render(request,'interview/analysis_copy.html',{"score":score,"face_result":face,"voice_result":voice})

@login_required
def analysis(request):
    # info=USER.objects.all()
    # info=info[len(info)-4:]
    info=USER.objects.filter(is_superuser=0)[:10]
    print(info.values()[3]["is_superuser"])
    print(info.values()[3]["username"])
    print(sum(map(lambda x: int(x["is_superuser"]),info.values())))
    # print(info.values_list()[0])
    # for i in info:
    #     print(i)
    # print(info,type(info))
    return render(request,'interview/analysis.html',{"info":info})