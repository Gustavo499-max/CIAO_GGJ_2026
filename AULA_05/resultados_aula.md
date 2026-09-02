MISSÃO 1 — A PARTÍCULA SOLITÁRIA



Velocidade:

v_nova = w*v + c1*r1*(pBest - pos) + c2*r2*(gBest - pos)

Posição:

pos_nova = pos + v_nova

Resultado obtido

Melhor fitness encontrado: 0.00002413

Melhor posição encontrada: aproximadamente x = -0.004912

Primeira iteração em que o melhor fitness ficou abaixo de 0,001: 6

Ótimo teórico: x = 0, com f(x) = 0

Conclusão
A partícula conseguiu se aproximar bastante do mínimo da função x², mesmo com apenas uma partícula, a atualização da velocidade permitiu que ela explorasse o espaço de busca e melhorasse sua posição.

MISSÃO 2 — O ENXAME DE PARTÍCULAS


Resultado obtido

Melhor posição: (1.011065, 1.020752)

Melhor fitness: 0.00034763

Ótimo teórico: (1, 1) com fitness 0

Conclusão
O enxame chegou muito próximo do mínimo global, a cooperação entre as partículas melhora a busca porque cada partícula considera tanto sua própria melhor experiência (pBest) quanto a melhor experiência global (gBest).

MISSÃO 3 — OTIMIZAÇÃO LOGÍSTICA

Resultado obtido

Melhor custo inicial do enxame: 4645.88

Melhor custo final: 3515.82

Redução de custo: 1130.06

Percentual aproximado de melhoria: 24.32%

Centros alocados: 5

Coordenadas encontradas

Centro 1: (2.76, 5.36)

Centro 2: (7.74, 6.15)

Centro 3: (0.58, 8.65)

Centro 4: (5.44, 1.81)

Centro 5: (0.92, 1.90)

Conclusão
O PSO reduziu o custo em relação à melhor solução inicial, cada cliente foi associado implicitamente ao centro mais próximo, e o custo foi calculado como distância × demanda.


MISSÃO 4 — OTIMIZAÇÃO DOS PARÂMETROS

Resultados dos experimentos

Experimento

Custo Médio

Melhor Custo

Pior Custo

Padrão

3596.33

3543.98

3703.59

Inércia Alta

3998.92

3856.11

4163.21

Inércia Baixa

3678.37

3513.98

3930.22

Cognitivo Alto

3791.46

3598.17

4011.01

Social Alto

4012.52

3884.98

4179.25

Mais Partículas

3636.36

3537.39

3801.62

Respostas
1- Considerando o custo médio das 5 execuções, a melhor configuração foi padrão.

2- Considerando o custo médio, a pior configuração foi social alto.

3. Efeito dos parâmetros

Inércia (w): valores maiores mantêm mais movimento e exploração, mas podem atrasar a convergência, neste teste, a inércia alta teve desempenho pior que a configuração padrão.

Cognitivo (c1): aumenta a influência da melhor experiência individual da partícula, quando muito alto, pode fazer partículas insistirem demais em regiões próprias.

Social (c2): aumenta a influência do gBest, valor muito alto pode fazer o enxame convergir cedo demais para uma região e perder diversidade.

Número de partículas: mais partículas aumentam a exploração do espaço, porém também aumentam o custo computacional.

4-  Entre as configurações testadas, recomendo padrão, pois apresentou o menor custo médio nas cinco execuções, isso indica um bom equilíbrio entre exploração e convergência neste conjunto de dados.

RELATÓRIO FINAL PSO

1- PSO, é um algoritmo de otimização inspirado no comportamento coletivo de grupos, como bandos de pássaros, cada possível solução é representada por uma partícula, as partículas se movimentam pelo espaço de busca atualizando velocidade e posição, para decidir para onde ir, cada uma considera sua velocidade atual, sua melhor posição já encontrada (pBest) e a melhor posição encontrada por todo o grupo (gBest).

2- pBest é a melhor posição que uma partícula encontrou individualmente durante a busca e é importante porque mantém a memória individual de cada partícula, gBest é a melhor posição encontrada por qualquer partícula do enxame, permite que todas compartilhem a melhor descoberta coletiva, a combinação dos dois ajuda a equilibrar exploração e convergência.

Missão 1 — A Partícula Solitária

A partícula encontrou o mínimo? (X) Sim  ( ) Não

Quantas iterações foram necessárias? 6 iterações para atingir fitness menor que 0,001

Dificuldade: (X) Fácil  ( ) Médio  ( ) Difícil

Missão 2 — O Enxame

O enxame encontrou o mínimo global? (X) Sim, aproximadamente  ( ) Não

Compare com a Missão 1: O enxame foi mais eficiente para um problema mais complexo? (X) Sim  ( ) Não

Dificuldade: ( ) Fácil  (X) Médio  ( ) Difícil

Missão 3 — Problema Corporativo

Compare com o custo inicial: Melhorou? (X) Sim  ( ) Não

Custo inicial: 4645.88

Custo final: 3515.82

Quantos centros foram alocados? 5

Dificuldade: ( ) Fácil  (X) Médio  ( ) Difícil

Missão 4 — Otimização de Parâmetros

Melhor configuração encontrada:
w=0.7, c1=1.8, c2=1.8, partículas=30

Pior configuração encontrada:
w=0.7, c1=1.8, c2=2.5, partículas=30

Dificuldade: ( ) Fácil  (X) Médio  ( ) Difícil

CONCLUSÃO FINAL

As quatro missões mostraram a evolução do PSO desde o movimento de uma única partícula até a aplicação em um problema de logística com dez variáveis de decisão, o principal aprendizado foi entender como pBest, gBest, inércia e os coeficientes cognitivo e social influenciam a busca, no problema corporativo, o PSO conseguiu reduzir o custo total e encontrar cinco posições adequadas para os centros de distribuição, os testes de parâmetros também mostraram que aumentar um parâmetro isoladamente nem sempre melhora o resultado, sendo necessário equilibrar exploração e convergência.
