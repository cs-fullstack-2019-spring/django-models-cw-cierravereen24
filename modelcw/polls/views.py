from django.http import HttpResponse


# Create your views here.

# function for when the default page if you dont specifically choose which one you want
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
