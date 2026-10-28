Segunda execução — Falha proposital

Foi realizada uma alteração proposital no teste `test_02_alto_risco`, modificando a condição de validação para `assert risco > 100`.

O motor fuzzy calculou um risco de 86,83%, provocando uma falha de asserção, conforme planejado.

**Resultados:**
- Teste 1: PASSED — 13,17%
- Teste 2: FAILED — 86,83% não é maior que 100%
- Teste 3: PASSED — validação de limites
- Total: 2 aprovados e 1 reprovado
- Tempo de execução: 1,33 segundos

A falha foi induzida intencionalmente para demonstrar a capacidade do Pytest de identificar condições incorretas.
