from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect, HttpResponse

# Create your views here.
from .models import BlogPost

def blog(request):
    print(request)
    bps = BlogPost.objects.order_by("-id")
    content = {'bps':bps}
    return render(request, 'blog.html', content)

def post(request):
    bp = BlogPost()
    print(request)
    bp.title = request.POST.get("title")
    bp.Content = request.POST.get("Content")
    bp.save()
    return HttpResponseRedirect("/blog/")

def delpost(request, poid):
    bp = get_object_or_404(BlogPost, pk=poid)
    bp.delete()
    return HttpResponseRedirect("/blog/")

def editpost(request, poid):
    bp = get_object_or_404(BlogPost, pk=poid)
    bp.title = request.POST.get("title")
    bp.Content = request.POST.get("Content")
    bp.save()
    return HttpResponseRedirect("/blog/")