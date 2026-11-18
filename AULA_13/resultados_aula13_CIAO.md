# AULA 13 — SPRINT 2 (AC-4)
# Operadores Evolucionários

**Aluno:** Gustavo Maiorino Wacker

**Disciplina:** Inteligência Computacional e Otimização

**Tecnologia:** Python, NumPy, Matplotlib e Pymoo

---

# 1. Introdução

Esta atividade apresenta a implementação de seis experimentos
práticos envolvendo operadores evolucionários e otimização
multiobjetivo.

Foi utilizado o algoritmo NSGA-II para explorar soluções que
consideram simultaneamente diferentes objetivos, como custo,
desempenho, latência e tempo de espera.

Também foram utilizados operadores de amostragem, cruzamento,
mutação, reparação de variáveis inteiras e tomada de decisão
multicritério.

# 2. Objetivos da atividade

- Aplicar variáveis inteiras em problemas de otimização.
- Configurar operadores genéticos SBX e PM.
- Comparar exploração e explotação.
- Avaliar a qualidade das soluções pelo Hipervolume.
- Utilizar PseudoWeights para selecionar soluções.
- Integrar otimização, restrições e MCDM em um problema hospitalar.

# 3. Fundamentação técnica

## 3.1 Algoritmo NSGA-II

O NSGA-II é um algoritmo evolucionário multiobjetivo que utiliza
classificação por dominância e diversidade das soluções para
construir uma fronteira de Pareto.

Uma solução é considerada não dominada quando não existe outra
solução que seja igual ou melhor em todos os objetivos e
estritamente melhor em pelo menos um deles.

## 3.2 Operadores evolucionários

**IntegerRandomSampling:** realiza a geração inicial de indivíduos
com valores inteiros.

**SBX (Simulated Binary Crossover):** operador de cruzamento que
combina características de duas soluções.

**PM (Polynomial Mutation):** operador de mutação que introduz
variações nas soluções.

**RoundingRepair:** corrige valores fracionários, arredondando-os
para valores inteiros.

## 3.3 Hipervolume

O Hipervolume (HV) mede a região do espaço de objetivos dominada
pelas soluções em relação a um ponto de referência.

Valores maiores indicam maior volume dominado, considerando
a mesma definição de objetivos e ponto de referência.

## 3.4 MCDM e PseudoWeights

O MCDM permite selecionar uma solução considerando pesos de
preferência para os objetivos.

O método PseudoWeights utiliza esses pesos para identificar
uma alternativa da fronteira de Pareto.

---

# 4. Desenvolvimento e resultados

## 4.1 Exercício 1 — Variáveis Inteiras na Prática (SOC Autônomo)

Foram utilizadas duas variáveis:

- Pods: de 1 a 30.
- Analistas de nível 2: de 1 a 15.

Objetivos:
- Minimizar a latência.
- Minimizar o custo.

Configuração:
- NSGA-II.
- População de 30 indivíduos.
- 40 gerações.
- Semente 42.
- IntegerRandomSampling.
- SBX com RoundingRepair.
- PM com RoundingRepair.

### Amostra dos resultados

| Pods | Analistas | Latência (ms) | Custo (R$/h) |
|---:|---:|---:|---:|
| 30 | 15 | 23.33 | 1215.00 |
| 1 | 1 | 550.00 | 63.00 |
| 2 | 1 | 350.00 | 81.00 |
| 3 | 1 | 283.33 | 99.00 |
| 4 | 1 | 250.00 | 117.00 |

### Gráfico da Fronteira de Pareto

![Exercicio 1](graficos/exercicio01_pareto.png)

**Análise:** o gráfico apresenta as soluções encontradas considerando
o compromisso entre latência e custo. A utilização de variáveis
inteiras permite representar quantidades reais de pods e analistas.

## 4.2 Exercício 2 — Dimensionamento Inteiro de Cluster Kubernetes

Variáveis:
- Réplicas da API: de 2 a 40.
- Worker Nodes: de 1 a 12.

Objetivos:
- Minimizar o tempo de resposta.
- Minimizar o custo mensal.

Configuração:
- População de 25 indivíduos.
- 35 gerações.
- Semente 10.
- IntegerRandomSampling.
- SBX e PM com RoundingRepair.

### Amostra dos resultados

| Réplicas | Worker Nodes | Tempo (ms) | Custo mensal (US$) |
|---:|---:|---:|---:|
| 2 | 1 | 500.00 | 109.00 |
| 40 | 12 | 31.67 | 1500.00 |
| 3 | 1 | 400.00 | 121.00 |
| 4 | 1 | 350.00 | 133.00 |
| 33 | 8 | 43.18 | 1076.00 |

**Análise:** o experimento demonstra o compromisso entre
dimensionamento da infraestrutura, tempo de resposta e custo
mensal. As quantidades de réplicas e nós são inteiras.

## 4.3 Exercício 3 — Operadores Genéticos: Exploração vs. Explotação

Foram comparadas duas configurações do NSGA-II.

**Configuração A — Exploração:**
- SBX com eta 5.
- PM com probabilidade 0,5 e eta 5.

