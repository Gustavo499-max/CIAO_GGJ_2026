
Lab01:

Total de solucoes avaliadas: 64
Tempo de execucao: 0.000365 segundos
Melhor valor encontrado: 8
Combinacao otima (0=nao leva, 1=leva): (1, 0, 1, 1, 0, 0)

Itens escolhidos:
 - Livro (peso: 2 , valor: 3 )
 - Camiseta (peso: 1 , valor: 2 )
 - Carregador (peso: 2 , valor: 3 )

 Relatorio:
1 - O resultado é 32 pois pois tem 5 itens e cada item tem 2 possibilidades então é feita a seguinte conta, 2x2x2x2x2= 32, agora caso a gente adicione mais um item com as mesmas 2 possibilidades a conta fica 2x2x2x2x2x2= 64 possiveis resultados
2 - O numero de resultados aumentaria para 32.768$ combinações, computador ainda resolveria isso em milissegundos, mas a complexidade aumentaria muito
3 - Investimentos: Um investimento com limite financeiro (capacidade) onde você escolhe em quais projetos aplicar dinheiro para obter o maior retorno possível, ou tambem em mapeamento de uma frota de caminhoes em uma operaçao logistica


Lab02: 

=================================================================
RESULTADOS DA FORCA-BRUTA NO TSP
=================================================================

>>> 4 cidades
    Rotas avaliadas : 6
    Melhor custo    : 80
    Melhor rota     : (0, 1, 3, 2, 0)
    Tempo (segundos): 0.000108

>>> 5 cidades
    Rotas avaliadas : 24
    Melhor custo    : 41
    Melhor rota     : (0, 1, 2, 3, 4, 0)
    Tempo (segundos): 0.000148

>>> 6 cidades
    Rotas avaliadas : 120
    Melhor custo    : 91
    Melhor rota     : (0, 1, 3, 4, 5, 2, 0)
    Tempo (segundos): 0.000415

=================================================================
OBSERVE: o numero de rotas cresce como (n-1)!  (fatorial)
4 cidades -> 6 rotas | 5 -> 24 | 6 -> 120 | 10 -> 362880 | 15 -> 87 bilhoes
=================================================================


 Relatorio:
 1 - podemos ver que o numero de rotas cresce bem mais rapido do que de forma linear ou quadratica, ele cresce de forma fatorial, de 4 pra 5 cidades ele cresceu 4x mais e de 5 pra 6 cidades ele cresceu 5x mais
 2 - levando em consideração que o numero de rotas esta crescendo de forma fatorial, caso fosse 10 cidades o numero de rotas seria de 362.880 rotas, com isso usando como base o tempo de 6 cidades o tempo estimado de 10 ciaddes seria de aproximadamente de 1.25 segundos
 3 - Por conta do crescimento do tempo


 Lab03: 


 import numpy as np
import itertools
import time

# ----------------------------------------------------------
# 1. Funcao que resolve a mochila por forca-bruta (otima)
# ----------------------------------------------------------
def mochila_otima(pesos, valores, capacidade):
    n = len(pesos)
    melhor = 0
    for comb in itertools.product([0, 1], repeat=n):
        peso = sum(pesos[i] for i in range(n) if comb[i] == 1)
        if peso <= capacidade:
            valor = sum(valores[i] for i in range(n) if comb[i] == 1)
            if valor > melhor:
                melhor = valor
    return melhor

# ----------------------------------------------------------
# 2. Heuristica Gulosa (ja pronta)
# ----------------------------------------------------------
def mochila_gulosa(pesos, valores, capacidade):
    n = len(pesos)
    densidade = [(valores[i] / pesos[i], i) for i in range(n)]
    densidade.sort(reverse=True)

    valor_total = 0
    peso_atual = 0
    for dens, i in densidade:
        if peso_atual + pesos[i] <= capacidade:
            peso_atual += pesos[i]
            valor_total += valores[i]
    return valor_total

# ----------------------------------------------------------
# 3. Funcao de calculo do Gap (IMPLEMENTADA)
# ----------------------------------------------------------
def calcular_gap(valor_heuristica, valor_otimo):
    """
    Retorna o gap percentual:
    gap = ((valor_otimo - valor_heuristica) / valor_otimo) * 100
    """
    if valor_otimo == 0:
        return 0.0
    return ((valor_otimo - valor_heuristica) / valor_otimo) * 100.0

# ----------------------------------------------------------
# 4. Experimento: varias instancias aleatorias
# ----------------------------------------------------------
np.random.seed(42)  # semente de aleatoriedade
n_itens = 12
capacidade = 30
n_instancias = 20

gaps = []

