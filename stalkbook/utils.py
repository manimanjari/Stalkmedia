import flickrapi
import json

from django.conf import settings


def get_flickr_images(tag_entered):
    api_key = settings.API_KEY
    api_secret = settings.API_SECRET
    photo_list = {}
    photo_count = 0

    flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
    all_photos = flickr.photos.search(api_key=api_key, tags=tag_entered)
    for photo in all_photos['photos']['photo']:
        title = photo['title']
        if not title:
            title = tag_entered
        farm_id = str(photo['farm'])
        server_id = str(photo['server'])
        individual_id = str(photo['id'])
        secret_id = str(photo['secret'])
        photo_url = (
            'http://farm{farm_id}.static.flickr.com/{server_id}/'
            '{individual_id}_{secret_id}.jpg'.format(
                farm_id=farm_id, server_id=server_id,
                individual_id=individual_id, secret_id=secret_id))
        photo_list[title] = photo_url
    return photo_list