**Configuração B — Explotação:**
- SBX com eta 30.
- PM com probabilidade 0,05 e eta 30.

Ambas utilizaram população de 30 indivíduos, 20 gerações
e semente 42.

### Resultados

| Configuração | Soluções encontradas |
|---|---:|
| Alta exploração | 30 |
| Alta explotação | 30 |

### Gráfico comparativo

![Exercicio 3](graficos/exercicio03_exploracao.png)

**Análise:** a configuração A favorece variações maiores e maior
exploração do espaço de busca. A configuração B favorece variações
menores e uma busca mais refinada ao redor das soluções existentes.
O gráfico permite comparar visualmente os resultados das duas
configurações.

## 4.4 Exercício 4 — Avaliação de Qualidade com Hipervolume

O problema utiliza duas variáveis:
- Potência de transmissão.
- Intervalo de envio.

Objetivos:
- Minimizar o consumo de bateria.
- Minimizar a perda de pacotes.

Foram realizadas duas execuções, com a mesma semente 42,
utilizando o NSGA-II e população padrão do algoritmo.

Ponto de referência: [400, 600].

### Resultados numéricos

| Execução | Gerações | Hipervolume |
|---|---:|---:|
| Curta | 10 | 227486.812874 |
| Longa | 80 | 227569.331921 |

### Comparação gráfica

![Exercicio 4](graficos/exercicio04_hipervolume.png)

**Análise:** A execucao com 80 geracoes apresentou maior hipervolume nesta experiencia.

O indicador permite avaliar quantitativamente a qualidade
das fronteiras de Pareto obtidas.

## 4.5 Exercício 5 — Tomada de Decisão Automática (MCDM)

O problema considera:
- RAM: de 4 GB a 128 GB.
- IOPS: de 100 a 5.000.

Objetivos:
- Minimizar o custo por hora.
- Minimizar o tempo de consulta.

Configuração:
- População de 40 indivíduos.
- 50 gerações.
- Semente 42.
- Pesos de 30% para custo e 70% para desempenho.

### Configuração recomendada

| Indicador | Resultado |
|---|---:|
| RAM | 76.62 GB |
| IOPS | 2754.54 |
| Custo por hora | US$ 56.52 |
| Tempo de consulta | 8.06 ms |

### Gráfico da seleção MCDM

![Exercicio 5](graficos/exercicio05_mcdm.png)

**Análise:** a solução selecionada pelo PseudoWeights considera
a preferência de negócio definida, atribuindo maior importância
ao desempenho do banco de dados.

## 4.6 Exercício 6 — Pipeline Completo: Otimização, Restrição e MCDM

O problema considera:
- Médicos plantonistas: de 2 a 20.
- Enfermeiros: de 4 a 40.

Objetivos:
- Minimizar o custo do plantão.
- Minimizar o tempo médio de espera na triagem.

Configuração:
- População de 40 indivíduos.
- 50 gerações.
- Semente 42.
- Pesos de 40% para custo e 60% para espera.

### Escala hospitalar recomendada

| Indicador | Resultado |
|---|---:|
| Médicos | 17 |
| Enfermeiros | 32 |
| Custo do plantão | R$ 34800.00 |
| Tempo de espera | 18.09 minutos |

### Verificação da restrição

A restrição de espera é definida por:

G(x) = f2_espera - 25 <= 0

Resultado:

18.09 - 25 = -6.91

**STATUS: APROVADO.**

A solução escolhida respeita a restrição de tempo de espera
menor ou igual a 25 minutos.

### Gráfico da escala hospitalar

![Exercicio 6](graficos/exercicio06_hospital.png)

**Análise:** o MCDM selecionou uma escala considerando os pesos
estabelecidos para custo e tempo de espera, respeitando a
restrição operacional do hospital.

---

# 5. Análise sobre variáveis contínuas e inteiras

Nos experimentos com variáveis inteiras, como os exercícios
1, 2 e 6, as soluções precisam representar quantidades completas
de recursos.

Nos exercícios com variáveis contínuas, como 3, 4 e 5,
o espaço de busca permite valores fracionários.

A diferença prática está na representação do problema:
recursos indivisíveis devem utilizar variáveis inteiras,
enquanto grandezas que admitem valores fracionários podem
ser modeladas como contínuas.

O uso de IntegerRandomSampling e RoundingRepair evita
quantidades fracionárias nos problemas inteiros.

# 6. Conclusão geral

A Aula 13 permitiu aplicar diferentes operadores evolucionários
em problemas de otimização multiobjetivo.

Os seis experimentos demonstraram como o NSGA-II pode ser
utilizado para resolver problemas de infraestrutura, sistemas
computacionais, redes de sensores, bancos de dados e
dimensionamento de equipes hospitalares.

A utilização de variáveis inteiras, operadores genéticos,
Hipervolume e PseudoWeights permitiu explorar diferentes
alternativas e selecionar soluções de acordo com os objetivos
e restrições de cada problema.

O exercício hospitalar integrou as técnicas estudadas em um
pipeline completo de otimização, com seleção automática e
verificação da restrição de espera máxima.

---

**Fim do relatório — Aula 13**
