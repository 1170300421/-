from django.urls import path
from django.conf.urls import url,include
from . import views
from django.contrib import admin

app_name = 'microblog'

urlpatterns = [
    path('weibo/', views.weibo, name='weibo'),
    path('weibo1/', views.weibo1, name='weibo1'),
    path('weibo2/', views.weibo2, name='weibo2'),
    path('', views.homepage, name='homepage'),
    path('homepage2/', views.homepage2, name='homepage2'),
    path('controlledweibo/', views.controlledweibo, name='controlledweibo'),
    path('controlledweibo1/', views.controlledweibo1, name='controlledweibo1'),
    path('detail/<int:num>/', views.detail, name='detail'),
    path('detail1/<int:num>/', views.detail1, name='detail1'),
    path('detail2/<int:num>/', views.detail2, name='detail2'),
    path('detail3/<int:num>/', views.detail3, name='detail3'),
    path('detail4/<int:num>/', views.detail4, name='detail4'),
    path('detail5/<int:num>/', views.detail5, name='detail5'),
    url('login/',views.login,name='login'),
    url('login1/',views.login1,name='login1'),
    url('register/',views.register,name='register'),
    url('register1/',views.register1,name='register1'),
    url('index/',views.register,name='index'),
    url('reg/',views.reg,name='reg'),
    url('read/',views.read,name='read')
]
