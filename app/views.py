from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def Insert_Topic(request):
    TO=input('Enter the topic_name: ')
    TO=Topic.objects.get_or_create(topic_name=TO)[0]
    return HttpResponse('topic insertion is succussfully')
    TO.save()



      
