import pickle as pk
from image_handler import ImageHandler
from machine_learning import MachineLearning

class PredictServices:

    def __init__(self):        
        self.initMachineLearningModels()
    
    machine_learning = MachineLearning({})

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
        
    
    def predict(self,image,model_name,metric):
        
        if model_name == 'knn' and metric == 'accuracy':
            print('')

        if model_name == 'knn' and metric == 'f1':
            print('')

        if model_name == 'knn' and metric == 'precision':
            print('')

        if model_name == 'knn' and metric == 'recall':
            print('')

        if model_name == 'random_forest' and metric == 'accuracy':
            print('')

        if model_name == 'random_forest' and metric == 'f1':
            print('')

        if model_name == 'random_forest' and metric == 'precision':
            print('')

        if model_name == 'random_forest' and metric == 'recall':
            print('')

        if model_name == 'decision_tree' and metric == 'accuracy':
            print('')

        if model_name == 'decision_tree' and metric == 'f1':
            print('')

        if model_name == 'decision_tree' and metric == 'precision':
            print('')

        if model_name == 'decision_tree' and metric == 'recall':
            print('')

        if model_name == 'naive_bayes' and metric == 'accuracy':
            print('')

        if model_name == 'naive_bayes' and metric == 'f1':
            print('')

        if model_name == 'naive_bayes' and metric == 'precision':
            print('')

        if model_name == 'naive_bayes' and metric == 'recall':
            print('')