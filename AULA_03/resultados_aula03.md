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


   


   

