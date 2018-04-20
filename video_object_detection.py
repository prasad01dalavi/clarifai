from clarifai.rest import Video as ClVideo
from clarifai.rest import ClarifaiApp

import json
import codecs
from pprint import pprint

app = ClarifaiApp(api_key='aa53cdc859b84d4d95190962e8613c9a')
model = app.models.get('general-v1.3')

video = ClVideo(filename='video.mp4')
response = model.predict([video])
pprint(response)

# Save the response locally in json format
file_name = 'output_video' + '.json'
with codecs.open(file_name, 'w', 'utf-8') as ww:
    json.dump(response, ww, ensure_ascii=False, indent=2)
