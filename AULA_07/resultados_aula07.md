resultados:

LAB 01:

1 - Como o uso da busca local 2-opt afeta o equilíbrio entre Exploration e Exploitation na busca de caminhos?
A busca local 2-opt aumenta a Exploitation do ACO, pois melhora localmente as rotas construídas pelas formigas através da inversão de trechos. Dessa forma, o ACO realiza a busca global e probabilística, enquanto o 2-opt refina as soluções encontradas. Isso pode acelerar a convergência, mas o uso excessivo da busca local pode diminuir a diversidade das soluções.

2 - O que aconteceria com a convergência do algoritmo se a taxa de evaporação (rho) fosse definida em 0.0 (sem evaporação)?
Com rho = 0.0, não ocorre evaporação dos feromônios. Assim, os feromônios acumulados permanecem durante todas as iterações, fazendo com que caminhos inicialmente favorecidos tenham influência cada vez maior. Isso reduz a exploração de novas rotas e pode causar convergência prematura ou estagnação em uma solução subótima.

LAB02:

Geração 1: Melhor Fitness = 13
Geração 2: Melhor Fitness = 15
Geração 3: Melhor Fitness = 15
Geração 4: Melhor Fitness = 15
Geração 5: Melhor Fitness = 15
Geração 6: Melhor Fitness = 15
Geração 7: Melhor Fitness = 15
Geração 8: Melhor Fitness = 15
Geração 9: Melhor Fitness = 15
Geração 10: Melhor Fitness = 15

==============================
        RESULTADO FINAL
==============================
Melhor indivíduo: [0 1 1 1 1]
Peso total: 8
Valor total: 15
Fitness: 15

[LAB 02 - SUCESSO] Algoritmo Genético executado!

Questões Técnicas — LAB 02
1 - Explique qual é o papel do operador de Mutação em um Algoritmo Genético e o que ocorre se a taxa de mutação for configurada em 100%.

A mutação tem o papel de introduzir diversidade genética na população. No código, ela pode inverter aleatoriamente os genes de um indivíduo de 0 → 1 ou de 1 → 0. Isso ajuda o Algoritmo Genético a explorar novas soluções e reduz a chance de ficar preso prematuramente em uma solução local.

Com a taxa de mutação configurada em 100%, todos os genes seriam invertidos durante a mutação. Por exemplo:

[1, 0, 1, 0, 1] → [0, 1, 0, 1, 0]

Nesse caso, a mutação deixa de ser uma pequena alteração aleatória e passa a modificar completamente cada indivíduo. Isso pode prejudicar o processo evolutivo, pois boas características obtidas pela seleção e pelo crossover são constantemente alteradas. Como consequência, a convergência pode ficar instável ou dificultada.

2 - Por que a penalização do fitness (atribuir 0 para indivíduos que estouram a capacidade) é fundamental para a convergência das restrições?

A penalização garante que soluções que violam a capacidade máxima da mochila não sejam consideradas boas soluções pelo Algoritmo Genético.

No código:

if total_weight > max_weight:
    return 0

Quando um indivíduo ultrapassa o limite de peso de 15, seu fitness é definido como 0. Isso reduz drasticamente sua chance de ser escolhido na seleção por torneio.

Sem essa penalização, uma solução poderia possuir um valor muito alto e ser considerada excelente mesmo ultrapassando a capacidade da mochila. O algoritmo poderia, então, favorecer e reproduzir soluções inválidas.

Portanto, a penalização direciona a evolução para regiões do espaço de busca que respeitam as restrições do problema, permitindo que o algoritmo procure soluções que sejam ao mesmo tempo válidas e de alto valor.


LAB 03:

Iteração 1: Melhor Fitness = 0.233705
Iteração 2: Melhor Fitness = 0.230322
Iteração 3: Melhor Fitness = 0.017423
Iteração 4: Melhor Fitness = 0.017423
Iteração 5: Melhor Fitness = 0.005174
Iteração 6: Melhor Fitness = 0.005174
Iteração 7: Melhor Fitness = 0.000399
Iteração 8: Melhor Fitness = 0.000399
Iteração 9: Melhor Fitness = 0.000399
Iteração 10: Melhor Fitness = 0.000399
Iteração 11: Melhor Fitness = 0.000399
Iteração 12: Melhor Fitness = 0.000399
Iteração 13: Melhor Fitness = 0.000399
Iteração 14: Melhor Fitness = 0.000280
Iteração 15: Melhor Fitness = 0.000226

