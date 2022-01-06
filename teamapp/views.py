from django.shortcuts import render, redirect
from teamapp.models import Account, Article, Comment
from django.http import Http404, JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .forms import Goto_form, AccountForm, AddAccountForm 
from django.views.generic import TemplateView
from django.contrib.auth import authenticate
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
        "form":form,
        "UserID":request.user,
    }
    
    return render(request, 'teamapp/index.html', context)


def post(request):
    if request.method == 'GET':
        if request.user.is_anonymous:
            return redirect('registration')
    #if  None == user:
        #return redirect('index')
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
        article.image = request.FILES['image']
        if request.POST:
            article.body = request.POST['body']
        #アカウント    
        article.post_user = request.user
        article.save()
        return redirect('index')
    return render(request, 'teamapp/post.html', {'form': form,'UserID': request.user})

def like(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
        article.like += 1
        article.save()
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
        
    return redirect(index, article_id)

def api_like(request,article_id):
    try:
        article=Article.objects.get(pk=article_id)
        article.like+=1
        article.save()
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    result={
        'id': article_id,
        'like': article.like
    }
    return JsonResponse(result)

#アカウント新規登録
class  AccountRegistration(TemplateView):

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        "add_account_form":AddAccountForm(),
        }

    # Get処理
    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["add_account_form"] = AddAccountForm()
        self.params["AccountCreate"] = False
        return render(request,"teamapp/register.html",context=self.params)

    # Post処理
    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)
        self.params["add_account_form"] = AddAccountForm(data=request.POST)

        # フォーム入力の有効検証
        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            # アカウント情報をDB保存
            account = self.params["account_form"].save()
            # パスワードをハッシュ化
            account.set_password(account.password)
            # ハッシュ化パスワード更新
            account.save()

            # 下記追加情報
            # 下記操作のため、コミットなし
            add_account = self.params["add_account_form"].save(commit=False)
            # AccountForm & AddAccountForm 1vs1 紐付け
            add_account.user = account

            # 画像アップロード有無検証
            if 'account_image' in request.FILES:
                add_account.account_image = request.FILES['account_image']

            # モデル保存
            add_account.save()

            # アカウント作成情報更新
            self.params["AccountCreate"] = True
            return redirect('Login')

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

        return render(request,"teamapp/register.html",context=self.params)

    
#ログイン
def Login(request):
    # POST
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)

        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('index'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'teamapp/login.html')

#ログアウト
@login_required
def Logout(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('index'))


def userpage(request):
    userpageid = request.GET['userpageid']
    if ('sort' in request.GET):
        if request.GET['sort'] == 'like':
            articles = Article.objects.order_by('-like').filter(post_user = userpageid)
        else:
            articles = Article.objects.filter(post_user = userpageid)
            articles = Article.objects.order_by('-posted_at')
    else:
        articles = Article.objects.filter(post_user = userpageid)
        articles = Article.objects.order_by('-posted_at')
    form = Goto_form()
    articles = Article.objects.filter(post_user = userpageid)
    context = {
        "articles": articles,
        "form":form,
        "UserID":request.user
    }
    
    return render(request, 'teamapp/userpage.html', context)


