import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

from copy import copy as copy

def iris(data):
    return data[:,:-1] #dados sem clase Y

def preprocessing(data):
    # media 0 e variância 1
    X = data - sp.mean(data,axis = 0)
    return X
    
def PCA(data, comp=2, verbose=False):
    n = data.shape[1]
    # matriz de covariância
    cov_matrix = np.cov(data.astype(float), rowvar=False)
   
    # autovetores e autovalores
    
    eig_val_cov, eig_vec_cov = np.linalg.eig(cov_matrix)
    
    eig_pairs = [(np.abs(eig_val_cov[i]), eig_vec_cov[:,i]) for i in range(len(eig_val_cov))]
    
    output_eig = [copy(eig_val_cov), copy(eig_vec_cov), copy(eig_pairs)]
    
    # ordenar autovetores e autovalores 
    eig_pairs.sort(key=lambda x: x[0], reverse=True)

    ind = 1
    suma = 0
    
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
            if ind - 1 < comp :
                suma_porcentaje = suma_porcentaje + i[0]
            ind = ind+1
        print("\nRedução da dimensionalidade com "+ str(comp) + " componentes,é responsavel do " + str(suma_porcentaje/suma * 100) + "% da variância")
    
    else:
        pass
    
    
    matrix_w = np.hstack((eig_pairs[0][1].reshape(n,1), eig_pairs[1][1].reshape(n,1)))
    
    if verbose:
        print(matrix_w)
    else:
        pass
    
    transformed = matrix_w.T.dot(data.T)
    return transformed, output_eig


def graficar(transformed):
    plt.plot(transformed[0,0:49], transformed[1,0:49], 'o', markersize=7, color='blue', alpha=0.5, label='Iris-setosa')
    plt.plot(transformed[0,50:99], transformed[1,50:99], '^', markersize=7, color='red', alpha=0.5, label='Iris-versicolor')
    plt.plot(transformed[0,100:149], transformed[1,100:149], 'X', markersize=7, color='green', alpha=0.5, label='Iris-virginica')
    plt.xlim([-4,4])
    plt.ylim([-4,4])
    plt.xlabel('PCA1')
    plt.ylabel('PCA2')
    plt.legend()
    plt.title('grafico  da dimensionalidade com 2 componentes')

    plt.show()
    return 

# def main():
#     datos = pd.read_csv("iris.data",sep = ",") 
#     X = datos.values
#     X = iris(X)
#     X = preprocessing(X)
#     T = PCA(X)
#     graficar(T)
# if __name__ == "__main__":
#     main()





