from django.shortcuts import render_to_response
from django.template import loader, Context
# from django.template import loader, RequestContext
from django.http import HttpResponse
from Blog.models import BlogPost
from django.template.context import RequestContext

# Create your views here.

def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("archieve.html")
    c = Context({'posts':posts})
#     return HttpResponse(t.render(c))
    return render_to_response("archieve.html", HttpResponse(t.render(c)))
#     return HttpResponse("Hello, world.")