from django.views.generic.simple import direct_to_template, redirect_to

def index(request):
    return direct_to_template(request, 'calc/index.html')
