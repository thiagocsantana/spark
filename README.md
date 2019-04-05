# spark
spark


### Qual o objetivo do comando cache em Spark?

Toda vez que for necessário realizar mais do que uma ação em uma RDD, o ideal é adicionar essa RDD em cache, através do comando cache(), isso melhora a performance do retorno dos dados na ação sobre esses dados executada. Sabemos que uma ação efetiva as operações de transformações imediatamente anteriores a esta e, portanto, colocar os resultados intermediários na memória sabendo que outras ações serão executadas sobre esse resultado evita que novamente os dados sejam processados, gerando performance.

### O mesmo código implementado em Spark é normalmente mais rápido que a implementação equivalente em MapReduce Por quê?

Uma implementação em spark ou em map reduce são equivalentes apenas no conceito de mapeamento e redução. Entretanto, enquanto o hadoop map reduce armazena os dados intermediários, resultantes do processo de mapeamento e redução em disco, o spark beneficia-se por realizar o mesmo procedimento, porém armazenando os dados intermediários em memória, permitindo que a execução iterativa de algoritmos sobre esses dados, por exemplo, seja realizado de forma eficiente, até 100x mais rápido do que o hadoop realizaria a mesma operação, mas armazenando os dados em disco.

### Qual é a função do SparkContext?

O SparkContext é a camada cliente que estabelece conexão com o ambiente de processamento do Spark, permitindo que aplicações Spark conecte-se a este ambiente. Cada aplicação Spark inicia uma instância do Spark Context, e não há como uma aplicação Spark conectar ao ambiente de processamento do Spark sem uma instância do SparkContext.

### Explique com suas palavras o que é Resilient Distributed Datasets (RDD).

Um RDD é um conceito chave no framework Spark. Um RDD pode ser imaginado como um conjunto de dados, semelhante a uma tabela de banco de dados, podendo armazenar qualquer tipo de dado, inclusive objetos Java, Scala ou Python, até mesmo classes definidas pelo usuário. RDD é uma coleção de dados, onde cada conjunto de dados no RDD é dividido em partições lógicas, permitindo que esses dados possam ser processados de forma distribuída por todo o cluster. Os dados em um RDD são imutáveis, ou seja, uma vez criado um RDD não é possível alterar seus dados. As transformações que são feitas em um RDD na verdade criam um novo RDD com o resultado dessas transformações, permanecendo imutável o RDD original. RDDs podem ser criados sob duas origens, através de uma paralelização de uma coleção existente, por meio do comando sc.parallelize, ou referenciando um dataset externo, como arquivos locais, dados em HDFS, em banco de dados relacionais ou não-relacionais. Na essência, os RDD´s são a base fundamental para o uso do framework Spark.

### GroupByKey é menos eficiente que reduceByKey em grandes dataset. Por quê?

O reduceByKey realiza o agrupamento dos valores das chaves em cada nó do cluster, trafegando pela rede apenas o resultado, ou saída para cada chave na rede. O groupByKey não realiza essa agregação parcialmente em cada nó do cluster, trafegando um conjunto de dados muito maior para que os executores realizem o trabalho de agrupamento em sua totalidade. Em grandes datasets, esse grande volume de dados trafegando pela rede pode exigir que o Spark realize o processamento desses dados em disco, tornando o groupByKey menos eficiente do que o reduceByKey. Em outras palavras, o reduceByKey implementa o mapeamento e a redução de forma mais eficiente realizando essa operação dentro do próprio node do cluster responsável pela partição dos dados em um RDD.

