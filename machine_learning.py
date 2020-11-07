from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

from grid_search_parameters import GSParameters

import numpy as np
import pickle as pk

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

    def crossValidation(self,epochs,model):
        
        score = cross_val_score(
            model,
            self.database["x"].reshape((-1,28 * 28)),
            self.database["y"],
            scoring='accuracy',
            cv=epochs
        )

        print("Score: {}".format(score))

    def gridSeach(self,model,parameters):

        grid_seach = GridSearchCV(model,parameters,scoring="accuracy")
        grid_seach.fit(self.database["x"].reshape((-1,28 * 28)),
                       self.database["y"])

        return grid_seach.best_params_

    def fitModel(self,model):

        model.fit(
            self.database["x"].reshape((-1,28 * 28)),
            self.database["y"]
            ) 
        return model

    def predict(self,trainned_model):
        predict = trainned_model.predict([np.ones(28 * 28)])
        return predict

    #Lista de Execuções
    def executeTrain(self):

        self.separateClasses()

        print("\nParte 5 - Executando Grid Search , isso pode levar algum tempo...")
        
        gs_parameters = GSParameters()
        
        knn = KNeighborsClassifier()
        random_forest = RandomForestClassifier()
        decision_tree = DecisionTreeClassifier()
        naive_bayes = BernoulliNB()

        knn_parameters = self.gridSeach(knn,gs_parameters.knnParameters())
        rf_parameters = self.gridSeach(random_forest,gs_parameters.randomForestParameters())
        dt_parameters = self.gridSeach(decision_tree,gs_parameters.decisionTreeParameters())
        nb_parameters = self.gridSeach(naive_bayes,gs_parameters.bernoulliParamaters())

        print('\nParte 6 - Treinando modelos com os melhores parametros')
    
        print('\nAlgoritmo KNN')
        knn = KNeighborsClassifier(
            n_neighbors= knn_parameters['n_neighbors'],
            leaf_size=knn_parameters['leaf_size'],
            weights=knn_parameters['weights'],
            p=knn_parameters['p']
        )
        self.crossValidation(5,knn)


        print('\nAlgoritmo RandomForest')
        random_forest = RandomForestClassifier(
            criterion= rf_parameters['criterion'],
            bootstrap=rf_parameters['bootstrap'],
            max_depth=rf_parameters['max_depth'],
            min_samples_split=rf_parameters['min_samples_split'],
            ccp_alpha=rf_parameters['ccp_alpha']
        )
        self.crossValidation(5,random_forest)

        print('\nAlgoritmo DecisionTree')
        decision_tree = DecisionTreeClassifier(
            criterion=dt_parameters['criterion'],
            splitter=dt_parameters['splitter'],
            max_depth=dt_parameters['max_depth'],
            ccp_alpha=dt_parameters['ccp_alpha']
        )
        self.crossValidation(5,decision_tree)

        print('\nAlgoritmo NaiveBayes')
        naive_bayes = BernoulliNB(
            alpha= nb_parameters['alpha'],
            fit_prior=nb_parameters['fit_prior']
        )
        self.crossValidation(5,naive_bayes)
        print('\nParte 7 - Exportando módulos')

        self.exportModel('knn.sav',knn)
        self.exportModel('random_forest.sav',random_forest)
        self.exportModel('decision_tree.sav',decision_tree)
        self.exportModel('bernoulli.sav',naive_bayes)

    def exportModel(self,filename,model):
        pk.dump(model,open('ExportedModels/'+filename,'wb'))
    
    def importModel(self):
        print('')
    