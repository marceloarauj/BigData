from flask import Flask,request
from services import PredictServices

app = Flask(__name__)
services = PredictServices()

@app.route('/predict',methods=['POST'])
def postPredict():

    body = request.json

    metrics = body['metrics']
    model = body['model']
    image = body['image']

    return services.predict(image,model,metrics)


if __name__ == '__main__':
    app.run()    