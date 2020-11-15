from machine_learning import MachineLearning

ml = MachineLearning({})

knn = {
    'accuracy':[6652.3,2553.0,44452.11,3331],
    'f1':[4444,3333,2222,111],
    'precision':[999000.2,00000,1.3323,4444],
    'recall':[22222,300.3,222.1,222.3]
}
ml.exportMetricsAsCSV('knn.csv',knn)