from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect

from .models import Pool, Choice
# Create your views here.

def index(request):
    poll = Pool.objects.all()
    return render(request, 'index.html', {'poll':poll})

def vote(request ,pollid):
    p = get_object_or_404(Pool, pk=pollid)
    choice_num = request.POST.get("which")
    if(choice_num is None):
        return HttpResponse("你沒選")
    choice = p.choice_set.get(pk=choice_num)
    choice.chount += 1
    choice.save()
    return HttpResponseRedirect("/detail/"+pollid)

def view(request ,pollid):
    p = get_object_or_404(Pool, pk=pollid)
    context = {'p':p,}
    return render(request,'view.html',context)

def detail(request, pollid):
    p = get_object_or_404(Pool,pk=pollid)
    context = {'p':p,}
    return render(request,"detail.html",context)
