import csv
import numpy as np
from scipy import stats

class StatisticalFunctions:

    def readCsv(self,file):
        data = {}

        with open('Metrics/'+file+'.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            keys = next(spamreader)
            for key in keys:
                data[key] = []
                
            for row in spamreader:
                data[keys[0]].append(row[0])
                data[keys[1]].append(row[1])
                data[keys[2]].append(row[2])
                data[keys[3]].append(row[3]) 

        return data            

    def mean(sef):
        print('')
    
    def desv(self):
        print('')

    def anova(self):
        print('')
    
    def checkNormalDistribution(self):
        values = self.readCsv('knn_metrics')
        accept_value = 0.05
        stats.normaltest(values['accuracy'])


teste = StatisticalFunctions()
#teste.readCsv('knn_metrics')
teste.checkNormalDistribution()