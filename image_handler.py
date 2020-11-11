import numpy as np
import base64
from matplotlib import pyplot as plt
from PIL import Image
import io
from cv2 import cv2

class ImageHandler:

    def npFromNpy(self,npy_path):
        return np.load(npy_path)

    #Passa imagem em vetor exemplo : porta_avioes[0]
    def drawImage(self,numpyImage):
        plt.figure()
        image = numpyImage.reshape(28,28)
        plt.imshow(image,cmap='gray')
        plt.show()

    def transformImageTo28x28(self,image):
        return (image.reshape(28,28)).tolist()

    def imageFormater(self,image):

        #Transforma de base 64 para numpy
        image_decoded = base64.b64decode(image)
        image = Image.open(io.BytesIO(image_decoded))
        cvImage = np.array(image)

        #transforma para grayscale
        gray_scale = cv2.cvtColor(cvImage,cv2.COLOR_BGR2GRAY)

        #redimensiona
        img28x28 = cv2.resize(gray_scale,(28,28))

        #redimensiona para uma array
        image_array = np.array(img28x28)
        image_array = image_array.reshape((1,28 * 28))
        
        #retorna o array da imagem
        return image_array[0]

    def loadDatabase(self,cutDatabase):
        print('Passo 2 - Carregando base de imagens')

        porta_avioes = self.npFromNpy('Database/full_numpy_bitmap_aircraft carrier.npy')
        alarme = self.npFromNpy('Database/full_numpy_bitmap_alarm clock.npy')
        ambulancia = self.npFromNpy('Database/full_numpy_bitmap_ambulance.npy')
        anjo = self.npFromNpy('Database/full_numpy_bitmap_angel.npy')
        formiga = self.npFromNpy('Database/full_numpy_bitmap_ant.npy')
        maca = self.npFromNpy('Database/full_numpy_bitmap_apple.npy')
        braco = self.npFromNpy('Database/full_numpy_bitmap_arm.npy')
        machado = self.npFromNpy('Database/full_numpy_bitmap_axe.npy')
        urso = self.npFromNpy('Database/full_numpy_bitmap_bear.npy')
        abelha = self.npFromNpy('Database/full_numpy_bitmap_bee.npy')
        
        porta_avioes = porta_avioes[:cutDatabase]
        alarme = alarme[:cutDatabase]
        ambulancia = ambulancia[:cutDatabase]
        anjo = anjo[:cutDatabase]
        formiga = formiga[:cutDatabase]
        maca = maca[:cutDatabase]
        braco = braco[:cutDatabase]
        machado = machado[:cutDatabase]
        urso = urso[:cutDatabase]
        abelha = abelha[:cutDatabase]

        print('Passo 3 - Convertendo para arrays 28x28')

        print("0%")
        porta_avioes = [ self.transformImageTo28x28(i) for i in porta_avioes]

        print('10%')
        alarme = [ self.transformImageTo28x28(i) for i in alarme]

        print('20%')
        ambulancia = [ self.transformImageTo28x28(i) for i in ambulancia]

        print('30%')
        anjo = [ self.transformImageTo28x28(i) for i in anjo]

        print('40%')
        formiga = [ self.transformImageTo28x28(i) for i in formiga]

        print('50%')
        maca = [ self.transformImageTo28x28(i) for i in maca]

        print('60%')
        braco = [ self.transformImageTo28x28(i) for i in braco]

        print('70%')
        machado = [ self.transformImageTo28x28(i) for i in machado]

        print('80%')
        urso = [ self.transformImageTo28x28(i) for i in urso]

        print('90%')
        abelha = [ self.transformImageTo28x28(i) for i in abelha]
        
        print('100%')

        return {
            'porta_avioes':porta_avioes,
            'alarme':alarme,
            'ambulancia':ambulancia,
            'anjo':anjo,
            'formiga':formiga,
            'maca':maca,
            'braco':braco,
            'machado':machado,
            'urso':urso,
            'abelha':abelha
        }