from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Rendering the index.html template
