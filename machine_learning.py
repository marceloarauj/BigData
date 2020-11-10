from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

from grid_search_parameters import GSParameters

import numpy as np
import pickle as pk
import csv

class MachineLearning:

    def __init__(self,database):
        self.database = database
    
    def separateClasses(self):
        print('Parte 4 - Separando classes')

        x = []
        y = []
        label = 0
        
        for classes in self.database:

            label = label + 1

            for image in self.database[classes]:
                x.append(image)
                y.append(label)

        self.database = {"x":np.array(x),"y":np.array(y)}

    def crossValidation(self,epochs,model,scoring_option):
        
        score = cross_val_score(
            model,
            self.database["x"].reshape((-1,28 * 28)),
            self.database["y"],
            scoring=scoring_option,
            cv=epochs,
        )

        print("{}: {}".format(scoring_option,score))
        return score

    def gridSeach(self,model,parameters,scoring_option):

        grid_seach = GridSearchCV(model,parameters,scoring=scoring_option)
        grid_seach.fit(self.database["x"].reshape((-1,28 * 28)),
                       self.database["y"])

        return grid_seach.best_params_

    def bestKNNModel(self,knn_parameters):
        return KNeighborsClassifier(
            n_neighbors= knn_parameters['n_neighbors'],
            leaf_size=knn_parameters['leaf_size'],
            weights=knn_parameters['weights'],
            p=knn_parameters['p']
        )
    
    def bestRForestModels(self,rf_parameters):
        return RandomForestClassifier(
            criterion= rf_parameters['criterion'],
            bootstrap=rf_parameters['bootstrap'],
            max_depth=rf_parameters['max_depth'],
            min_samples_split=rf_parameters['min_samples_split'],
            ccp_alpha=rf_parameters['ccp_alpha']
        )
    
    def bestDTreeModel(self,dt_parameters):
        return DecisionTreeClassifier(
            criterion=dt_parameters['criterion'],
            splitter=dt_parameters['splitter'],
            max_depth=dt_parameters['max_depth'],
            ccp_alpha=dt_parameters['ccp_alpha']
        )
    
    def bestNBModel(self,nb_parameters):
        return BernoulliNB(
            alpha= nb_parameters['alpha'],
            fit_prior=nb_parameters['fit_prior']
        )

    def exportModel(self,filename,model,metric):
        pk.dump(model,open('ExportedModels/'+metric+'_'+filename,'wb'))
    
    def importModel(self,filename):
        return pk.load(open('ExportedModels/' + filename,'rb'))
    
    def exportMetricsAsCSV(self,filename,data):
        print('')

    #Lista de Execuções
    def executeTrain(self):

        self.separateClasses()

        print("\nParte 5 - Executando Grid Searchs , isso pode levar algum tempo...")
        
        gs_parameters = GSParameters()
        
        knn = KNeighborsClassifier()
        random_forest = RandomForestClassifier()
        decision_tree = DecisionTreeClassifier()
        naive_bayes = BernoulliNB()

        print("\nObtendo melhores parâmetros para accuracy")
        #Melhores parâmetros de accuracy
        knn_parameters_accuracy = self.gridSeach(knn,gs_parameters.knnParameters(),'accuracy')
        rf_parameters_accuracy = self.gridSeach(random_forest,gs_parameters.randomForestParameters(),'accuracy')
        dt_parameters_accuracy = self.gridSeach(decision_tree,gs_parameters.decisionTreeParameters(),'accuracy')
        nb_parameters_accuracy = self.gridSeach(naive_bayes,gs_parameters.bernoulliParamaters(),'accuracy')

        knn = KNeighborsClassifier()
        random_forest = RandomForestClassifier()
        decision_tree = DecisionTreeClassifier()
        naive_bayes = BernoulliNB()

        print("\nObtendo melhores parâmetros para f1")
        #Melhores parâmetros de f1
        knn_parameters_f1 = self.gridSeach(knn,gs_parameters.knnParameters(),'f1_macro')
        rf_parameters_f1 = self.gridSeach(random_forest,gs_parameters.randomForestParameters(),'f1_macro')
        dt_parameters_f1 = self.gridSeach(decision_tree,gs_parameters.decisionTreeParameters(),'f1_macro')
        nb_parameters_f1 = self.gridSeach(naive_bayes,gs_parameters.bernoulliParamaters(),'f1_macro')

        knn = KNeighborsClassifier()
        random_forest = RandomForestClassifier()
        decision_tree = DecisionTreeClassifier()
        naive_bayes = BernoulliNB()

        print("\nObtendo melhores parâmetros para precision")
        #Melhores parâmetros de precision
        knn_parameters_precision = self.gridSeach(knn,gs_parameters.knnParameters(),'precision_macro')
        rf_parameters_precision = self.gridSeach(random_forest,gs_parameters.randomForestParameters(),'precision_macro')
        dt_parameters_precision = self.gridSeach(decision_tree,gs_parameters.decisionTreeParameters(),'precision_macro')
        nb_parameters_precision = self.gridSeach(naive_bayes,gs_parameters.bernoulliParamaters(),'precision_macro')

        knn = KNeighborsClassifier()
        random_forest = RandomForestClassifier()
        decision_tree = DecisionTreeClassifier()
        naive_bayes = BernoulliNB()

        print("\nObtendo melhores parâmetros para recall")
        #Melhores parâmetros de recall
        knn_parameters_recall = self.gridSeach(knn,gs_parameters.knnParameters(),'recall_macro')
        rf_parameters_recall = self.gridSeach(random_forest,gs_parameters.randomForestParameters(),'recall_macro')
        dt_parameters_recall = self.gridSeach(decision_tree,gs_parameters.decisionTreeParameters(),'recall_macro')
        nb_parameters_recall = self.gridSeach(naive_bayes,gs_parameters.bernoulliParamaters(),'recall_macro')

        print('\nParte 6 - Treinando modelos com os melhores parametros')
    
        print('\nAlgoritmo KNN')
        knn_accuracy = self.bestKNNModel(knn_parameters_accuracy)
        knn_accuracy_results = self.crossValidation(5,knn_accuracy,'accuracy')

        knn_f1 = self.bestKNNModel(knn_parameters_f1)
        knn_f1_results = self.crossValidation(5,knn_f1,'f1_macro')

        knn_precision = self.bestKNNModel(knn_parameters_precision)
        knn_precision_results = self.crossValidation(5,knn_precision,'precision_macro')

        knn_recall = self.bestKNNModel(knn_parameters_recall)
        knn_recall_results = self.crossValidation(5,knn_recall,'recall_macro')

        print('\nAlgoritmo RandomForest')

        random_forest_accuracy = self.bestRForestModels(rf_parameters_accuracy)
        random_forest_accuracy_results = self.crossValidation(5,random_forest_accuracy,'accuracy')

        random_forest_f1 = self.bestRForestModels(rf_parameters_f1)
        random_forest_f1_results = self.crossValidation(5,random_forest_f1,'f1_macro')

        random_forest_precision = self.bestRForestModels(rf_parameters_precision)
        random_forest_precision_results = self.crossValidation(5,random_forest_precision,'precision_macro')

        random_forest_recall = self.bestRForestModels(rf_parameters_recall)
        random_forest_recall_results = self.crossValidation(5,random_forest_recall,'recall_macro')

        print('\nAlgoritmo DecisionTree')

        decision_tree_accuracy = self.bestDTreeModel(dt_parameters_accuracy)
        decision_tree_accuracy_results = self.crossValidation(5,decision_tree_accuracy,'accuracy')

        decision_tree_f1 = self.bestDTreeModel(dt_parameters_f1)
        decision_tree_f1_results = self.crossValidation(5,decision_tree_f1,'f1_macro')

        decision_tree_precision = self.bestDTreeModel(dt_parameters_precision)
        decision_tree_precision_results = self.crossValidation(5,decision_tree_precision,'precision_macro')

        decision_tree_recall = self.bestDTreeModel(dt_parameters_recall)
        decision_tree_recall_results = self.crossValidation(5,decision_tree_recall,'recall_macro')

        print('\nAlgoritmo NaiveBayes')

        naive_bayes_accuracy = self.bestNBModel(nb_parameters_accuracy)
        naive_bayes_accuracy_results = self.crossValidation(5,naive_bayes_accuracy,'accuracy')

        naive_bayes_f1 = self.bestNBModel(nb_parameters_f1)
        naive_bayes_f1_results = self.crossValidation(5,naive_bayes_f1,'f1_macro')

        naive_bayes_precision = self.bestNBModel(nb_parameters_precision)
        naive_bayes_precision_results = self.crossValidation(5,naive_bayes_precision,'precision_macro')

        naive_bayes_recall = self.bestNBModel(nb_parameters_recall)
        naive_bayes_recall_results = self.crossValidation(5,naive_bayes_recall,'recall_macro')

        print('\nParte 7 - Exportando módulos')

        self.exportModel('knn.sav',knn_accuracy,'accuracy')
        self.exportModel('random_forest.sav',random_forest_accuracy,'accuracy')
        self.exportModel('decision_tree.sav',decision_tree_accuracy,'accuracy')
        self.exportModel('bernoulli.sav',naive_bayes_accuracy,'accuracy')

        self.exportModel('knn.sav',knn_f1,'f1')
        self.exportModel('random_forest.sav',random_forest_f1,'f1')
        self.exportModel('decision_tree.sav',decision_tree_f1,'f1')
        self.exportModel('bernoulli.sav',naive_bayes_f1,'f1')

        self.exportModel('knn.sav',knn_precision,'precision')
        self.exportModel('random_forest.sav',random_forest_precision,'precision')
        self.exportModel('decision_tree.sav',decision_tree_precision,'precision')
        self.exportModel('bernoulli.sav',naive_bayes_precision,'precision')

        self.exportModel('knn.sav',knn_recall,'recall')
        self.exportModel('random_forest.sav',random_forest_recall,'recall')
        self.exportModel('decision_tree.sav',decision_tree_recall,'recall')
        self.exportModel('bernoulli.sav',naive_bayes_recall,'recall')