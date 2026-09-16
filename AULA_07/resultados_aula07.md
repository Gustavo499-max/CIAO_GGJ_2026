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





