from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from StringIO import *


# Read the image and convert it into raw bytes
def read_and_convert(filename):
    with open(filename, 'rb') as imgfile:
        return imgfile.read()    # Return image in raw bytes


image_path = 'car.jpg'
app = ClarifaiApp(api_key='aa53cdc859b84d4d95190962e8613c9a')
model = app.models.get('general-v1.3')

response = model.predict_by_filename(filename=image_path)
concepts = response['outputs'][0]['data']['concepts']

for concept in concepts:
    print concept['name'], '|', concept['value']
# -----------------------------------------------------------------------------

# Another method
img_bytes = read_and_convert(image_path)
# Note: I can provide response.content as raw image bytes
# This is in case of python requests

image = ClImage(file_obj=StringIO(img_bytes))
response = model.predict([image])
concepts = response['outputs'][0]['data']['concepts']

print 	# Leave a blank line
print 'Using another method to get the objects in an image'
for concept in concepts:
    print concept['name'], '|', concept['value']
