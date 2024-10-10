from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Member



# Create your views here.
def members_list(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('members/all_members.html')
    context = {
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))

def details(request,id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('members/details.html')
    context = {
        'mymember':mymember,
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template = loader.get_template('members/main.html')
    return HttpResponse(template.render())

def testing(request):
    mymembers = Member.objects.all()
    template = loader.get_template('members/template.html')
    context = {
        'mymembers':mymembers
    }
    return HttpResponse(template.render(context,request))