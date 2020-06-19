from django.shortcuts import render

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from .models import  User
from .models import  User1
# Create your views here.
from microblog.models import HotSpot
from microblog.models import ControlledHotSpot
from microblog.models import ControlledHotSpot1
from keyword_processer.keyword_processer import KeywordProcesser
from log.log4j import Log4j
import pymysql
#from microblog.models import Hot

class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=50)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())
    email = forms.EmailField(label='邮箱')
# 这个函数不用关注
def weibo(request):
    return render(request, 'weibo.html')

def weibo1(request):
    return render(request, 'weibo1.html')

def weibo2(request):
    return render(request, 'weibo2.html')

def controlledweibo(request):
    return render(request, 'controlledweibo.html')

def controlledweibo1(request):
    return render(request, 'controlledweibo1.html')

def index(request):
    return render(request,'index.html')

def homepage(request):
    return render(request, 'homepage.html')

def homepage2(request):
    return render(request, 'homepage2.html')

def detail(request, num):
    list = HotSpot.objects.all()
    #list1=Hot.objects.all()
    # 实现分页功能
    paginator = Paginator(list, 8)
    if num > 100:
        num = 1
    page = paginator.page(num)

    return render(request, 'weibo.html', {'spotList': page})

def detail1(request, num):
    path = "E:/Python/WeiboYouth/log4j.txt"
    log4j = Log4j()
    list = HotSpot.objects.all()
    #list1=Hot.objects.all()
    # 实现分页功能
    paginator = Paginator(list, 8)
    if num > 100:
        num = 1
    page = paginator.page(num)

    content="管理员打开头条界面"
    log4j.writelog(path,content)
    return render(request, 'weibo1.html', {'spotList': page})


def detail2(request, num):
    path = "E:/Python/WeiboYouth/log4j.txt"
    log4j = Log4j()
    list = ControlledHotSpot.objects.all()
    paginator = Paginator(list, 8)
    if num > 100:
        num = 1
    page = paginator.page(num)

    content = "管理员打开引导界面"
    log4j.writelog(path, content)
    return render(request, 'controlledweibo3.html', {'spotList': page})

def detail3(request, num):
    path = "E:/Python/WeiboYouth/log4j.txt"
    log4j = Log4j()
    list = ControlledHotSpot1.objects.all()
    paginator = Paginator(list, 8)
    if num > 100:
        num = 1
    page = paginator.page(num)
    content = "管理员打开控管界面"
    log4j.writelog(path, content)
    return render(request, 'controlledweibo.html', {'spotList': page})

def detail4(request, num):
    path = "E:/Python/WeiboYouth/log4j.txt"
    log4j = Log4j()
    list = ControlledHotSpot1.objects.all()
    paginator = Paginator(list, 8)
    if num > 100:
        num = 1
    page = paginator.page(num)
    content = "用户打开头条界面"
    log4j.writelog(path, content)
    return render(request, 'controlledweibo1.html', {'spotList': page})

def detail5(request, num):
    path = "E:/Python/WeiboYouth/log4j.txt"
    log4j = Log4j()
    list = ControlledHotSpot.objects.all()
    paginator = Paginator(list, 8)
    if num > 100:
        num = 1
    page = paginator.page(num)
    content = "用户打开热点界面"
    log4j.writelog(path, content)
    return render(request, 'controlledweibo4.html', {'spotList': page})

def register(request):
    path = "E:/Python/WeiboYouth/log4j.txt"
    log4j = Log4j()
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            email = userform.cleaned_data['email']

            User.objects.create(username=username,password=password,email=email)

            content="管理员"+username+"注册成功"
            log4j.writelog(path,content)
            #User.save()
            #return HttpResponse('regist success!!!')
            return render(request, 'weibo1.html', {'userform': userform})
            #return render(request, 'homepage.html', {'userform': userform})
            #return login(request.method == 'POST')
    else:
        userform = UserForm()
    return render(request,'register.html',{'userform':userform})

