import numpy as np
from funcoes import *

# Instalar a biblioteca cv2 pode ser um pouco demorado. Não deixe para ultima hora!
import cv2 as cv

def run():
    # Essa função abre a câmera. Depois desta linha, a luz de câmera (se seu computador tiver) deve ligar.
    cap = cv.VideoCapture(0)

    # Aqui, defino a largura e a altura da imagem com a qual quero trabalhar.
    # Dica: imagens menores precisam de menos processamento!!!
    width = 320
    height = 240

    # Talvez o programa não consiga abrir a câmera. Verifique se há outros dispositivos acessando sua câmera!
    if not cap.isOpened():
        print("Não consegui abrir a câmera!")
        exit()

    matriz_rotacao = np.array([[0.7, -0.7, 0], [0.7, 0.7, 0], [0, 0,1]])
    # Esse loop é igual a um loop de jogo: ele encerra quando apertamos 'q' no teclado.
    while True:
        # Captura um frame da câmera
        ret, frame = cap.read()

        # A variável `ret` indica se conseguimos capturar um frame
        if not ret:
            print("Não consegui capturar frame!")
            break

        # Mudo o tamanho do meu frame para reduzir o processamento necessário
        # nas próximas etapas
        frame = cv.resize(frame, (width,height), interpolation =cv.INTER_AREA)

        # A variável image é um np.array com shape=(width, height, colors)
        image = np.array(frame).astype(float)/255

        # Agora, mostrar a imagem na tela!
        cv.imshow('Minha Imagem!', image)

        # rotacionar a imagem
        image_ = np.zeros_like(image)

        Xd = criar_indices(0, 300, 0, 300)
        Xd = np.vstack ( (Xd, np.ones( Xd.shape[1]) ) )

        T = np.array([[1, 0, -150], [0, 1, -150], [0, 0,1]])
        T2 = np.array([[1, 0, 150], [0, 1, 150], [0, 0,1]])

        R = np.array([[0.7, -0.7, 0], [0.7, 0.7, 0], [0, 0,1]])

        A  = T2 @ R @ T
        X = np.linalg.inv(A)  @  Xd

        Xd = Xd.astype(int)
        X = X.astype(int)

        # Troque este código pelo seu código de filtragem de pixels
        Xd[0,:] = np.clip(Xd[0,:], 0, image.shape[0])
        Xd[1,:] = np.clip(Xd[1,:], 0, image.shape[1])

        image_[Xd[0,:], Xd[1,:], :] = image[X[0,:], X[1,:], :]

        # Se aperto 'q', encerro o loop
        if cv.waitKey(1) == ord('q'):
            break

        if cv.waitKey(1) == ord('m'):
            R = matriz_rotacao @ R
    # Ao sair do loop, vamos devolver cuidadosamente os recursos ao sistema!
    cap.release()
    cv.destroyAllWindows()

run()
