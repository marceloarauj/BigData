# Python versão 3.8.6

# Execução

- Os módulos necessários são executados no inicio
- a variavel na linha 10 do arquivo main.py cutDatabase é equivalente à quantidade de dados de cada classe
- após a execução do main.py execute o controllers.py para disponibilizar a API

# ATENÇÃO 

- Crie um pasta Database com os arquivos de dados baixados do site:
    - full_numpy_bitmap_aircraft carrier.npy
    - full_numpy_bitmap_alarm clock.npy
    - full_numpy_bitmap_ambulance.npy
    - full_numpy_bitmap_angel.npy
    - full_numpy_bitmap_ant.npy
    - full_numpy_bitmap_apple.npy
    - full_numpy_bitmap_arm.npy
    - full_numpy_bitmap_axe.npy
    - full_numpy_bitmap_bear.npy
    - full_numpy_bitmap_bee.npy

# Arquivos
- Database: possui a base de dados com as 10 classes
- ExportedModels: após a execução do main , os melhores modelos de ML são exportados para essa pasta

- auto_imports.py : importa as bibliotecas necessárias para a aplicação funcionar
- controllers.py: possui os endpoints e disponibiliza a API, deve ser executado após o main.py
- services.py: possui os serviços que as apis utilizam
- functions_statistical.py: possui os métodos de análise estatistica
- grid_search_parameters.py: possui as variáveis utilizadas no grid search de cada modelo
- image_handler.py: possui funções relacionadas às imagens como transformação e plot
- machine_learning.py: possui os métodos de machine learning como treinamento, validação e uso do grid search
- main.py: arquivo que deve ser executado inicialmente