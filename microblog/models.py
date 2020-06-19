from django.db import models
from django.contrib import admin
# Create your models here.


class HotSpot(models.Model):

    content = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publishTime = models.CharField(max_length=255)
    repost = models.IntegerField()
    comment = models.IntegerField()
    approve = models.IntegerField()
    address = models.URLField()

    # 排序
    class Meta:
        ordering = ['-id']

class ControlledHotSpot(models.Model):
    content = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publishTime = models.CharField(max_length=255)
    repost = models.IntegerField()
    comment = models.IntegerField()
    approve = models.IntegerField()
    address = models.URLField()

    # 排序
    class Meta:
        ordering = ['-id']

class ControlledHotSpot1(models.Model):
    content = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publishTime = models.CharField(max_length=255)
    repost = models.IntegerField()
    comment = models.IntegerField()
    approve = models.IntegerField()
    address = models.URLField()

    # 排序
    class Meta:
        ordering = ['-id']

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()

class User1(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','password','email')

admin.site.register(User,UserAdmin)

