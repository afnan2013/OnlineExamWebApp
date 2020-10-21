from django.http import HttpResponse


def index(request):
    return HttpResponse("Hi... Everything is working fine!!!")
