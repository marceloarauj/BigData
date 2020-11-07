from image_handler import ImageHandler
from machine_learning import MachineLearning
from flask import Flask

app = Flask(__name__)

@app.route('/knn')
def postPredictKNN():
    return 'teste'

@app.route('/rf')
def postPredictRandomForest():
    print('')

@app.route('/dt')
def postPredictDecisionTree():
    print('')

@app.route('/nb')
def postPredictBernoulli():
    print('')


if __name__ == '__main__':
    app.run()    