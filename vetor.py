import threading

def imprime(vetor,resto):
    #print(f"Thread {threading.current_thread().name}")
    for i in range(len(vetor)):
        if ((i % 2 == resto)):
            print(f'vetor[{i}]={vetor[i]}')


if __name__ == '__main__':
    
    vetor = [1,2,3,4,5,6,7,8,9,10]
    print('Posicoes Pares')
    thread1 = threading.Thread(target=imprime,args=(vetor,0))
    print('Posicoes Impares')
    thread2 = threading.Thread(target=imprime,args=(vetor,1))

    thread1.start()
    thread2.start()
    