class GSParameters:

    def knnParameters(self):
        return{
            "n_neighbors":[4,6,8,10,20,30],
            "leaf_size":[5,10,20,25,30],
            "weights" : ['uniform', 'distance'],
            "p":[1,2]
        }

    def randomForestParameters(self):
        return {
            "criterion":['gini','entropy'],
            "bootstrap":[True,False],
            "max_depth":[10,15,20,25,30],
            "min_samples_split":[2,3,4,5,6,10],
            "ccp_alpha":[0.0, 0.1,0.4, 0.5]
        }

    def decisionTreeParameters(self):
        return{
            "criterion":['gini','entropy'],
            "splitter" : ['best', 'random'],
            "max_depth":[None,2,5,10],
            "ccp_alpha":[0.0, 0.1,0.4, 0.5]
        }
    
    
    def bernoulliParamaters(self):
        return{
            "alpha":[0.1, 0.5, 1.0, 1.3, 1.7, 2.0],
            "fit_prior":[True,False]
        }