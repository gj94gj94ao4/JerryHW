from django.shortcuts import render
from django.http import HttpResponse

from .models import Post
# Create your views here.


def index(request):
    if(request.method == 'POST'):
        name = request.POST.get("name")
        message = request.POST.get("message")
        post = Post()
        post.auther = name
        post.text = message
        post.save()
    return render(request,"index.html")

def detail(request):
    post = Post.objects.all()
    return render(request, 'detail.html',{'post':post,'request':request})