def register1(request):
    path = "E:/Python/WeiboYouth/log4j.txt"
    log4j = Log4j()
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            email = userform.cleaned_data['email']

            User1.objects.create(username=username,password=password,email=email)

            content="用户"+username+"注册成功"
            log4j.writelog(path,content)
            #User.save()
            #return HttpResponse('regist success!!!')
            return render(request, 'weibo2.html', {'userform': userform})
            #return render(request, 'homepage.html', {'userform': userform})
            #return login(request.method == 'POST')
    else:
        userform = UserForm()
    return render(request,'register1.html',{'userform':userform})

def login(request):
    path = "E:/Python/WeiboYouth/log4j.txt"
    log4j = Log4j()
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']

            user = User.objects.filter(username__exact=username,password__exact=password)

            content = "管理员"+username+"登陆成功"
            log4j.writelog(path,content)

            if user:
                return render(request,'weibo1.html',{'userform':userform})
                #return render(request, "/homepage/")
            else:
                return HttpResponse('用户名或密码错误,请重新登录')

    else:
        userform = UserForm()
    return render(request,'login.html',{'userform':userform})

def login1(request):
    path = "E:/Python/WeiboYouth/log4j.txt"
    log4j = Log4j()
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']

            user = User1.objects.filter(username__exact=username,password__exact=password)

            content = "用户" + username + "登陆成功"
            log4j.writelog(path, content)

            if user:
                return render(request,'weibo2.html',{'userform':userform})
                #return render(request, "/homepage/")
            else:
                return HttpResponse('用户名或密码错误,请重新登录')

    else:
        userform = UserForm()
    return render(request,'login1.html',{'userform':userform})

def reg(request):
  path = "E:/Python/WeiboYouth/log4j.txt"
  log4j = Log4j()
  if request.method == 'POST':
    #key=KeywordProcesser()
    keyword=request.POST.get('keybord')
    keyword_processor = KeywordProcesser()
    keyword_processor.add_keyword_from_list(keyword)
    #HttpResponse(keyword_processor.keyword_count)
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="124088he",
        database="weibo1",
        charset="utf8mb4"
    )
    cursor = conn.cursor()
    sql = "select * from microblog_hotspot"
    cursor.execute(sql)
    data = cursor.fetchall()
    #sql1 = "delete from microblog_controlledhotspot where id < 10000"
    #cursor.execute(sql1)
    conn.commit()
    for i in data:
        if keyword_processor.extract_keywords(i[1]):
            sql2 = 'insert into microblog_controlledhotspot(id, content, author, publishTime, repost, comment, ' \
                   'approve, address) values (%s, %s, %s, %s, %s, %s, %s, %s)'
            HttpResponse(i)
            cursor.executemany(sql2, [i])
            conn.commit()
    cursor.close()
    conn.close()
    content="管理员匹配引导字符串“"+keyword+"”成功"
    log4j.writelog(path,content)
    return render(request,'weibo1.html')
    #pwd=request.POST.get('pwd')
  #print(name)
    #return HttpResponse(keyword)
  return render(request,'test1.html')

def read(request):
  path = "E:/Python/WeiboYouth/log4j.txt"
  log4j = Log4j()
  if request.method == 'POST':
    #key=KeywordProcesser()
    keyword=request.POST.get('keybord')
    keyword_processor = KeywordProcesser()
    keyword_processor.add_keyword_from_list(keyword)
    #HttpResponse(keyword_processor.keyword_count)
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="124088he",
        database="weibo1",
        charset="utf8mb4"
    )
    cursor = conn.cursor()
    sql = "select * from microblog_hotspot"
    cursor.execute(sql)
    data = cursor.fetchall()
    sql1 = "delete from microblog_controlledhotspot1 where id < 10000"
    cursor.execute(sql1)
    conn.commit()
    for i in data:
        if not keyword_processor.extract_keywords(i[1]):
            sql2 = 'insert into microblog_controlledhotspot1(id, content, author, publishTime, repost, comment, ' \
                   'approve, address) values (%s, %s, %s, %s, %s, %s, %s, %s)'
            HttpResponse(i)
            cursor.executemany(sql2, [i])
            conn.commit()
    cursor.close()
    conn.close()
    content = "管理员匹配屏蔽字符串“" + keyword + "”成功"
    log4j.writelog(path, content)
    return render(request,'weibo1.html')
    #pwd=request.POST.get('pwd')
  #print(name)
    #return HttpResponse(keyword)
  return render(request,'test2.html')