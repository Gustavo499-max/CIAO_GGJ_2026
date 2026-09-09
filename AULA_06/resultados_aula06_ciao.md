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

Resposta: 
1- O ACO utiliza várias formigas porque cada uma pode explorar caminhos diferentes, dessa forma, o algoritmo consegue analisar várias possibilidades ao mesmo tempo e aumenta a chance de encontrar uma rota melhor, se apenas uma formiga fosse utilizada, ela poderia escolher um caminho ruim logo no início e não explorar outras alternativas, com várias formigas, algumas podem encontrar rotas diferentes e comparar indiretamente suas soluções por meio do feromônio, portanto, a exploração de diferentes caminhos ajuda o algoritmo a evitar ficar preso em uma solução ruim e aumenta a possibilidade de encontrar uma rota de menor custo.

2- Uma rota de menor custo recebe mais feromônio porque ela representa uma solução melhor para o problema, portanto, quanto menor o custo, maior será a quantidade de feromônio depositada, esse aumento do feromônio faz com que as próximas formigas tenham uma probabilidade maior de escolher as mesmas conexões, assim, caminhos que apresentaram bons resultados são reforçados e passam a influenciar positivamente as próximas decisões da colônia.

3- Sem a evaporação, o feromônio acumulado nos primeiros caminhos encontrados permaneceria indefinidamente, isso poderia fazer com que as formigas começassem a seguir sempre os mesmos caminhos, mesmo que eles não fossem realmente os melhores, o algoritmo perderia capacidade de explorar novas alternativas e poderia ficar preso em uma solução de baixa qualidade, a evaporação diminui gradualmente a influência das informações antigas e permite que novos caminhos também sejam testados e reforçados. Dessa forma, existe um equilíbrio entre explorar novos caminhos e aproveitar os caminhos que já apresentaram bons resultados.


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


Os experimentos mostraram que os parâmetros do ACO influenciam diretamente o equilíbrio entre exploração e aproveitamento das soluções já encontradas, o parâmetro ALPHA controla a influência do feromônio, portanto valores maiores fazem com que as formigas sigam com maior intensidade os caminhos que foram bem avaliados anteriormente, o parâmetro BETA controla a influência do custo, fazendo com que valores altos aumentem a preferência por conexões de menor custo, a taxa de evaporação determina por quanto tempo as informações acumuladas permanecem no algoritmo. Uma evaporação baixa mantém o conhecimento das rotas anteriores por mais tempo, enquanto uma evaporação alta faz com que o algoritmo esqueça rapidamente essas informações. Por fim, aumentar o número de formigas permite explorar uma quantidade maior de caminhos em cada iteração, aumentando a possibilidade de encontrar boas soluções rapidamente, porém também aumentando o custo computacional, mesmo alterando os parâmetros, neste problema simples o algoritmo tende a encontrar a rota 0 → 1 → 2 → 3 → 4 → 5, com custo total 8, a principal diferença entre os experimentos aparece na velocidade de convergência e na distribuição final do feromônio.

Resposta da pergunta principal: Quando o algoritmo esquece rapidamente as experiências anteriores, o comportamento das formigas passa a depender muito mais das experiências recentes, isso pode aumentar a exploração, mas também pode dificultar a consolidação de uma boa rota, porque o feromônio das soluções anteriores desaparece rapidamente.


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

Assim, as conexões de menor custo possuem uma probabilidade maior de serem escolhidas pelas formigas, se o algoritmo utilizasse diretamente o custo, as rotas mais caras poderiam acabar se tornando mais atrativas, o que seria o contrário do objetivo da otimização.


2- Quando uma conexão recebe mais feromônio, sua atratividade aumenta, isso acontece porque o feromônio faz parte da fórmula:

fer ** ALPHA

Portanto, quanto maior a quantidade de feromônio, maior tende a ser o valor da atratividade, como consequência, as próximas formigas terão maior probabilidade de escolher aquela conexão, dessa forma, o ACO cria um processo de aprendizado coletivo: caminhos utilizados em boas soluções recebem mais feromônio e passam a ser escolhidos com maior frequência.


3- A função precisa impedir que a formiga retorne a um nó já visitado para evitar ciclos, por exemplo, sem essa restrição uma formiga poderia fazer:

0 → 1 → 2 → 1 → 2 → 1 → 2...

Ela poderia ficar repetindo os mesmos nós e nunca chegar ao destino, além disso, retornar para nós já visitados aumentaria desnecessariamente o custo da rota, por isso o código utiliza:

candidatos = [
    no for no in vizinhos
    if no not in rota
]

Assim, cada nó pode ser visitado apenas uma vez durante a construção daquela rota.



Lab04_aula06
Resultados:


# ============================================================
# LABORATÓRIO 04 — ACO DO ZERO
# ============================================================

import numpy as np
import random
import matplotlib.pyplot as plt


# ============================================================
# 1. MATRIZ DE CUSTOS
# ============================================================

