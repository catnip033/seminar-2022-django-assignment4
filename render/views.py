from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('hello 김유신!')
