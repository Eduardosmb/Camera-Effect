# Camera Effect

Este é um projeto da matéria, Algebra linear e Teoria da Informação, em que consiste em aplicar efeitos visuais de rotação a câmera de seu computador

## Como usar:

Para utilizar o programa, basta seguir os passos abaixo:

1. Instale o Python 3.8 ou superior;

2. Instale a biblioteca Numpy;

    ```pip install numpy```

3. Instale a biblioteca opencv-python;

    ```pip install opencv-python```

4. Para facilitar, basta instalar os requirements.txt, que contém todas as bibliotecas necessárias para o funcionamento do programa.

    ```pip install -r requirements.txt```

5. Por fim basta rodar o arquivo "demo.py". Após fazer isso, sua câmera irá aparecer em sua tela. Para iniciar o efeito basta apertar a tecla "M" de seu telcado, e para paralo basta apertala de novo. Para finalizar o programa aperte a tecla "Q".

## Efeito

### Como funciona:
    O processo para gerar o efeito de rotação da camera acontece em alguns passo.
    
    1. É realizado uma translação na matriz que representa os pontos da imagem. Essa matriz tem como objetivo mover a imagem para o ponto de origem (0,0).
    
    2. É realizado uma rotação através de matrizes com o objetivo de rotacionar a imagem no aângulo desejado.
    
    3. É realizado uma outro transalção através de matrizes, porém dessa vez de voltar a posicao de nossa imagem ao ponto inicial. Para isso é necessario mulitplicão pelo inverso da mateiz do passo 1.
    
    4. Por fim são aplicados filtros, para que assim não tenham falhas nas imagens devidos a pixeis perdidos.
   


