from django.db import models
from teamapp.models import Article
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models
from django.utils import timezone
# Create your models here.

def post(request):
    if request.method == 'POST':
        article = Article(body=request.POST['text'], img =request.POST['Article-image'])
        article.save()
    return  render(request, 'teamapp/post.html')

class Article(models.Model):
    img = models.ImageField(upload_to='/Article-image')
    # title = models.CharField(max_length=200)
    body = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    ## published_at = models.DateTimeField(blank=True, null=True)
    like = models.IntegerField(default=0)
    #def publish(self):
        #self.published_at = timezone.now()
        #self.save()
    #def __str__(self):
        #return self.title
class Comment(models.Model):
    text = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)