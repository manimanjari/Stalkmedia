import flickrapi
import json


def get_flickr_images(tag_entered):
    api_key = u'55f0cde720c94ed849661690881c01ea'
    api_secret = u'e7c9bdfaede2036b'
    photo_list = []
    photo_json = {}
    photo_count = 0

    flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
    all_photos = flickr.photos.search(api_key=api_key, tags=tag_entered)
    for photo in all_photos['photos']['photo']:
        photo_details = all_photos['photos']['photo'][photo_count]
        photo_count = photo_count + 1
        title = photo_details['title']
        if not title:
            title = "sunset"
        farm_id = str(photo_details['farm'])
        server_id = str(photo_details['server'])
        individual_id = str(photo_details['id'])
        secret_id = str(photo_details['secret'])
        photo_url = 'http://farm{farm_id}.static.flickr.com/{server_id}/{individual_id}_{secret_id}.jpg'.format(
            farm_id=farm_id, server_id=server_id, individual_id=individual_id,
            secret_id=secret_id)
        photo_json['title'] = title
        photo_json['link'] = photo_url
        photo_list.append(photo_json.copy())
    photo_lists = json.dumps(photo_list)
    return photo_lists
