from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    template = "index.html"
    return render(request, template)

# def counter(request):
#     text = request.POST['text']
#    # amount_of_words = len(text.split())
#     return  render(request,'counter.html', {'text':text})