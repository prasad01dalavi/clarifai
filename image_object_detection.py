from clarifai.rest import ClarifaiApp

image_path = 'car.jpg'
app = ClarifaiApp(api_key='aa53cdc859b84d4d95190962e8613c9a')
model = app.models.get('general-v1.3')

response = model.predict_by_filename(filename=image_path)
concepts = response['outputs'][0]['data']['concepts']

for concept in concepts:
    print concept['name'], '|', concept['value']
