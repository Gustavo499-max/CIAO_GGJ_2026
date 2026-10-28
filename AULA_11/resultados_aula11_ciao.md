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
