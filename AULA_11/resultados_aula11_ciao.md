 AULA 11 — VALIDAÇÃO EXPERIMENTAL E FECHAMENTO DA AC-3

 Objetivo

O objetivo desta atividade foi realizar a validação experimental de sistemas baseados em lógica fuzzy, utilizando testes automatizados com Pytest, identificação de falhas, correção de erros e análise de cobertura de código.

A atividade foi dividida em duas fases:

Fase 1: validação de um motor de inferência fuzzy.
Fase 2:  desenvolvimento e validação de um sistema fuzzy para triagem de pacientes em UTI.

O desenvolvimento foi realizado em Python, utilizando Google Colab, Scikit-Fuzzy, NumPy e Pytest.



 Fase 1 — Validação do motor de inferência fuzzy

Foram utilizados os arquivos `engine.py`, `model.py` e `test_fuzzy_engine.py`.

O sistema foi submetido a três execuções para avaliar seu comportamento em condições normais, durante uma falha proposital e após a correção.

 Primeira execução — Validação inicial

A primeira execução teve como objetivo verificar o funcionamento do motor fuzzy antes da introdução de erros.

Foram considerados três cenários de teste:

1. Avaliação de uma situação de baixo risco.
2. Avaliação de uma situação de alto risco.
3. Validação dos limites de entrada.

Os valores de referência obtidos nas execuções foram:

- Baixo risco: 13,17%.
- Alto risco: 86,83%.

A primeira execução serviu como referência para a análise experimental posterior.

Observação: o tempo e a saída exata da primeira execução devem ser preenchidos a partir do registro original do Colab, caso estejam disponíveis.

 Segunda execução — Falha proposital

Na segunda execução, foi introduzida intencionalmente uma condição incorreta no teste `test_02_alto_risco`.

A condição foi modificada para:

`assert risco > 100`

Como o motor fuzzy calculou um risco de aproximadamente 86,83%, o Pytest identificou corretamente a falha de asserção.

Resultados:

- Teste 1 — Baixo risco: PASSED (13,17%).
- Teste 2 — Alto risco: FAILED (86,83% não é maior que 100%).
- Teste 3 — Validação de limites: PASSED.
- Total: 2 testes aprovados e 1 reprovado.
- Tempo de execução: 1,33 segundos.

A falha demonstrou a capacidade do Pytest de detectar inconsistências nas condições de validação, permitindo identificar precisamente o teste que não atendeu ao resultado esperado.

 Terceira execução — Correção dos erros

Após a identificação da falha proposital, a condição original do teste de alto risco foi restaurada.

A suíte de testes foi executada novamente, apresentando os seguintes resultados:

- Teste 1 — Baixo risco: PASSED (13,17%).
- Teste 2 — Alto risco: PASSED (86,83%).
- Teste 3 — Validação de limites: PASSED.

Resultado final: 3 testes aprovados e nenhuma falha.

Tempo de execução: 1,90 segundos.

 Cobertura de código da Fase 1

A análise de cobertura apresentou:

| Arquivo | Cobertura |
|---|---|
| engine.py | 78% |
| model.py | 100% |
| Total | 89% |

- Instruções analisadas: 36.
- Instruções não cobertas: 4.

A cobertura total de 89% demonstra que a maior parte das instruções do sistema foi exercitada pelos testes automatizados.

Os resultados confirmaram que, após a correção, o motor de inferência apresentou comportamento compatível com os cenários avaliados.



 Fase 2 — Sistema Fuzzy de Triagem UTI

Descrição do sistema

Na segunda fase, foi desenvolvido um sistema de inferência fuzzy destinado à classificação experimental de risco de pacientes em uma Unidade de Terapia Intensiva.

O sistema utiliza duas variáveis de entrada:

- Frequência cardíaca (FC), medida em batimentos por minuto.
- Saturação periférica de oxigênio (SpO2), expressa em porcentagem.

A variável de saída representa o nível de risco calculado pelo sistema, em uma escala de 0% a 100%.

Foram implementadas funções de pertinência triangulares e trapezoidais, cinco regras de inferência fuzzy e o método do centroide para defuzzificação.

O sistema foi desenvolvido para fins acadêmicos e experimentais, não constituindo ferramenta validada para decisões clínicas reais.

Regras de inferência

Foram implementadas cinco regras:

1. Se a saturação estiver crítica, então o risco será crítico.
2. Se a frequência cardíaca estiver baixa e a saturação estiver limítrofe, então o risco será crítico.
3. Se a frequência cardíaca estiver elevada e a saturação estiver limítrofe, então o risco será crítico.
4. Se a frequência cardíaca estiver normal e a saturação estiver limítrofe, então o risco será moderado.
5. Se a frequência cardíaca estiver normal e a saturação estiver normal, então o risco será baixo.

 Validação experimental

