# AULA 13 — SPRINT 2 (AC-4)
## Operadores Evolucionários

**Aluno:** Gustavo Maiorino Wacker

**Disciplina:** Inteligência Computacional e Otimização

---

## 1. Variáveis contínuas e inteiras

Durante os experimentos, foi possível observar a diferença entre
variáveis contínuas e inteiras nos algoritmos evolucionários.

As variáveis contínuas permitem valores fracionários, como 3.5
servidores ou 7.8 analistas. Embora matematicamente possíveis,
esses valores não representam quantidades executáveis de recursos.

As variáveis inteiras representam quantidades completas, como
servidores, réplicas, médicos e enfermeiros.

No experimento foram utilizados:

- IntegerRandomSampling(): gera indivíduos com valores inteiros
  na população inicial.
- RoundingRepair(): arredonda os valores produzidos pelos
  operadores genéticos de cruzamento e mutação.

Dessa maneira, as soluções encontradas representam configurações
praticamente aplicáveis, evitando quantidades fracionárias de recursos.

## 2. Avaliação do Hipervolume — Exercício 4

Foi utilizado o indicador Hipervolume (HV) para comparar a
qualidade das soluções obtidas pelo NSGA-II em duas execuções.

Ponto de referência: [400.0, 600.0].

| Configuração | Hipervolume |
|---|---:|
| 10 gerações | 227486.812874 |
| 80 gerações | 227569.331921 |

### Análise dos resultados

A execução com 80 gerações apresentou maior hipervolume, indicando maior cobertura da região dominada em relação ao ponto de referência.

O Hipervolume considera a região dominada pelas soluções em relação
ao ponto de referência. Quanto maior seu valor, melhor a qualidade
da fronteira segundo esse indicador.

## 3. Tomada de decisão MCDM — Exercício 6

Foi desenvolvido um modelo de otimização para dimensionar uma
escala hospitalar, considerando médicos e enfermeiros como
variáveis inteiras.

Os objetivos foram minimizar o custo do plantão e o tempo médio
de espera na triagem.

Foram utilizados pesos de preferência de negócio:

- Custo: 40%.
- Tempo de espera: 60%.

### Escala hospitalar recomendada

| Indicador | Resultado |
|---|---:|
| Médicos plantonistas | 17 |
| Enfermeiros | 32 |
| Custo do plantão | R$ 34,800.00 |
| Tempo médio de espera | 18.09 minutos |

### Verificação da restrição hospitalar

A restrição estabelecida foi:

G(x) = Tempo de espera - 25 <= 0

Resultado: 18.09 - 25 = -6.91

**Status: APROVADO.** A escala recomendada respeita o limite
máximo de 25 minutos de espera.

## 4. Conclusão

A atividade permitiu aplicar operadores evolucionários,
otimização multiobjetivo e tomada de decisão multicritério.

Os experimentos demonstraram a importância da utilização de
variáveis inteiras para representar recursos reais, da avaliação
da qualidade das fronteiras por meio do Hipervolume e da utilização
de pesos de preferência para selecionar soluções de Pareto.

No estudo hospitalar, o modelo integrou otimização, restrições
operacionais e decisão automática, selecionando uma escala
que respeita o limite de espera estabelecido.

---

**Fim do relatório — Aula 13**
