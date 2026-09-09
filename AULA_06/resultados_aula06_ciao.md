Resultado 
Lab01_aula06:

Matriz inicial de feromônio:
[[0. 1. 1. 0. 0. 0.]
 [1. 0. 1. 1. 0. 0.]
 [1. 1. 0. 1. 1. 0.]
 [0. 1. 1. 0. 1. 1.]
 [0. 0. 1. 1. 0. 1.]
 [0. 0. 0. 1. 1. 0.]]

Vizinhos do nó 0: [1, 2]
Vizinhos do nó 2: [0, 1, 3, 4]

Exemplo de rotas encontradas:
Formiga 1: [0, 1, 2, 3, 4, 5]
Formiga 2: [0, 1, 2, 3, 4, 5]
Formiga 3: [0, 1, 2, 3, 4, 5]
Formiga 4: [0, 1, 2, 3, 4, 5]
Formiga 5: [0, 2, 1, 3, 4, 5]

Melhor rota encontrada: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0

Cálculo da melhor rota:
0 -> 1 = 2.0
1 -> 2 = 1.0


1- O ACO utiliza várias formigas porque cada uma pode explorar caminhos diferentes. Dessa forma, o algoritmo consegue analisar várias possibilidades ao mesmo tempo e aumenta a chance de encontrar uma rota melhor.

Se apenas uma formiga fosse utilizada, ela poderia escolher um caminho ruim logo no início e não explorar outras alternativas. Com várias formigas, algumas podem encontrar rotas diferentes e comparar indiretamente suas soluções por meio do feromônio.

Portanto, a exploração de diferentes caminhos ajuda o algoritmo a evitar ficar preso em uma solução ruim e aumenta a possibilidade de encontrar uma rota de menor custo.

2- Uma rota de menor custo recebe mais feromônio porque ela representa uma solução melhor para o problema. 
Portanto, quanto menor o custo, maior será a quantidade de feromônio depositada.

Esse aumento do feromônio faz com que as próximas formigas tenham uma probabilidade maior de escolher as mesmas conexões. Assim, caminhos que apresentaram bons resultados são reforçados e passam a influenciar positivamente as próximas decisões da colônia.

3- Sem a evaporação, o feromônio acumulado nos primeiros caminhos encontrados permaneceria indefinidamente.

Isso poderia fazer com que as formigas começassem a seguir sempre os mesmos caminhos, mesmo que eles não fossem realmente os melhores. O algoritmo perderia capacidade de explorar novas alternativas e poderia ficar preso em uma solução de baixa qualidade.

A evaporação diminui gradualmente a influência das informações antigas e permite que novos caminhos também sejam testados e reforçados. Dessa forma, existe um equilíbrio entre explorar novos caminhos e aproveitar os caminhos que já apresentaram bons resultados.


Lab02_aula06
Resultados:

EXPERIMENTO PADRÃO

==============================================
========== RESULTADO DO EXPERIMENTO ==========
Número de formigas: 20
Número de iterações: 50
ALPHA: 1.0
BETA: 2.0
Taxa de evaporação: 0.5
Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0

EXPERIMENTO 1 — ALPHA = 0.1

==============================================
========== RESULTADO DO EXPERIMENTO ==========
Número de formigas: 20
Número de iterações: 50
ALPHA: 0.1
BETA: 2.0
Taxa de evaporação: 0.5
Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0

EXPERIMENTO 1 — ALPHA = 5.0

==============================================
========== RESULTADO DO EXPERIMENTO ==========
Número de formigas: 20
Número de iterações: 50
ALPHA: 5.0
BETA: 2.0
Taxa de evaporação: 0.5
Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0

EXPERIMENTO 2 — BETA = 0.5

==============================================
========== RESULTADO DO EXPERIMENTO ==========
Número de formigas: 20
Número de iterações: 50
ALPHA: 1.0
BETA: 0.5
Taxa de evaporação: 0.5
Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0

EXPERIMENTO 2 — BETA = 5.0

==============================================
========== RESULTADO DO EXPERIMENTO ==========
Número de formigas: 20
Número de iterações: 50
ALPHA: 1.0
BETA: 5.0
Taxa de evaporação: 0.5
Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0



EXPERIMENTO 3 — EVAPORAÇÃO = 0.1

==============================================
========== RESULTADO DO EXPERIMENTO ==========
Número de formigas: 20
Número de iterações: 50
ALPHA: 1.0
BETA: 2.0
Taxa de evaporação: 0.1
Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0

EXPERIMENTO 3 — EVAPORAÇÃO = 0.9