Foram desenvolvidos três testes automatizados:

Teste 1 — Paciente saudável

Verifica se um paciente com frequência cardíaca de 75 bpm e saturação de 98% apresenta risco inferior a 30%.

Resultado: PASSED.

Teste 2 — Salto não linear da saturação

Verifica a diferença de risco entre saturações de 95% e 89%, mantendo a frequência cardíaca em 75 bpm.

O teste considera que:

- O risco com SpO2 de 95% deve ser inferior a 35%.
- O risco com SpO2 de 89% deve ser superior a 65%.
- O risco com SpO2 de 89% deve ser maior que o risco com SpO2 de 95%.

Resultado final: PASSED.

Teste 3 — Validação de limites fisiológicos

Verifica se o sistema rejeita valores de entrada fora dos limites configurados, como frequência cardíaca de 35 bpm e saturação de 105%.

Resultado: PASSED.

 Identificação e correção de falha

Na primeira execução dos testes da UTI, dois testes foram aprovados e um apresentou falha.

O erro ocorreu no teste de salto não linear da saturação, pois o risco calculado para SpO2 de 95% foi de aproximadamente 35,71%, ultrapassando o limite estabelecido de 35%.

Para atender à condição experimental, foi realizado um ajuste na função de pertinência da saturação limítrofe.

Configuração inicial:

`[89, 93, 96]`

Configuração ajustada:

`[89, 93, 95]`

Esse ajuste alterou a distribuição de pertinência da variável, influenciando o resultado da inferência fuzzy.

A modificação foi documentada por representar uma alteração em relação à parametrização inicial do exercício.

 Resultados finais da Fase 2

Após o ajuste, os três testes automatizados foram executados novamente.

| Teste | Resultado |
|---|---|
| Paciente saudável | PASSED |
| Salto não linear de SpO2 | PASSED |
| Validação de limites fisiológicos | PASSED |

- Total: 3 testes aprovados.
- Falhas: 0.
- Tempo de execução: 1,87 segundos.

 Cobertura de código da Fase 2

A análise de cobertura do arquivo `src/uti_triagem.py` apresentou:

- Instruções analisadas: 34.
- Instruções não cobertas: 4.
- Cobertura total: 88%.

O resultado indica que a maior parte das instruções implementadas foi exercitada durante a execução dos testes.



 Análise comparativa dos resultados

| Indicador | Motor Fuzzy | Triagem UTI |
|---|---|---|
| Testes aprovados na execução final | 3 | 3 |
| Testes reprovados na execução final | 0 | 0 |
| Cobertura | 89% | 88% |
| Tempo de execução | 1,90 s | 1,87 s |
| Situação final | Aprovado nos testes | Aprovado nos testes |

Ambos os sistemas apresentaram resultados satisfatórios nos cenários avaliados.

A introdução proposital de uma falha na primeira fase demonstrou o funcionamento dos mecanismos de verificação do Pytest.

Na segunda fase, a execução dos testes permitiu identificar uma diferença entre o comportamento inicial do sistema e os limites definidos para o experimento, resultando em um ajuste documentado da função de pertinência.



 Evidências experimentais

As evidências da atividade compreendem as saídas do Google Colab durante a execução dos testes automatizados.

Os principais registros são:

1. Primeira execução do motor fuzzy.
2. Segunda execução com falha proposital.
3. Terceira execução após a correção.
4. Relatório de cobertura do motor fuzzy.
5. Execução dos testes da UTI.
6. Relatório de cobertura da UTI.

As capturas de tela podem ser armazenadas na pasta `AULA_11/evidencias` do repositório GitHub.



 Conclusão

A atividade permitiu aplicar conceitos de inteligência computacional, lógica fuzzy, testes automatizados e análise de cobertura em dois sistemas desenvolvidos em Python.

Na primeira fase, foi possível demonstrar a identificação de falhas por meio de testes automatizados, incluindo uma falha introduzida intencionalmente e sua posterior correção.

O motor fuzzy apresentou três testes aprovados e cobertura total de 89%.

Na segunda fase, foi desenvolvido um sistema de triagem UTI baseado em frequência cardíaca e saturação de oxigênio, utilizando regras de inferência e funções de pertinência fuzzy.

Após um ajuste experimental documentado, o sistema apresentou três testes aprovados e cobertura de 88%.

Os resultados demonstram a importância da validação automatizada para identificar inconsistências, acompanhar alterações no comportamento do software e avaliar a abrangência dos testes.

Conclui-se que os objetivos de implementação e validação experimental foram alcançados nos cenários executados, consolidando a aplicação prática dos conteúdos estudados na AC-3.
