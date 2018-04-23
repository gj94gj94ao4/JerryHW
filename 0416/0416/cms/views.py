from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Student


def index(request):
    student = Student.objects.all()
    return render_to_response('cms/menu.html', locals())