print('Rodando', n_instancias, 'instancias...')
for k in range(n_instancias):
    pesos = np.random.randint(1, 15, size=n_itens)
    valores = np.random.randint(10, 50, size=n_itens)

    otimo = mochila_otima(pesos, valores, capacidade)
    heur = mochila_gulosa(pesos, valores, capacidade)

    # Calculo e insercao do gap na lista
    gap = calcular_gap(heur, otimo)
    gaps.append(gap)

    print(f'Instancia {k+1:2d} | Otimo: {otimo:4d} | Gulosa: {heur:4d} | Gap: {gap:5.1f}%')

# ----------------------------------------------------------
# 5. Estatisticas finais
# ----------------------------------------------------------
print('\n===== RESUMO =====')
print(f'Gap medio     : {np.mean(gaps):.2f}%')
print(f'Gap minimo    : {np.min(gaps):.2f}%')
print(f'Gap maximo    : {np.max(gaps):.2f}%')
print(f'Desvio padrao : {np.std(gaps):.2f}%')


Resultado: 
Rodando 20 instancias...
Instancia  1 | Otimo:  199 | Gulosa:  199 | Gap:   0.0%
Instancia  2 | Otimo:  170 | Gulosa:  170 | Gap:   0.0%
Instancia  3 | Otimo:  155 | Gulosa:  155 | Gap:   0.0%
Instancia  4 | Otimo:  147 | Gulosa:  147 | Gap:   0.0%
Instancia  5 | Otimo:  261 | Gulosa:  261 | Gap:   0.0%
Instancia  6 | Otimo:  214 | Gulosa:  214 | Gap:   0.0%
Instancia  7 | Otimo:  191 | Gulosa:  187 | Gap:   2.1%
Instancia  8 | Otimo:  183 | Gulosa:  183 | Gap:   0.0%
Instancia  9 | Otimo:  215 | Gulosa:  206 | Gap:   4.2%
Instancia 10 | Otimo:  174 | Gulosa:  174 | Gap:   0.0%
Instancia 11 | Otimo:  262 | Gulosa:  262 | Gap:   0.0%
Instancia 12 | Otimo:  206 | Gulosa:  206 | Gap:   0.0%
Instancia 13 | Otimo:  231 | Gulosa:  231 | Gap:   0.0%
Instancia 14 | Otimo:  309 | Gulosa:  309 | Gap:   0.0%
Instancia 15 | Otimo:  294 | Gulosa:  294 | Gap:   0.0%
Instancia 16 | Otimo:  247 | Gulosa:  247 | Gap:   0.0%
Instancia 17 | Otimo:  136 | Gulosa:  134 | Gap:   1.5%
Instancia 18 | Otimo:  212 | Gulosa:  212 | Gap:   0.0%
Instancia 19 | Otimo:  243 | Gulosa:  243 | Gap:   0.0%
Instancia 20 | Otimo:  193 | Gulosa:  193 | Gap:   0.0%

===== RESUMO =====
Gap medio     : 0.39%
Gap minimo    : 0.00%
Gap maximo    : 4.19%
Desvio padrao : 1.03%


3- Sim, na prática ela se mostrou muito boa. Nos testes que rodamos, ela teve um gap médio de apenas 0,39%, acertando o valor ótimo exato em 17 das 20 instâncias (85% das vezes). Como o código é super simples e roda quase instantaneamente, compensa muito usar a gulosa na maioria dos casos.
Mas vale lembrar que ela não garante 100% de precisão sempre. Como não podemos "cortar" os itens ao meio na Mochila 0/1, pode acontecer de a gulosa colocar um item com densidade alta que ocupa muito espaço e acaba deixando um buraco na mochila que não dá para preencher com mais nada.



Lab04: 

import numpy as np

# ============================================================
# 1. Definição do Cenário do Problema Real
# ============================================================
np.random.seed(42)  # Para reproduzibilidade dos resultados

# Nomes fictícios de tarefas de freelancing
nomes_tarefas = [
    "Ajuste de CSS em site",
    "Criação de Logo",
    "Modelagem de Banco de Dados",
    "Automação em Python",
    "Correção de Bug em App",
    "Escrita de Artigo Técnico",
    "Design de Landing Page",
    "Integração de API de Pagamento",
    "Otimização de SEO",
    "Tradução de Documentação"
]

n_tarefas = len(nomes_tarefas)
tempo_maximo_disponivel = 16  # limite de 16 horas no fim de semana

# Gera tempo em horas (1 a 8 horas por tarefa)
horas_tarefas = np.random.randint(1, 9, size=n_tarefas)

