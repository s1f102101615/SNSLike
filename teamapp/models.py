from django.db import models
from teamapp.models import Article
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your models here.

def post(request):
    return  render(request, 'teamapp/post.html')