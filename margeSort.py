from random import randint
import time

def mergeSortValues():
    secondsInicial = time.time()
    lista = []
    for n in range (0,1000000):
      lista.append(randint(1, 15))
    mergeSort(lista,0,len(lista)-1)
    secondsFinal = time.time()
    print(secondsFinal - secondsInicial)

#Primeiro precisamos solicitar a lista com os numeros a ordenar, a posição inicial e final da lista
def mergeSort(lista, first, last):
  #Como o métoto é recursivo (chama ele mesmo varias vezes), teremos que definir um parametro para
  #finalizar o processo. Neste caso será que quando atingir apenas um elemento, ou seja, posição
  #inicial igual à final.
  if first < last:
    #Teremos que dividir a lista em sub listas, então pegaremos o valor médio da mesma usando o valor
    #inteiro da divisão da soma do inicial com o final por dois. Nesta função pegamos apenas as posições
    #das divisões de listas. 
    middle = (first + last) // 2
    mergeSort(lista, first, middle) #Fazemos a lista esquerda chamar o método novamente, dividindo em duas partes
    mergeSort(lista, middle+1, last) #O mesmo para a lista da direita
    #As linhas 22 e 23 irão chamar o método até que se obtenha conjuntos de 1 elemento na lista, então prosseguindo
    # para a chamada do metodo marge
    merge(lista,first,middle,last)

#Agora iremos realizar a divisão das listas usando os indices das posições obtidas na função anterior (mergeSort)
def merge(lista,first,middle,last):
    left = lista[first:middle+1] #Obtendo a sublista esquerda com seus valores 
    right = lista[middle+1:last+1] #Obtendo a sublista direita com seus valores 
    left.append(-999999999) #Estamos ordenando decrescente, então atribuimos no final da sublista um valor muito pequeno
                            #para poder comparar na linha 38 e 42.
    right.append(-999999999)
    l = r = 0
    for k in range (first,last+1):
        if left[l] > right[r]: #Comparamos os valores por indice entre a lista esquerda e direita
            lista[k] = left[l]  #Se o valor da esquerda for maior, atribuimos ela na lista
            l += 1 #Subimos o indice da lista da esquerda para comparar novamente
        else:
            lista[k] = right[r] #Caso contrario atribuimos o valor da lista da direita
            r += 1#Subimos o indice da lista da direita para comparar novamente

margeSortValues()