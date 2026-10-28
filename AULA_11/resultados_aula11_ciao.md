Segunda execução — Falha proposital

Foi realizada uma alteração proposital no teste `test_02_alto_risco`, modificando a condição de validação para `assert risco > 100`.

O motor fuzzy calculou um risco de 86,83%, provocando uma falha de asserção, conforme planejado.

Resultados:
- Teste 1: PASSED — 13,17%
- Teste 2: FAILED — 86,83% não é maior que 100%
- Teste 3: PASSED — validação de limites
- Total: 2 aprovados e 1 reprovado
- Tempo de execução: 1,33 segundos

A falha foi induzida intencionalmente para demonstrar a capacidade do Pytest de identificar condições incorretas.



 Terceira execução — Correção dos erros

Após a identificação da falha proposital na segunda execução, foi restaurada a condição original do teste de alto risco.

A suíte foi executada novamente utilizando o Pytest, obtendo os seguintes resultados:

- Teste 1 — Baixo risco: PASSED (13,17%)
- Teste 2 — Alto risco: PASSED (86,83%)
- Teste 3 — Validação de limites: PASSED

Resultado: 3 testes aprovados, nenhuma falha.

Tempo de execução: 1,90 segundos.

Cobertura de código:
- engine.py: 78%
- model.py: 100%
- Cobertura total: 89%
- Instruções analisadas: 36
- Instruções não cobertas: 4

A terceira execução confirmou que a correção restaurou o comportamento esperado do sistema. A cobertura total de 89% demonstra que a maior parte das instruções do motor de inferência foi exercitada pelos testes automatizados.


## Resultado final — Sistema de Triagem UTI

O sistema fuzzy de triagem médica foi desenvolvido
com duas variáveis de entrada: frequência cardíaca
e saturação de oxigênio.

Foram implementadas cinco regras de inferência,
utilizando funções triangulares e trapezoidais.

### Validação experimental

Na execução inicial, dois testes passaram e um
falhou devido ao risco calculado para SpO2 de 95%.

Foi realizado um ajuste experimental na função
de pertinência limítrofe, alterando os parâmetros
de [89, 93, 96] para [89, 93, 95].

Após o ajuste, foram obtidos:

- Paciente saudável: PASSED
- Salto não linear de SpO2: PASSED
- Validação de limites fisiológicos: PASSED

### Cobertura de código

- Arquivo: src/uti_triagem.py
- Instruções analisadas: 34
- Instruções não cobertas: 4
- Cobertura total: 88%
- Tempo de execução: 1,87 segundos
- Resultado: 3 testes aprovados, nenhuma falha

### Conclusão

A validação experimental confirmou que o sistema
atendeu aos três critérios de teste após o ajuste
documentado na função de pertinência.

O projeto demonstrou a aplicação da lógica fuzzy,
dos testes automatizados e da análise de cobertura
na verificação de um motor de inferência.
