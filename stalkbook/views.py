import flickrapi
import json
import re
import utils

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings


from django.shortcuts import render
from django.template import Context, loader


def home(req):
    return HttpResponse("Welcome to homepage")

# It returns all the urls for photos with the given tag


def images_extract(request):
    flickr_photos = utils.get_flickr_images("sunset")
    photos = json.dumps(flickr_photos)
    return HttpResponse(photos)
