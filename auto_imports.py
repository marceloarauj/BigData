import subprocess
import sys

class Modules:

    def __init__(self):
        self.modules = [
            'wheel',
            'flask-cors',
            'numpy',
            'pandas',
            'matplotlib',
            'scipy',
            'scikit-learn',
            'opencv-python',
            'flask'
        ]

    def install_modules(self):
        print('Passo 1 - Verificando módulos')

        for i in self.modules:
            subprocess.check_call([sys.executable, "-m","pip","install","--user",i])