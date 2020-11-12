from flask import Flask,request,jsonify
from flask_cors import CORS
from services import PredictServices

app = Flask(__name__)
cors = CORS(app,resources={r"/predict":{"origins":"*"}})

services = PredictServices()

@app.route('/predict',methods=['POST'])
def postPredict():
    body = request.json
    print(body)
    metrics = body['metrics']
    print(metrics)
    model = body['model']
    image = body['image']

    response = services.predict(image,model,metrics)
    return jsonify({'class':response})


if __name__ == '__main__':
    app.run()    