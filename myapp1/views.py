from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from myapp1.models import *

def create_topic(request):
    if request.method=="POST":
        topic=request.POST.get("topic")
        t=topic.objects.get_or_create(topic_name=topic)
        if t[1]==True:
            t[0].save()
            return HttpResponse("<h3>Topic Added Successfully</h3>")
        else:
            return HttpResponse("<h3>Topic Is Already Exist In Table</h3>")
    return render(request,"create_topic.html")

def create_webpage(request):
    if request.method=="POST":
        topic=request.POST.get('topic')
        name=request.POST.get('name')
        url=request.POST.get("url")
        t=topic.objects.get_or_create(topic_name=topic)[0]
        w=webpage.objects.get_or_create(topic=t,name=name,url=url)[0]
        w.save()
        return HttpResponse("<h3>Webpage Added Successfully</h3>")
    topics=topic.objects.all()
    return render(request,"create_webpage.html",context={'topic':topics})