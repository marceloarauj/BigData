from auto_imports import Modules
from image_handler import ImageHandler
from machine_learning import MachineLearning

def main():
    install = Modules()
    install.install_modules()

    image_handler = ImageHandler()
    database = image_handler.loadDatabase(cutDatabase = 250)

    machine_learning = MachineLearning(database)
    machine_learning.executeTrain()
    
if __name__ == '__main__':
    main()