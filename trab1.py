import cv2
import numpy as np

'''
1. Alteração de brilho. Um valor deve ser lido e passado por parâmetro para o procedimento
de alteração de brilho da imagem.

2. Imagem negativa (inversão de cores).

3. Histograma global. Gerar um vetor para representar o histograma da imagem. Concatenar
o histograma de cada banda RGB em um único vetor. Armazenar o resultado em um arquivo
para facilitar a visualização do resultado.

4. Histograma local. Defina um particionamento da imagem com no mínimo 3 partições.
Concatenar os histogramas em um único vetor. Armazenar o resultado em um arquivo para
facilitar a visualização do resultado.

5. Três transformadas radiométricas: uma de Equalização de Histograma e as outra duas a
escolha da equipe.

6. Três filtros espaciais, podendo escolher entre o filtro dos k vizinhos mais próximos, filtro
da mediana, filtro da moda. Comparar os resultados com o filtro da média (este será um
dos filtros implementados). Deve-se gerar imagens com ruído (tipicamente 10%) do tipo sal
e pimenta para testes. Comparar os resultados.

7. Detecção de bordas, qualquer técnica. Pode ser necessário reduzir a quantidade de cores
(quantização). A quantização escolhida deve ficar entre 32 a 256 cores. A técnica de
redução da quantização fica a sua escolha, podendo nesse caso, utilizar operações
disponíveis na biblioteca OpenCV (ou a biblioteca da escolha da equipe).

8. Extração de propriedades de cor usando o descritor BIC. Aproveita a redução da
quantização da questão anterior. O resultado principal é um arquivo com os histogramas
de pixels de borda e interior. Deve-se também gerar duas imagens, uma somente com os
pixels de borda (com a cor original para os pixels de borda e os pixels de interior em branco)
e outra com os pixels de interior (com a cor original para os pixels de interior e pixels de
borda em branco).'''

MAX_VAL = 255

imOut = "output"

def createArray(lenght):
    vetor = []
    for i in range(lenght):
        vetor.append([0,0,0])
    return vetor

def writeArray(name, array):
    with open(name,'w') as file:
        file.write(','.join(map(str, array)))

def grayscale(mat,dim):
    for i in range(dim[0]):
        for j in range(dim[1]):
            temp=mat[i][j].sum()
            for k in range(dim[2]):
                mat[i][j][k] = temp/3
    return mat

    

def questao1(image,dim):

    if image is None:
        print("Imagem não encontrada!")
        return 0
    else:
        image_mat = np.array(image)
    numVal = 0
    while(numVal == 0):
        print('Entre com um valor maior que -256 e menor que 256: ')
        val = input()
        try:
            val = int(val)
        except Exception as e:
            print('Entrada invalida!')
        finally:
            if val >= MAX_VAL*(-1) and val <= MAX_VAL:
                numVal = 1
            else:
                print('Entrada invalida!')

    for i in range(dim[0]):
        for j in range(dim[1]):
            for k in range(dim[2]):
                temp =image_mat[i][j][k]+val
                if(temp > MAX_VAL):
                    image_mat[i][j][k] = MAX_VAL
                elif(temp < 0):
                    image_mat[i][j][k] = 0
                else:
                    image_mat[i][j][k] = temp
    cv2.imwrite(imOut+'1.jpg',image_mat)



def questao2(image,dim):
    if image is None:
        print("Imagem não encontrada!")
        return 0
    else:
        image_mat = np.array(image)

    for i in range(dim[0]):
        for j in range(dim[1]):
            for k in range(dim[2]):
                image_mat[i][j][k] = MAX_VAL - image_mat[i][j][k]
                
    cv2.imwrite(imOut+'2.jpg',image_mat)


def questao3(image,dim):
    vetor = createArray(MAX_VAL+1)
    if image is None:
        print("Imagem não encontrada!")
        return 0
    else:
        image_mat = np.array(image)

    for i in range(dim[0]):
        for j in range(dim[1]):
            for k in range(dim[2]):
                vetor[image_mat[i][j][k]][k]+=1       
    writeArray('output3.txt',vetor)

def questao4(image,dim):
    hei20 = int(dim[1]*0.2)
    wei20 = int(dim[0]*0.2)
    hei50 = int(dim[1]*0.5)
    wei50 = int(dim[0]*0.5)

    histograma =[]
    num_particoes = 5
    for i in range(num_particoes):
        histograma.append(createArray(MAX_VAL+1))

    if image is None:
        print("Imagem não encontrada!")
        return 0
    else:
        image_mat = np.array(image)
    for i in range(dim[0]):
        for j in range(dim[1]):
            for k in range(dim[2]):
                if (j < hei50 and i < wei20) or (j < hei20 and i < wei50):
                    histograma[0][image_mat[i][j][k]][k]+=1
                elif (j > hei50 and i < wei20) or (j > dim[1]-hei20 and i < wei50):
                    histograma[1][image_mat[i][j][k]][k]+=1
                elif (j > hei50 and i > dim[0]-wei20) or (j > dim[1]-hei20 and i > wei50):
                    histograma[2][image_mat[i][j][k]][k]+=1
                elif (j < hei50 and i > dim[0]-wei20) or (j < hei20 and i > wei50):
                    histograma[3][image_mat[i][j][k]][k]+=1               
                else:
                    histograma[4][image_mat[i][j][k]][k]+=1
    writeArray('output4.txt',histograma)

def questao5(image,dim):
    if image is None:
        print("Imagem não encontrada!")
        return 0
    else:
        image_mat = np.array(image)

    image_mat = grayscale(image_mat,dim)
    cv2.imwrite(imOut+'5.jpg',image_mat)

def questao6():
    return 0

def questao7():
    return 0

def questao8():
    return 0

def questao9():
    a = 11
    image = cv2.imread('img1.jpg')
    dim = image.shape
    while(a!='0'):
        print('Entre com o indice da questao:')
        print('\t1 - Questao 01')
        print('\t2 - Questao 02')
        print('\t3 - Questao 03')
        print('\t4 - Questao 04')
        print('\t5 - Questao 05')
        print('\t6 - Questao 06')
        print('\t7 - Questao 07')
        print('\t8 - Questao 08')
        print('\t0 - Finalizar o programa')
        a=input()
        if a == '0':
            print("Fim do Programa.")

        elif a == '1':
            questao1(image,dim)

        elif a == '2':
            questao2(image,dim)
            
        elif a == '3':
            questao3(image,dim)

        elif a == '4':
            questao4(image,dim)
        
        elif a == '5':
            questao5(image,dim)

        elif a == '6':
            questao6()
        
        elif a == '7':
            questao7()

        elif a == '8':
            questao8()

        else:
            print("Opção invalida!")


questao9()