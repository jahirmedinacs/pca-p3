# Comparativa Principal Component Analysis Clasico e Principal Component Analysis rede adaptativa - Wine 

Autor:

- **Jeffri Erwin Murrugarra Llerena**
    * *USP #* **10655837** 
    

- **Jahir Gilbert Medina Llerena**
    * *USP #* **10659682**    
    
## Resumo
   
   Implementação da técnica PCA clasico e PCA con rede adaptativo no conjunto de dados Wine.

## Apresentação
   
   - **Wine** : Estes dados são os resultados de uma análise química de vinhos cultivados na mesma região na Itália, mas derivados de três diferentes cultivares. A análise determinou as quantidades de 13 constituintes encontrados em cada um dos três tipos de vinhos.
   
   - **PCA Clasico** : É um procedimento estatístico que usa uma transformação ortogonal para converter um conjunto de observações de variáveis possivelmente correlacionadas em um conjunto de valores de variáveis linearmente não correlacionadas, chamadas componentes principais.
   
   - **PCA con regra Hebbiana Generalizada** : É um modelo de rede neural feedforward linear para aprendizado não supervisionado com aplicações principalmente na análise de componentes principais é semelhante à regra de Oja em sua formulação e estabilidade, exceto que ele pode ser aplicado a redes com múltiplas saídas.

## Descrição de atividades

### Pre Procesamiento
   -  Padronize os dados X_i para estes tenham média igual a 0 e variância igual a 1

### PCA clasico

   - Foi calculado a matrix de covariância e calculo - se os autovetores e autovalores
   
### PCA adaptativo
   
   - Foi feito uma rede não supervisionada 13x13 con regra hebbiana generalizada para o aprendizado
   
### Test

   - Foi feito a reducão de dimensionalidade considerando 8 melhores variables 
   - Foi feito uma MLP 8x5x13, con funcão de ativação relu,hard_sigmoid,softmax e um dropout de 0.2,0.1
   - Foi particionada a data em 75% para treinamento e 25% para teste
   
## Resultados

### Responsabilidade na variância PCA clásica ###

| PCA                          | Responsabilidade |
|------------------------------|------------------|
| alcohol                      | 36.1988 %        |
| malic_acid                   | 19.2075 %        |
| ash                          | 11.1236 %        |
| alcalinity_of_ash            | 7.0690  %        |
| magnesium                    | 6.5633  %        |
| total_phenols                | 4.9358  %        |
| flavanoids                   | 4.2387  %        |
| proanthocyanins              | 2.6807  %        |
| hue                          | 2.2222  %        |
| proline                      | 1.9300  %        |
| od280/od315_of_diluted_wines | 1.7368  %        |
| color_intensity              | 1.2982  %        |
| nonflavanoid_phenols         | 0.7952  %        |

### Responsabilidade na variância PCA adaptativo ###

| PCA                               | Responsabilidade |
|-----------------------------------|------------------|
| alcohol                           | 19.32981         |
| malic_acid                        | 13.986309        |
| ash                               | 10.735028        |
| alcalinity_of_ash                 | 8.558073         |
| magnesium                         | 8.251536         |
| total_phenols                     | 7.156269         |
| flavanoids                        | 6.636788         |
| nonflavanoid_phenols              | 5.276198         |
| proanthocyanins                   | 4.801283         |
| color_intensity                   | 4.474312         |
| hue                               | 4.247415         |
| od280/od315_of_diluted_wines      | 3.672289         |
| proline                           | 2.874692         |

### Reducão de dimensionalidade ###

#### PCA clásico ####

#### PCA adaptativo ####


### Resultados do dataset wine ###

#### PCA clásico ####

#### PCA adaptativo ####

## Conclusões

  -
  
  -