==============================================
========== RESULTADO DO EXPERIMENTO ==========
Número de formigas: 20
Número de iterações: 50
ALPHA: 1.0
BETA: 2.0
Taxa de evaporação: 0.9
Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0



EXPERIMENTO 4 — 5 FORMIGAS

==============================================
========== RESULTADO DO EXPERIMENTO ==========
Número de formigas: 5
Número de iterações: 50
ALPHA: 1.0
BETA: 2.0
Taxa de evaporação: 0.5
Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0

EXPERIMENTO 4 — 50 FORMIGAS

==============================================
========== RESULTADO DO EXPERIMENTO ==========
Número de formigas: 50
Número de iterações: 50
ALPHA: 1.0
BETA: 2.0
Taxa de evaporação: 0.5
Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0


Os experimentos mostraram que os parâmetros do ACO influenciam diretamente o equilíbrio entre exploração e aproveitamento das soluções já encontradas. O parâmetro ALPHA controla a influência do feromônio, portanto valores maiores fazem com que as formigas sigam com maior intensidade os caminhos que foram bem avaliados anteriormente. O parâmetro BETA controla a influência do custo, fazendo com que valores altos aumentem a preferência por conexões de menor custo.

A taxa de evaporação determina por quanto tempo as informações acumuladas permanecem no algoritmo. Uma evaporação baixa mantém o conhecimento das rotas anteriores por mais tempo, enquanto uma evaporação alta faz com que o algoritmo esqueça rapidamente essas informações. Por fim, aumentar o número de formigas permite explorar uma quantidade maior de caminhos em cada iteração, aumentando a possibilidade de encontrar boas soluções rapidamente, porém também aumentando o custo computacional.

Mesmo alterando os parâmetros, neste problema simples o algoritmo tende a encontrar a rota 0 → 1 → 2 → 3 → 4 → 5, com custo total 8. A principal diferença entre os experimentos aparece na velocidade de convergência e na distribuição final do feromônio.

Resposta da pergunta principal: quando o algoritmo esquece rapidamente as experiências anteriores, o comportamento das formigas passa a depender muito mais das experiências recentes. Isso pode aumentar a exploração, mas também pode dificultar a consolidação de uma boa rota, porque o feromônio das soluções anteriores desaparece rapidamente.


Lab03_aula06
Resultado:

Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0

Cálculo da melhor rota:
0 -> 1 = 2.0
1 -> 2 = 1.0
2 -> 3 = 2.0
3 -> 4 = 1.0
4 -> 5 = 2.0

Matriz final de feromônio:
[[  0. 500.   0.   0.   0.   0.]
 [  0.   0. 500.   0.   0.   0.]
 [  0.   0.   0. 500.   0.   0.]
 [  0.   0.   0.   0. 500.   0.]
 [  0.   0.   0.   0.   0. 500.]
 [  0.   0.   0.   0.   0.   0.]]


 Resposta: 

 1- A fórmula utiliza 1 / custo porque o objetivo do problema é encontrar caminhos de menor custo.

Ao utilizar:

1 / custo

um caminho barato produz um valor maior de atratividade, enquanto um caminho caro produz um valor menor.

Por exemplo:

Custo 1 → 1 / 1 = 1

Custo 2 → 1 / 2 = 0,5

Custo 5 → 1 / 5 = 0,2

Assim, as conexões de menor custo possuem uma probabilidade maior de serem escolhidas pelas formigas.

Se o algoritmo utilizasse diretamente o custo, as rotas mais caras poderiam acabar se tornando mais atrativas, o que seria o contrário do objetivo da otimização.


2- Quando uma conexão recebe mais feromônio, sua atratividade aumenta.

Isso acontece porque o feromônio faz parte da fórmula:

fer ** ALPHA

Portanto, quanto maior a quantidade de feromônio, maior tende a ser o valor da atratividade.

Como consequência, as próximas formigas terão maior probabilidade de escolher aquela conexão.

Dessa forma, o ACO cria um processo de aprendizado coletivo: caminhos utilizados em boas soluções recebem mais feromônio e passam a ser escolhidos com maior frequência.


3- A função precisa impedir que a formiga retorne a um nó já visitado para evitar ciclos.

Por exemplo, sem essa restrição uma formiga poderia fazer:

0 → 1 → 2 → 1 → 2 → 1 → 2...

Ela poderia ficar repetindo os mesmos nós e nunca chegar ao destino.

Além disso, retornar para nós já visitados aumentaria desnecessariamente o custo da rota.

Por isso o código utiliza:

candidatos = [
    no for no in vizinhos
    if no not in rota
]

Assim, cada nó pode ser visitado apenas uma vez durante a construção daquela rota.







