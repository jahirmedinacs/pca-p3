import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

from copy import copy as copy

def wine(data):
    return data[:,1:]

def normalizacion(Data):
    
    for i in  np.arange(Data.shape[1]): 
        Data[:,i] = ( Data[:,i] - np.min(Data[:,i]) )/( np.max(Data[:,i]) - np.min(Data[:,i]) )
    return Data

def PCA_adaptative(X,C = 13,eta = 0.001,threshold = 1e-8 ,maxiter = 1000, verbose=False):
    comp = X.shape[1]
    W2 = np.random.random_sample((comp,X.shape[1]))# randomização dos pesos sinapticos
    c = 0
    
    #Treinamento da rede
    while c < maxiter: # criterio de parada
        tam = X.shape[0]
        for o in np.arange(tam):
            
            
            #regra Hebbiana Generalizada
            Xi = X[o,] 
            Yi = np.dot(W2,np.reshape(Xi,(13,1)))
            Z2 = np.dot(np.reshape(Yi,(comp,1)),np.reshape(Yi,(1,comp)))
            Z1 = np.dot(np.reshape(Yi,(comp,1)),np.reshape(Xi,(1,X.shape[1])))
            W2 = W2 + eta*( Z1 - np.dot(np.tril(Z2),W2))
        c = c + 1
      
    
    # Autovetores
    eig_vec_adap = np.transpose(W2)
    
    if verbose:
        print("Verificando Propiedad")
        for i in np.arange(comp):
           print(np.sum(np.power(eig_vec_adap[:,i],2)))
    else:
        pass
        
    M = np.dot(X,eig_vec_adap)
    eig_val_adap = np.zeros(comp)
    #Autovalores
    for i in np.arange(comp):
       eig_val_adap[i] = np.sqrt(np.sum(np.power(M[:,i],2)))
       
    
    eig_pairs = [(np.abs(eig_val_adap[i]), eig_vec_adap[:,i]) for i in range(len(eig_val_adap))]
    
    #output
    output_eig = [copy(eig_val_adap), copy(eig_vec_adap), copy(eig_pairs)]
    
    eig_pairs.sort(key=lambda x: x[0], reverse=True)
    ind = 1
    suma = 0 
    
    # print en pantalla
    if verbose:
        print("Autovalores em forma creciente")
        for i in eig_pairs:
            print('PCA'+ str(ind) + ': ' + str(i[0]))
            ind = ind+1
            suma = suma + i[0];
    else:
        pass

    ind = 1
    suma_porcentaje = 0
    if verbose:
        print("\nResponsabilidade na variância")
        for i in eig_pairs:
            print('PCA'+ str(ind) + ': ' + str((i[0]/suma) * 100) + '%')
            if ind - 1 < C :
                suma_porcentaje = suma_porcentaje + i[0]
            ind = ind+1
        print("\nRedução da dimensionalidade com "+ str(C) + 
            " componentes,é responsavel do " + str(suma_porcentaje/suma * 100) + "% da variância")
    else:
        pass
    

    matrix_w = np.hstack((eig_vec_adap[:,0].reshape(X.shape[1],1), eig_vec_adap[:,1].reshape(X.shape[1],1))) 
    transformed = matrix_w.T.dot(X.T) 
        
    
    return transformed, output_eig


def graficar(transformed):
    plt.plot(transformed[0,0:59], transformed[1,0:59], 'o', markersize=7, color='blue', alpha=0.5, label='Clase_1')
    plt.plot(transformed[0,60:130], transformed[1,60:130], '^', markersize=7, color='red', alpha=0.5, label='Clase_2')
    plt.plot(transformed[0,131:178], transformed[1,131:178], 'X', markersize=7, color='green', alpha=0.5, label='Clase_3')
    plt.xlim(np.min(transformed[0,] - 1),np.max(transformed[0,] + 1))
    plt.ylim(np.min(transformed[1,] - 1),np.max(transformed[1,] + 1))
    plt.xlabel('PCA1')
    plt.ylabel('PCA2')
    plt.legend()
    plt.title('grafico  da dimensionalidade com 2 componentes')

    plt.show()
    return 

def preprocessing(data):
    # media 0 e variância 1
    data = np.array(data,dtype = np.float32)
    scale = np.std(data, axis = 0)
    X = data - sp.mean(data,axis = 0)
    return X/scale

# def main():   
#    Comp = 2
#    datos = pd.read_csv("wine.data",sep = ",") # leitura dos dados
#    X = datos.values
#    X = wine(X)
#    X = preprocessing(X)
#    W = PCA_adaptative(X,C = Comp,eta = 0.001)
#    graficar(W[0])
   
# if __name__ == "__main__":
#    main()