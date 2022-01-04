from django.db import models
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model):
    image = models.ImageField(upload_to='Article-image',blank=True, null=True)
    # title = models.CharField(max_length=200)
    body = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    ## published_at = models.DateTimeField(blank=True, null=True)
    like = models.IntegerField(default=0)
    post_user = models.TextField(max_length=150)
    
    #def publish(self):
        #self.published_at = timezone.now()
        #self.save()
    #def __str__(self):
        #return self.title
class Comment(models.Model):
    text = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)

#アカウント追加
class Account(models.Model):

    # ユーザー認証のインスタンス(1vs1関係)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #アカウント画像
    account_image = models.ImageField(upload_to="profile_pics",blank=True)

    def __str__(self):
        return self.user.username