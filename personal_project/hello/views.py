
#장고에 필요한 라이브러리
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.files.storage import FileSystemStorage

#딥페이크에 필요한 라이브러리
import requests
import json
import time

from .forms import MyForm
from .models import MyModel, Letter

from django .http import JsonResponse
from django.views import View

import pymysql
# from snack.views import View

# class SnackView(View):
#     def postt(self, request):
#         data = json.loads(request.body)
#         Snack.object.create(name=data["snack_name"])
#         return JsonResponse({"message":"created"}, status=201)
        

# def get(self, request):
#     results = []
#     snack_list = Snack.object.all()
#     for i in snack_list:
#         results.append({
#             "id":i.id,
#             "name":i.name

#         })
#         return JsonResponse({"results": results},status=200)






def index(request):
  return render(request, 'index.html')

def login(request):
    # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        username = request.POST['username']
        password = request.POST['password']

        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)
        
        # 해당 user 객체가 존재한다면
        if user is not None:
            # 로그인 한다
            auth.login(request, user)
            return redirect('/')
        # 존재하지 않는다면
        else:
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
    else:
        return render(request, 'login.html')

def signup(request):
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == 'POST':
        # password와 confirm에 입력된 값이 같다면
        if request.POST['password'] == request.POST['confirm']:
            # user 객체를 새로 생성
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            # 로그인 한다
            auth.login(request, user)
            return redirect('/')
    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    return render(request, 'signup.html')


def ai(request):
  return render(request,'ai.html')

def mypage(request):
  return render(request,'mypage.html')

# 로그 아웃
def logout(request):
    # logout으로 POST 요청이 들어왔을 때, 로그아웃 절차를 밟는다.
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')

    # logout으로 GET 요청이 들어왔을 때, 로그인 화면을 띄워준다.
    return render(request, 'login.html')


def upload(request):
    if request.method == "GET":
        return HttpResponse('정상적인 경로가 아닙니다.')

    # 변수값 확인
    msg = request.POST.get('msg', '')

    try:
        image = request.FILES['image']
        voice = request.FILES['voice']
    except:
        return HttpResponse('업로드된 파일이 없습니다.')
    
    print('이미지파일 : ', image.name)
    print('음성파일 : ', voice.name)
    
    # 파일 저장
    up_image = image.name
    up_voice = voice.name
    
     # 이미지 서버에 저장
    fs = FileSystemStorage(location='media/upload/', base_url='media/upload')
    save_file = fs.save(up_image, image)
    save_voice = fs.save(up_voice, voice)
    
    # 실제 저장된 파일 경로 확인
    upload_image_path = '/' + fs.url(save_file)
    print('실제 이미지 경로 : ', upload_image_path)
    
    upload_voice_path = '/' + fs.url(save_voice)
    print('실제 음성 경로 : ', upload_voice_path)
    
    print('받은 메시지 : ', msg)

    # 디비에 저장
    saveDB = Letter()
    saveDB.username = '.'
    saveDB.mess_reco = msg
    saveDB.mess_id = '.'
    saveDB.mess_titles = '소개메시지'
    saveDB.dates='.'
    saveDB.mess_dates='.'
    saveDB.url = upload_image_path
    saveDB.save()

    # API 처리

    return redirect('index')


def upload_image(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_display')
    else:
        form = MyForm()
    return render(request, 'ai.html', {'form': form})

def display_image(request):
    my_model_instance = MyModel.objects.first()
    image_url = my_model_instance.upload_file.url
    return render(request, 'display.html', {'image_url': image_url})



# url = "https://api.d-id.com/talks"

# payload = {
#     "script": {
#         "type": "text",
#         "input": "안녕하세요. 저는 김태권입니다.",
#         "provider": {
#             "type": "microsoft",
#             "voice_id": "ko-KR-BongJinNeural",
#             "voice_config": {"style": "cheerful"},
#         },
#     },
#     "source_url":"https://create-images-results.d-id.com/google-oauth2%7C109366194011084691279/upl_GNgtpYmEvl6tkxh1Dqt7U/image.jpeg",
#     "config": {"stich": "true"},
# }

# headers = {
#     "accept": "application/json",
#     "content-type": "application/json",
#     "authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik53ek53TmV1R3ptcFZTQjNVZ0J4ZyJ9.eyJodHRwczovL2QtaWQuY29tL2ZlYXR1cmVzIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jeF9sb2dpY19pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vY2hhdF9zdHJpcGVfc3Vic2NyaXB0aW9uX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfY3VzdG9tZXJfaWQiOiIiLCJpc3MiOiJodHRwczovL2F1dGguZC1pZC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDg4NjU5MzU1MjIzOTEyMDY0ODAiLCJhdWQiOlsiaHR0cHM6Ly9kLWlkLnVzLmF1dGgwLmNvbS9hcGkvdjIvIiwiaHR0cHM6Ly9kLWlkLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2OTQ1NjQ0OTQsImV4cCI6MTY5NDY1MDg5NCwiYXpwIjoiR3pyTkkxT3JlOUZNM0VlRFJmM20zejNUU3cwSmxSWXEiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIHJlYWQ6Y3VycmVudF91c2VyIHVwZGF0ZTpjdXJyZW50X3VzZXJfbWV0YWRhdGEgb2ZmbGluZV9hY2Nlc3MifQ.3Z5-OmzeZlqImRLfFjiW0PO7-GqeprIirJiDXCJsboHL85CtTm1WPGe07402KIvqA4fG3szUMSIhr62Q6Tlom6qsbeI2lnpNjb1aEzVJQQQ4nl2qEQ5BUmetYYlRffICdprpvzJst5IJS6RakpJyYcYLkGnE5I5swbbTa8tbsa58TezW01JVsA5aBTd4FK1GvTZLfFLNuDyuVvahan49bcotg7_GVX0GbOtdlpQpQJCwU9z4DIlRLLn8IH9SUtu50LSrcMzMfpLpHkvIEvEpw6QTW4KkHqYkQXLEQqCrWojVwfUS5qWcDEHBvg0pSrH-llPGnbmAVXbuxVdtYhX-ng",
# }

# response = requests.post(url, json=payload, headers=headers)

# print(response.text)

# # 아이디 결과 처리
# res = json.loads(response.text)

# id = res["id"]
# print("id = ", id)

# for i in range(30):
#     print(f'변환까지 {i}/30 초 남았습니다.')
#     time.sleep(1)



# url = "https://api.d-id.com/talks/" + id

# result = requests.get(url, headers=headers)

# print(result.text)

# # 오디오 추출
# audio_res = json.loads(result.text)

# video_link = audio_res["result_url"]

# print("영상경로")
# print(video_link)
#  conn = pymysql.connect(id='1', emails='ee', mess_reco= 'dd', mess=’soloDB’, charset=‘utf8’)