CUSTOS = np.array([
    [0, 2, 4, np.inf, np.inf, np.inf],
    [2, 0, 1, 5, np.inf, np.inf],
    [4, 1, 0, 2, 3, np.inf],
    [np.inf, 5, 2, 0, 1, 4],
    [np.inf, np.inf, 3, 1, 0, 2],
    [np.inf, np.inf, np.inf, 4, 2, 0]
])

ORIGEM = 0
DESTINO = 5


# ============================================================
# 2. PARÂMETROS DO ACO
# ============================================================

NUM_FORMIGAS = 20
NUM_ITERACOES = 50

ALPHA = 1.0
BETA = 2.0

TAXA_EVAPORACAO = 0.5
Q = 100


# ============================================================
# 3. SEMENTE PARA REPETIR O RESULTADO
# ============================================================

random.seed(42)
np.random.seed(42)


# ============================================================
# 4. MATRIZ DE FEROMÔNIO
# ============================================================

feromonio = np.ones_like(
    CUSTOS,
    dtype=float
)

# Onde não existe conexão,
# o feromônio deve ser zero.
feromonio[CUSTOS == np.inf] = 0

# Também não precisamos de feromônio
# do nó para ele mesmo.
np.fill_diagonal(
    feromonio,
    0
)


# ============================================================
# 5. DESCOBRIR VIZINHOS
# ============================================================

def obter_vizinhos(no):

    vizinhos = []

    for proximo in range(
        len(CUSTOS)
    ):

        # Verifica se existe conexão
        if (
            proximo != no
            and
            CUSTOS[no][proximo] != np.inf
        ):

            vizinhos.append(
                proximo
            )

    return vizinhos


# ============================================================
# 6. CALCULAR ATRATIVIDADE
# ============================================================

def calcular_atratividade(
    atual,
    proximo
):

    fer = feromonio[
        atual
    ][
        proximo
    ]

    custo = CUSTOS[
        atual
    ][
        proximo
    ]

    # Fórmula do ACO:
    # feromônio^ALPHA × (1/custo)^BETA

    atratividade = (
        (fer ** ALPHA)
        *
        ((1 / custo) ** BETA)
    )

    return atratividade


# ============================================================
# 7. CONSTRUIR A ROTA DE UMA FORMIGA
# ============================================================

def construir_rota():

    # Toda formiga começa na origem.
    rota = [ORIGEM]

    atual = ORIGEM

    # Continua até chegar ao destino.
    while atual != DESTINO:

        vizinhos = obter_vizinhos(
            atual
        )

        # Impede a formiga de voltar
        # para um nó já visitado.
        candidatos = [
            no
            for no in vizinhos
            if no not in rota
        ]

        # Se não houver saída possível,
        # a rota é descartada.
        if not candidatos:
            return None


        # ----------------------------------------
        # Calculando atratividade
        # ----------------------------------------

        atratividades = []

        for candidato in candidatos:

            valor = calcular_atratividade(
                atual,
                candidato
            )

            atratividades.append(
                valor
            )


        # ----------------------------------------
        # Transformando em probabilidades
        # ----------------------------------------

        soma = sum(
            atratividades
        )

        # Proteção caso todas as
        # atratividades sejam zero.
        if soma == 0:

            proximo = random.choice(
                candidatos
            )

        else:

            probabilidades = [
                valor / soma
                for valor in atratividades
            ]


            # ------------------------------------
            # Escolha probabilística
            # ------------------------------------

            proximo = random.choices(
                candidatos,
                weights=probabilidades,
                k=1
            )[0]


        # Adiciona o nó escolhido à rota.
        rota.append(
            proximo
        )

        atual = proximo


    return rota


# ============================================================
# 8. CALCULAR O CUSTO DE UMA ROTA
# ============================================================

def calcular_custo(
    rota
):

    custo_total = 0

    for i in range(
        len(rota) - 1
    ):

        origem = rota[i]
        destino = rota[i + 1]

        custo_total += CUSTOS[
            origem
        ][
            destino
        ]

    return custo_total


# ============================================================
# 9. EVAPORAÇÃO DO FEROMÔNIO
# ============================================================

def evaporar_feromonio():

    global feromonio

    feromonio *= (
        1 - TAXA_EVAPORACAO
    )

    # Continua deixando zero
    # onde não existe ligação.
    feromonio[
        CUSTOS == np.inf
    ] = 0

    np.fill_diagonal(
        feromonio,
        0
    )


# ============================================================
# 10. DEPÓSITO DE FEROMÔNIO
# ============================================================

def depositar_feromonio(
    rota,
    custo
):

    # Quanto menor o custo,
    # maior o depósito.
    deposito = Q / custo

    for i in range(
        len(rota) - 1
    ):

        origem = rota[i]
        destino = rota[i + 1]

        feromonio[
            origem
        ][
            destino
        ] += deposito


# ============================================================
# 11. EXECUTANDO A COLÔNIA
# ============================================================

melhor_rota = None

melhor_custo = float(
    "inf"
)

historico = []


for iteracao in range(
    NUM_ITERACOES
):

    rotas_encontradas = []


    # Cada formiga procura uma rota.
    for formiga in range(
        NUM_FORMIGAS
    ):

        rota = construir_rota()


        if rota is not None:

            custo = calcular_custo(
                rota
            )

            rotas_encontradas.append(
                (rota, custo)
            )


            # Verifica se é a melhor
            # solução até o momento.
            if custo < melhor_custo:

                melhor_custo = custo

                melhor_rota = (
                    rota.copy()
                )


    # Primeiro ocorre a evaporação.
    evaporar_feromonio()


    # Depois ocorre o reforço
    # dos caminhos encontrados.
    for rota, custo in rotas_encontradas:

        depositar_feromonio(
            rota,
            custo
        )


    # Guarda o melhor custo de
    # cada iteração para o gráfico.
    historico.append(
        melhor_custo
    )


# ============================================================
# 12. RESULTADO FINAL
# ============================================================

print(
    "\n========== RESULTADO =========="
)

print(
    "\nMelhor rota encontrada:"
)

print(
    melhor_rota
)

print(
    "\nMelhor custo:"
)

print(
    melhor_custo
)


# ============================================================
# 13. MOSTRANDO O CÁLCULO DA MELHOR ROTA
# ============================================================

print(
    "\nCálculo da melhor rota:"
)

for i in range(
    len(melhor_rota) - 1
):

    origem = melhor_rota[i]
    destino = melhor_rota[i + 1]

    print(
        f"{origem} -> {destino}"
        f" = {CUSTOS[origem][destino]}"
    )


# ============================================================
# 14. GRÁFICO DA EVOLUÇÃO
# ============================================================

plt.figure(
    figsize=(10, 5)
)

plt.plot(
    historico
)

plt.xlabel(
    "Iteração"
)

plt.ylabel(
    "Melhor custo"
)

plt.title(
    "Evolução do melhor custo no ACO"
)

plt.grid()

plt.show()


# ============================================================
# 15. MATRIZ FINAL DE FEROMÔNIO
# ============================================================

print(
    "\nMatriz final de feromônio:"
)

print(
    np.round(
        feromonio,
        2
    )
)


plt.figure(
    figsize=(7, 6)
)

plt.imshow(
    feromonio,
    cmap="hot"
)

plt.colorbar(
    label="Quantidade de feromônio"
)

plt.xlabel(
    "Nó de destino"
)

plt.ylabel(
    "Nó de origem"
)

plt.title(
    "Matriz Final de Feromônio"
)

plt.xticks(
    range(len(CUSTOS))
)

plt.yticks(
    range(len(CUSTOS))
)

plt.show()

========== RESULTADO ==========

Melhor rota encontrada:
[0, 1, 2, 3, 4, 5]

Melhor custo:
8.0

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


 Resposta 

 1- O feromônio funciona como uma espécie de memória coletiva da colônia, quando uma formiga encontra uma rota, ela deposita feromônio nas conexões que utilizou, como o depósito é calculado por:

deposito = Q / custo

uma rota de menor custo recebe uma quantidade maior de feromônio.

Nas próximas iterações, as conexões que possuem mais feromônio tornam-se mais atrativas e têm uma chance maior de serem escolhidas pelas novas formigas, dessa maneira, as boas experiências das formigas anteriores influenciam as decisões das próximas formigas, com o passar das iterações, os melhores caminhos tendem a acumular mais feromônio.

2- Explorar significa testar caminhos diferentes, inclusive caminhos que ainda possuem pouco feromônio. Isso é importante porque permite descobrir novas rotas que podem ser melhores do que as encontradas anteriormente, aproveitar significa utilizar o conhecimento acumulado pela colônia, dando preferência aos caminhos que já possuem bastante feromônio e que anteriormente apresentaram bons resultados, o ACO precisa encontrar um equilíbrio entre os dois comportamentos, se o algoritmo explorar demais, pode demorar para aproveitar uma boa solução já encontrada, se aproveitar demais, pode ficar preso em uma rota encontrada no início e deixar de descobrir uma solução ainda melhor.

3- Eu investigaria primeiro o número de formigas e o número de iterações, porque eles influenciam diretamente a quantidade de caminhos analisados e o custo computacional do algoritmo, em uma rede pequena, utilizar 20 formigas por 50 iterações significa realizar uma quantidade relativamente pequena de buscas. Porém, em uma rede com centenas ou milhares de nós, aumentar demais esses valores pode deixar o processamento muito mais lento, também seria importante analisar a função que seleciona os próximos nós, tentando evitar cálculos desnecessários e restringir candidatos pouco interessantes, portanto, eu buscaria um equilíbrio entre quantidade de formigas, número de iterações e qualidade da exploração, para encontrar boas soluções sem tornar o algoritmo excessivamente lento.






