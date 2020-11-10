from flask import Flask,request
from services import PredictServices

app = Flask(__name__)
services = PredictServices()

@app.route('/knn/accuracy',methods=['POST'])
def postPredictKNNAccuracy():
    
    return 'teste'

@app.route('/knn/f1')
def postPredictKNNF1():
    return 'teste'

@app.route('/knn/precision')
def postPredictKNNPrecision():
    return 'teste'

@app.route('/knn/recall')
def postPredictKNNRecall():
    return 'teste'

@app.route('/rf/accuracy')
def postPredictRandomForestAccuracy():
    print('')

@app.route('/rf/f1')
def postPredictRandomForestF1():
    print('')

@app.route('/rf/precision')
def postPredictRandomForestPrecision():
    print('')

@app.route('/rf/recall')
def postPredictRandomForestRecall():
    print('')

@app.route('/dt/accuracy')
def postPredictDecisionTreeAccuracy():
    print('')

@app.route('/dt/f1')
def postPredictDecisionTreeF1():
    print('')

@app.route('/dt/precision')
def postPredictDecisionTreePrecision():
    print('')

@app.route('/dt/recall')
def postPredictDecisionTreeRecall():
    print('')

@app.route('/nb/accuracy')
def postPredictBernoulliAccuracy():
    print('')

@app.route('/nb/f1')
def postPredictBernoulliF1():
    print('')

@app.route('/nb/precision')
def postPredictBernoulliPrecision():
    print('')

@app.route('/nb/recall')
def postPredictBernoulliRecall():
    print('')


if __name__ == '__main__':
    app.run()    