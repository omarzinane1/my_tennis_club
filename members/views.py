from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from .models import Member

def members(request):
    mymembers = Member.objects.all().values()
    tamplate = loader.get_template('all_members.html')
    context = {
        'mymembers':mymembers
    }
    return HttpResponse(tamplate.render(context, request))

def details(request, id):
    member = Member.objects.get(id=id)
    tamplate = loader.get_template('details.html')
    context = {
        'mymember':member
    }
    return HttpResponse(tamplate.render(context, request))

def main(request):
    tamplate = loader.get_template('main.html')
    return HttpResponse(tamplate.render())


def testing(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