========================================
          RESULTADO FINAL - PSO
========================================
[LAB 03] Melhor posição encontrada pelo Enxame (gbest): [ 0.00742668 -0.0130891 ]
Melhor Fitness: 0.000226
Coordenada X: 0.007427
Coordenada Y: -0.013089

Questões Técnicas — LAB 03
1 - O que acontece com o comportamento das partículas se zerarmos a componente cognitiva (c_1 = 0)?

A componente cognitiva representa a memória individual da partícula, fazendo com que ela seja atraída para a melhor posição que ela própria já encontrou (pbest).

Se c1 = 0, essa influência desaparece da equação:

V[i] = (w * V[i]) + (c2 * r2 * (gbest_X - X[i]))

Assim, as partículas deixam de considerar suas próprias melhores experiências e passam a se movimentar principalmente com base na inércia e na melhor posição encontrada pelo enxame (gbest).

Isso pode fazer com que as partículas se concentrem mais rapidamente em torno do gbest, reduzindo a diversidade do enxame. Como consequência, pode ocorrer convergência prematura caso o gbest esteja próximo de um mínimo local em problemas mais complexos.

2 - Qual a função do parâmetro de Inércia (w) na busca por mínimos globais?

O parâmetro de inércia w controla quanto da velocidade anterior da partícula será mantida na próxima iteração.

Na equação:

V[i] = (
    (w * V[i])
    + (c1 * r1 * (pbest_X[i] - X[i]))
    + (c2 * r2 * (gbest_X - X[i]))
)

O termo:

w * V[i]

determina a influência do movimento anterior.

Um valor maior de w faz as partículas manterem mais velocidade e explorarem regiões mais distantes do espaço de busca, aumentando a Exploration.

Um valor menor de w reduz o movimento das partículas, favorecendo uma busca mais detalhada próxima das melhores soluções já encontradas, aumentando a Exploitation.

Portanto, a inércia é importante para equilibrar exploração e refinamento. Um bom equilíbrio ajuda o PSO a explorar o espaço de busca sem abandonar rapidamente regiões promissoras.


LAB 04: 

[LAB 04] Matriz de Feromônio Atualizada:
 [[0.75       0.91666667 0.91666667 0.75      ]
 [0.75       0.75       0.75       1.08333333]
 [0.75       0.91666667 0.75       0.75      ]
 [0.75       0.75       0.75       0.75      ]]

Questões Técnicas — LAB 04
1 - Por que a evaporação do feromônio é necessária no algoritmo ACO?

A evaporação é necessária para evitar que os caminhos utilizados anteriormente mantenham uma influência muito grande durante toda a execução.

Ela ocorre pela fórmula:

feromônio = (1 - rho) × feromônio

No LAB, como rho = 0.25, a cada atualização permanece 75% do feromônio anterior.

Isso permite que o algoritmo gradualmente reduza a importância de caminhos antigos e continue explorando outras alternativas. Portanto, a evaporação ajuda a manter o equilíbrio entre Exploration, procurando novas rotas, e Exploitation, utilizando as melhores rotas já encontradas.

2 - O que ocorreria em grafos complexos sem ela?Qual a relação matemática entre a latência de um enlace e sua atratividade inicial (eta) para as formigas?

Sem evaporação (rho = 0), o feromônio depositado nunca seria reduzido e continuaria se acumulando.

Em grafos complexos, alguns caminhos poderiam receber muito feromônio nas primeiras iterações simplesmente por terem sido escolhidos inicialmente. As formigas passariam a escolher esses caminhos com frequência cada vez maior, reduzindo a exploração de outras rotas.

Isso pode provocar convergência prematura ou estagnação, fazendo com que o algoritmo permaneça em uma solução subótima e tenha dificuldade para descobrir caminhos melhores.


LAB 05:






