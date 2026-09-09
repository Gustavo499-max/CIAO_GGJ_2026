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

==============================
       RESULTADO FINAL
==============================
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


2 -> 3 = 2.0
3 -> 4 = 1.0
4 -> 5 = 2.0
