from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required(login_url="login/")
def home(request):
    return render(request, 'main.html', {'STATIC_URL': settings.STATIC_URL})
