Lab-01:

O resultado obtido é que o algoritmo encontrou o ótimo global, o resultado mostra que se caso x for igual a 31, a função de x tem como resultado 961, que no caso é o ótimo global, olhando o gráfico se pode ver que o melhor fitness aumenta constantemente a cada geração, atingindo x = 28 (fitness 784) na geração 0, depois x = 29 (fitness 841) na geração 2, e x = 30 (fitness 900) na geração 3, o que no final encontra com o ótimo, o papel do elitismo desempenhou um papel significativo na garantia de que o melhor fitness não diminuísse, já que no caso o valor do melhor fitness não caiu nas gerações sequentes, a combinação de crossover e mutação permitiu que a população explorasse o espaço de busca, o crossover ajudou a combinar as melhores partes, enquanto a mutação introduz o novo material genético, evitando uma possível colisão, com essas variáveis  o algoritmo encontrou o ótimo rapidamente para problemas mais complexos ou espaços de busca maiores, esses parâmetros podem precisar ser aumentados para garantir a exploração e convergência adequadas


Lab-02:
ONEMAX - AG com 10 indivíduos, 100 gerações
==================================================
Geração   0: Melhor = 13/20, Média = 9.90
Geração  10: Melhor = 17/20, Média = 16.20
Geração  20: Melhor = 19/20, Média = 18.80
Geração  30: Melhor = 20/20, Média = 19.10
Geração  40: Melhor = 20/20, Média = 19.30
Geração  50: Melhor = 20/20, Média = 19.70
Geração  60: Melhor = 20/20, Média = 19.90
Geração  70: Melhor = 20/20, Média = 19.80
Geração  80: Melhor = 20/20, Média = 19.80
Geração  90: Melhor = 20/20, Média = 19.90

 MELHOR FITNESS: 20/20
   Ótimo = 20 (todos os bits são 1)

   1- A mutação alta insere ruído em excesso, com isso o algoritmo tem dificuldades para estabilizar a população próxima do topo pois o indivíduo perfeito constantemente terá mudanças e perderá bits 1, com isso o resultado será o seguinte A média da população cai e flutua bastante, impedindo a convergência completa da população

   2- as populações menores tem uma diversidade genética inicial menor, porém o algoritmo precisa de mais gerações para encontrar o ótimo de 20/20, com isso temos o seguinte resultado A convergência desacelera, aumentando a chance de estagnação em mínimos locais caso a taxa de mutação seja baixa

   3- Esse resultado permite que uma população menor encontre a solução perfeita ou dá tempo para a média da população inteira encostar no valor máximo, com isso o resultado é que no Teste 1, dar 100 gerações compensou o fato de a população ser pequena garantindo a média de 19.90 ao final

   4- O melhor indivíduo da geração deixa de ter garantia de sobrevivência para a próxima rodada, com isso a o encontrar o indivíduo 20/20, o algoritmo pode se destruir no crossover ou na mutação, com isso a linha do melhor fitness sofrerá oscilações e quedas ao longo do tempo em vez de permanecer travada no topo


Lab-03: 

   import numpy as np
import matplotlib.pyplot as plt
import random

# ==================== CONFIGURAÇÕES ====================
BITS = 8              # 8 bits → valores de 0 a 255
POP_SIZE = 20
GERACOES = 50
TAXA_CROSS = 0.8
TAXA_MUT = 0.05

# Intervalo de x
X_MIN = 0
X_MAX = 10

# ==================== FUNÇÃO OBJETIVO ====================
def funcao_objetivo(x):
    """f(x) = x * sin(3*x)"""
    return x * np.sin(3 * x)

# ==================== FUNÇÕES COMPLETADAS ====================

def bits_para_x(bits):
    """
    Converte lista de 8 bits para valor real no intervalo [X_MIN, X_MAX].
    """
    decimal = 0
    for i, bit in enumerate(reversed(bits)):
        decimal += bit * (2 ** i)
    
    max_decimal = (2 ** BITS) - 1
    x = X_MIN + (decimal / max_decimal) * (X_MAX - X_MIN)
    return x

def fitness(individuo):
    """
    Calcula o fitness de um indivíduo.
    Soma um offset (+10.0) para garantir valores positivos na roleta.
    """
    x = bits_para_x(individuo)
    val = funcao_objetivo(x)
    return val + 10.0