# Gera valor pago em R$ (R$ 50 a R$ 400 por tarefa)
valores_tarefas = np.random.randint(50, 401, size=n_tarefas)


# ============================================================
# 2. Funções de Modelagem e Avaliação
# ============================================================
def gerar_solucao_aleatoria(n):
    """
    Gera um vetor binário aleatório representando a escolha de tarefas.
    Ex: [1, 0, 1, 1, ...]
    """
    return np.random.randint(0, 2, size=n)

def calcular_funcao_objetivo(solucao, valores):
    """
    Calcula a receita total obtida pelas tarefas selecionadas.
    """
    return int(np.sum(solucao * valores))

def verificar_restricoes(solucao, horas, limite_horas):
    """
    Verifica se a solução respeita a restrição de horas disponíveis.
    Retorna True se for factível e o total de horas gastas.
    """
    horas_totais = int(np.sum(solucao * horas))
    factivel = horas_totais <= limite_horas
    return factivel, horas_totais


# ============================================================
# 3. Execução do Teste
# ============================================================
# Gerando uma solução aleatória
solucao_testada = gerar_solucao_aleatoria(n_tarefas)
receita_total = calcular_funcao_objetivo(solucao_testada, valores_tarefas)
eh_factivel, horas_usadas = verificar_restricoes(solucao_testada, horas_tarefas, tempo_maximo_disponivel)

# Exibição detalhada dos resultados
print("=" * 60)
print(" RELATÓRIO DE AVALIAÇÃO DE SOLUÇÃO ALEATÓRIA")
print("=" * 60)
print(f"Capacidade Máxima do Fim de Semana : {tempo_maximo_disponivel} horas\n")

print("Tarefas Selecionadas na Solução:")
print("-" * 60)
for i in range(n_tarefas):
    status = "ACEITA" if solucao_testada[i] == 1 else "RECUSADA"
    print(f"[{status:8s}] {nomes_tarefas[i]:32s} | Tempo: {horas_tarefas[i]}h | Valor: R$ {valores_tarefas[i]}")

print("-" * 60)
print(f"Tempo Total Exigido : {horas_usadas}h / {tempo_maximo_disponivel}h")
print(f"Valor Total Obtido  : R$ {receita_total}")
print(f"A solução é Factual? : {'SIM (Respeita as restrições)' if eh_factivel else 'NÃO (Ultrapassa o tempo disponível)'}")
print("=" * 60)


Resultado: 
============================================================
 RELATÓRIO DE AVALIAÇÃO DE SOLUÇÃO ALEATÓRIA
============================================================
Capacidade Máxima do Fim de Semana : 16 horas

Tarefas Selecionadas na Solução:
------------------------------------------------------------
[ACEITA  ] Ajuste de CSS em site            | Tempo: 7h | Valor: R$ 264
[ACEITA  ] Criação de Logo                  | Tempo: 4h | Valor: R$ 380
[ACEITA  ] Modelagem de Banco de Dados      | Tempo: 5h | Valor: R$ 137
[ACEITA  ] Automação em Python              | Tempo: 7h | Valor: R$ 149
[ACEITA  ] Correção de Bug em App           | Tempo: 3h | Valor: R$ 201
[ACEITA  ] Escrita de Artigo Técnico        | Tempo: 8h | Valor: R$ 180
[RECUSADA] Design de Landing Page           | Tempo: 5h | Valor: R$ 199
[RECUSADA] Integração de API de Pagamento   | Tempo: 5h | Valor: R$ 358
[ACEITA  ] Otimização de SEO                | Tempo: 7h | Valor: R$ 307
[ACEITA  ] Tradução de Documentação         | Tempo: 2h | Valor: R$ 393
------------------------------------------------------------
Tempo Total Exigido : 43h / 16h
Valor Total Obtido  : R$ 2011
A solução é Factual? : NÃO (Ultrapassa o tempo disponível)
============================================================

Relatorio: 

o código que fiz, a função gerar_solucao_aleatoria só joga a moeda para cada tarefa (0 ou 1) de forma totalmente cega. Ela não olha se o tempo estourou e nem se o valor ganho é bom.
Na prática, ao rodar essa solução aleatória:
Risco de ser inválida (infactível): Na maioria das vezes, a soma das horas vai passar do limite de 16h do fim de semana.
Longe do ótimo: Mesmo quando ela não estoura o tempo, quase nunca pega a combinação que dá mais dinheiro.
É exatamente por isso que esse problema é difícil. Não basta sair escolhendo qualquer tarefa: o desafio real é achar um método (como uma heurística gulosa ou busca) que consiga equilibrar o tempo gasto com o valor ganho, respeitando a restrição de 16h e maximizando o lucro.






