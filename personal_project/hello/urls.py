from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('ai/', views.ai, name='ai'),
    path('mypage/', views.mypage, name='mypage'),
    path('upload/', views.upload, name='upload'),
    path('upload/', views.upload_image, name='upload_image'),
    path('display/', views.display_image, name='image_display'),
      
]