def mutacao(individuo):
    """
    Aplica mutação bit-flip em cada bit com probabilidade TAXA_MUT.
    """
    ind_mutado = individuo.copy()
    for i in range(len(ind_mutado)):
        if random.random() < TAXA_MUT:
            ind_mutado[i] = 1 - ind_mutado[i]
    return ind_mutado

# ==================== CÓDIGO PRONTO ====================

def criar_individuo():
    return [random.randint(0, 1) for _ in range(BITS)]

def criar_populacao():
    return [criar_individuo() for _ in range(POP_SIZE)]

def selecao_roleta(pop, fitnesses):
    total = sum(fitnesses)
    if total == 0:
        return random.choice(pop)
    pick = random.uniform(0, total)
    acumulado = 0
    for i, ind in enumerate(pop):
        acumulado += fitnesses[i]
        if acumulado > pick:
            return ind.copy()
    return pop[-1].copy()

def crossover(pai1, pai2):
    if random.random() > TAXA_CROSS:
        return pai1.copy(), pai2.copy()
    ponto = random.randint(1, BITS - 1)
    filho1 = pai1[:ponto] + pai2[ponto:]
    filho2 = pai2[:ponto] + pai1[ponto:]
    return filho1, filho2

def executar_ag():
    pop = criar_populacao()
    historico = []
    
    for gen in range(GERACOES):
        # Avaliar
        fitnesses = [fitness(ind) for ind in pop]
        
        melhor_fit = max(fitnesses)
        melhor_ind = pop[fitnesses.index(melhor_fit)]
        melhor_x = bits_para_x(melhor_ind)
        
        # Armazena o valor real da função f(x), descontando o offset do fitness
        f_x_real = funcao_objetivo(melhor_x)
        historico.append((melhor_x, f_x_real))
        
        if gen % 10 == 0:
            print(f"Geração {gen:3d}: Melhor f(x) = {f_x_real:.4f} (x = {melhor_x:.4f})")
        
        # Elitismo (preserva os 2 melhores)
        sorted_idx = np.argsort(fitnesses)[::-1]
        nova_pop = [pop[i].copy() for i in sorted_idx[:2]]
        
        # Criar filhos
        while len(nova_pop) < POP_SIZE:
            pai1 = selecao_roleta(pop, fitnesses)
            pai2 = selecao_roleta(pop, fitnesses)
            filho1, filho2 = crossover(pai1, pai2)
            nova_pop.append(mutacao(filho1))
            if len(nova_pop) < POP_SIZE:
                nova_pop.append(mutacao(filho2))
        
        pop = nova_pop
    
    return historico

# ==================== EXECUTAR ====================
print("=" * 50)
print("OTIMIZANDO f(x) = x * sin(3x)")
print("=" * 50)

historico = executar_ag()

# Visualizar
x_plot = np.linspace(X_MIN, X_MAX, 1000)
y_plot = funcao_objetivo(x_plot)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(x_plot, y_plot, 'b-', linewidth=2, label='f(x)')
melhor_x, melhor_fx = max(historico, key=lambda item: item[1])
plt.scatter(melhor_x, melhor_fx, color='red', s=100, zorder=5, label=f'Melhor: x={melhor_x:.3f}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Função e Melhor Solução')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
y_hist = [h[1] for h in historico]
plt.plot(range(GERACOES), y_hist, 'r-o', linewidth=2, markersize=4)
plt.xlabel('Geração')
plt.ylabel('Melhor f(x)')
plt.title('Convergência do AG')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print(f"\nMELHOR SOLUÇÃO ENCONTRADA: x = {melhor_x:.4f}, f(x) = {melhor_fx:.4f}")

OTIMIZANDO f(x) = x * sin(3x)
==================================================
Geração   0: Melhor f(x) = 8.5852 (x = 8.8235)
Geração  10: Melhor f(x) = 8.9019 (x = 8.9020)
Geração  20: Melhor f(x) = 8.9019 (x = 8.9020)
Geração  30: Melhor f(x) = 8.9019 (x = 8.9020)
Geração  40: Melhor f(x) = 8.9019 (x = 8.9020)


MELHOR SOLUÇÃO ENCONTRADA: x = 8.9020, f(x) = 8.9019




   

