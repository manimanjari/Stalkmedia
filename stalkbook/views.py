import flickrapi
import json
import re
import webbrowser

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings


from django.shortcuts import render
from django.template import Context, loader


def home(req):
    return HttpResponse("hiii")

# It returns all the urls for photos with the given tag


def flickr_extract(request):
    api_key = u'55f0cde720c94ed849661690881c01ea'
    api_secret = u'e7c9bdfaede2036b'
    photo_list = []
    photo_json = {}
    flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
    all_photos = flickr.photos.search(api_key=api_key, tags="sunset")

    for i in range(50):
        photo_details = all_photos['photos']['photo'][i]
        farm_id = str(photo_details['farm'])
        server_id = str(photo_details['server'])
        individual_id = str(photo_details['id'])
        secret_id = str(photo_details['secret'])
        photo_url = 'http://farm' + farm_id + '.static.flickr.com/'
        + server_id + '/' + individual_id + '_' + secret_id + '.jpg'
        photo_json['link'] = photo_url
        photo_list.append(photo_json.copy())
    photo_lists = json.dumps(photo_list)
    return HttpResponse(photo_lists)
