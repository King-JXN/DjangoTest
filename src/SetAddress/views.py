from django.shortcuts import render_to_response
from django.template import loader, Context
from django.http.response import HttpResponse
from SetAddress.models import SetAddressPostInfor

# Create your views here.

def loadDisplayInfor(request):
    posts = SetAddressPostInfor.objects.all();
    t = loader.get_template("addressArchieve.html")
    c = Context({'posts':posts})
    return render_to_response("addressArchieve.html", HttpResponse(t.render(c)))
