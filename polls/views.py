from django.http import HttpResponse



def index(self, request):
    return HttpResponse("Hello, world. You're at the polls index.")