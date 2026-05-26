from apiflask import APIFlask
from .model_provider import ModelProvider
from .utils import ModelData, ResponseModel
from .my_logger import log
import os

app = APIFlask(__name__, title="Model API", version="1.0")


provider = ModelProvider()
provider.load_model('model_payment_next_month')


@app.get('/health')
def health_check():
    return {'status': 'ok'}

@app.post("/prediction")
@app.output(ResponseModel, status_code=200)
@app.input(ModelData, location="json")
def get_prediction(json_data):

    prediction = provider.predict(json_data)

    log('Get Prediction', f'Model prediction={prediction}')
    
    return ResponseModel(prediction=prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)