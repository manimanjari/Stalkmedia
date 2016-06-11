import json
import re
import utils

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings


import flickrapi

from django.shortcuts import render
from django.template import Context, loader


def home(request):
    return render(request, 'main.html', {'STATIC_URL': settings.STATIC_URL})


def fetch_images_by_tag(request):
    tag_entered = request.GET['q']
    flickr_photos = utils.get_flickr_images(tag_entered)
    photos = json.dumps(flickr_photos)
    return HttpResponse(photos)
