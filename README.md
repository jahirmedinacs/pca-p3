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

   - Foi calculado a matrix de covariância e
   
### PCA adaptativo
   
   - Foi feito uma rede não supervisionada 13x13   
## Resultados

### Responsabilidade na variância PCA clásica ###

| alcohol   | malic_acid |       ash | alcalinity_of_ash | magnesium | total_phenols | flavanoids | proanthocyanins | hue      | proline  | od280/od315_of_diluted_wines | color_intensity | nonflavanoid_phenols |
|-----------|:----------:|----------:|-------------------|-----------|---------------|------------|-----------------|----------|----------|------------------------------|-----------------|----------------------|
| 36.198848 |  19.20749  | 11.123631 | 7.06903           | 6.563294  | 4.935823      | 4.238679   | 2.680749        | 2.222153 | 1.930019 | 1.736836                     | 1.298233        | 0.795215             |


### Responsabilidade na variância PCA adaptativo ###


### Reducão de dimensionalidade ###

#### PCA clásico ####

#### PCA adaptativo ####


### Resultados do dataset wine ###

#### PCA clásico ####

#### PCA adaptativo ####

## Conclusões

  -
  
  -
