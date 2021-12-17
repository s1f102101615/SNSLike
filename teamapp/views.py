from django.shortcuts import render, redirect
from teamapp.models import Article,Comment
# Create your views here.

def index(request):
    if ('sort' in request.GET):
        if request.GET['sort'] == 'like':
            articles = Article.objects.order_by('-like')
        else:
            articles = Article.objects.order_by('-posted_at')
    else:
        articles = Article.objects.order_by('-posted_at')

    context = {
        "articles": articles
    }
    
    return render(request, 'teamapp/index.html', context)


def post(request):
    if request.method == 'POST':
        article = Article(body=request.POST['text'], img=request.POST['Article-image'])
        article.save()
        return redirect(index, article)