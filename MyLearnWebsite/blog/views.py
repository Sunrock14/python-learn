from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def blog(request):
    return HttpResponse("blog")

def blog_detail(request, id):
    return render(request, "blog/blog_detail.html" , {
        "id" : str(id)
    })