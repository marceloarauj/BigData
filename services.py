import pickle as pk
from image_handler import ImageHandler
from machine_learning import MachineLearning

class PredictServices:

    def __init__(self):        
        self.initMachineLearningModels()
    
    machine_learning = MachineLearning({})
    image_hander = ImageHandler()

    knn_accuracy ={}
    knn_f1 = {}
    knn_precision = {}
    knn_recall = {}

    random_forest_accuracy = {}
    random_forest_f1 = {}
    random_forest_precision = {}
    random_forest_recall = {}

    decision_tree_accuracy = {}
    decision_tree_f1 = {}
    decision_tree_precision = {}
    decision_tree_recall = {}

    naive_bayes_accuracy ={}
    naive_bayes_f1 ={}
    naive_bayes_precision ={}
    naive_bayes_recall ={}

    dict_models_metrics ={}

    classes = {
            1:'porta aviões',
            2:'alarme',
            3:'ambulância',
            4:'anjo',
            5:'formiga',
            6:'maçã',
            7:'braço',
            8:'machado',
            9:'urso',
            10:'abelha'
    }

    def initMachineLearningModels(self):
        self.knn_accuracy = self.machine_learning.importModel('accuracy_knn.sav')
        self.knn_f1 = self.machine_learning.importModel('f1_knn.sav')
        self.knn_precision = self.machine_learning.importModel('precision_knn.sav')
        self.knn_recall = self.machine_learning.importModel('recall_knn.sav')

        self.random_forest_accuracy = self.machine_learning.importModel('accuracy_random_forest.sav')
        self.random_forest_f1 = self.machine_learning.importModel('f1_random_forest.sav')
        self.random_forest_precision = self.machine_learning.importModel('precision_random_forest.sav')
        self.random_forest_recall = self.machine_learning.importModel('recall_random_forest.sav')

        self.decision_tree_accuracy = self.machine_learning.importModel('accuracy_decision_tree.sav')
        self.decision_tree_f1 = self.machine_learning.importModel('f1_decision_tree.sav')
        self.decision_tree_precision = self.machine_learning.importModel('precision_decision_tree.sav')
        self.decision_tree_recall = self.machine_learning.importModel('recall_decision_tree.sav')

        self.naive_bayes_accuracy = self.machine_learning.importModel('accuracy_bernoulli.sav')
        self.naive_bayes_f1 = self.machine_learning.importModel('f1_bernoulli.sav')
        self.naive_bayes_precision = self.machine_learning.importModel('precision_bernoulli.sav')
        self.naive_bayes_recall = self.machine_learning.importModel('recall_bernoulli.sav')
        
        self.dict_models_metrics = {
            'knn':{
                'accuracy': self.knn_accuracy,
                'f1': self.knn_f1,
                'precision': self.knn_precision,
                'recall':self.knn_recall
            },
            'random_forest':{
               'accuracy': self.random_forest_accuracy,
                'f1': self.random_forest_f1,
                'precision':self.random_forest_precision,
                'recall':self.random_forest_recall
            },
            'decision_tree':{
               'accuracy': self.decision_tree_accuracy,
                'f1':self.decision_tree_f1,
                'precision':self.decision_tree_precision,
                'recall': self.decision_tree_recall
            },
            'naive_bayes':{
               'accuracy':self.naive_bayes_accuracy,
                'f1':self.naive_bayes_f1,
                'precision':self.naive_bayes_precision,
                'recall':self.naive_bayes_recall
            }
        }
    
    def predict(self,image,model_name,metric):

        imagem = self.image_hander.imageFormater(image)
        model = self.dict_models_metrics[model_name][metric]
        classification = model.predict([imagem])

        return self.classes[classification[0]] 