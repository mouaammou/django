from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.


def default(request):
	hame_page = loader.get_template("home.html")
	return HttpResponse(hame_page.render())

def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())

def members(request):
    all_members = Member.objects.all().values()
    template = loader.get_template("all_members.html")
    context = {"members": all_members}
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        "member": mymember,
    }
    return HttpResponse(template.render(context, request))