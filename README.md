# API Overview
This following API provides a browser-as-a-service for listing trending images given a tag to search. The result is returned as a Json response.

# API Documentation

## Getting list of trending images
Fetch images by tag


`GET /images/?q=nature%20photography`

## Output

```javascript
{
 {
  url: "http://farm8.static.flickr.com/7421/27600220515_66288337b8.jpg",
  title: "violet beauties."
 },
 {
  url: "http://farm8.static.flickr.com/7454/27321368660_d5372ab907.jpg",
  title: "White Throated Kingfisher!!"
 },
 {
  url: "http://farm8.static.flickr.com/7469/27599519975_340181d083.jpg",
  title: "Back Garden Plants"
 },
 {
 url: "http://farm8.static.flickr.com/7442/27526966411_4acb72a34e.jpg",
 title: "Butterfly Ready for Takeoff"
 },
}
```
**Request method:** GET

**URL Parameters:**
- (Required):
 q=[string]       
- ex: q=nature photography

**Success Response**
- 200 : Ok

**Error Response:**
- 400 : Bad Request
- 404 : Not found
- 503 : Service unavailable

