from django.shortcuts import render

# Create your views here.
def index(request):
    # display an index page
    return render(request, "index.html")
