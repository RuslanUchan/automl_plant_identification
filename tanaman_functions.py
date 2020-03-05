import os

from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2


# 'content' is base-64-encoded image data.
def get_prediction(request):
    request_json = request.get_json()
    
    if request_json and 'content' in request_json:
        content = request_json['content']
        
        prediction_client = automl_v1beta1.PredictionServiceClient()
	
        project_id = os.environ.get('PROJECT_ID', 'No Project ID is supplied')
        model_id = os.environ.get('MODEL_ID', 'No Model ID is supplied')

        name = 'projects/{}/locations/us-central1/models/{}'.format(
            project_id, model_id)
        payload = {'image': {'image_bytes': content}}
        params = {}
        request = prediction_client.predict(name, payload, params)

        print(request)

        return request  # waits till request is returned
    else:
        return f'Pastikan data sudah benar'