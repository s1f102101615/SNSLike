from django.shortcuts import render, redirect
from teamapp.models import Article, Comment
from django.http import Http404, JsonResponse
from django.http import HttpResponse
from django.utils import timezone
from .forms import Goto_form
# Create your views here.

def index(request):
    if ('sort' in request.GET):
        if request.GET['sort'] == 'like':
            articles = Article.objects.order_by('-like')
        else:
            articles = Article.objects.order_by('-posted_at')
    else:
        articles = Article.objects.order_by('-posted_at')
    form = Goto_form()
    context = {
        "articles": articles,
        "form":form
    }
    
    return render(request, 'teamapp/index.html', context)


def post(request):
    form = Goto_form()
    if request.method == 'POST':
        #article = Article(body=request.POST['text'], img=request.POST['Article-image'])
        #article = Article(body=request.POST['text'])
        #article.save()
        #return redirect(index)
        form = Goto_form(request.FILES,request.POST)
        if not request.FILES:
            return redirect('post')
        article = Article()
        print(request)
        article.image = request.FILES['image']
        if request.POST:
            article.body = request.POST['body']
        article.save()
        return redirect('index')
    return render(request, 'teamapp/post.html', {'form': form})

def like(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
        article.like += 1
        article.save()
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
        
    return redirect(index, article_id)