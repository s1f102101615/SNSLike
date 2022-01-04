from .models import Article, Account
from django import forms
from django.contrib.auth.models import User

#記事投稿用
class Goto_form(forms.ModelForm):
    class Meta: 
        model=Article
        fields = ('image','body')
    #class Meta:
        ##fields = ('image','body')

#新規アカウント登録フォーム
class AccountForm(forms.ModelForm):
    # パスワード入力：非表示対応
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        # ユーザー認証
        model = User
        # フィールド指定
        fields = ('username','email','password')
        # フィールド名指定
        labels = {'username':"ユーザーID",'email':"メール"}

class AddAccountForm(forms.ModelForm):
    class Meta():
        # モデルクラスを指定
        model = Account
        fields = ('account_image',)
        labels = {'account_image':"写真アップロード",}