Resultado Lab01-


A lógica fuzzy é utilizada para trabalhar com situações em que os valores não precisam pertencer exclusivamente a uma única categoria. Diferentemente da lógica tradicional, na qual uma condição normalmente é verdadeira ou falsa, a lógica fuzzy permite graus de pertinência entre 0 e 1.
Neste sistema, a variável de entrada é a temperatura, que varia de 0°C a 40°C, enquanto a variável de saída é a velocidade do ventilador, variando de 0% a 100%.
A temperatura foi dividida em três conjuntos fuzzy: frio, morno e quente. Já a velocidade do ventilador foi dividida em baixa, média e alta.
As funções de pertinência permitem que uma mesma temperatura pertença parcialmente a mais de um conjunto. Por exemplo, uma temperatura de 20°C pode possuir determinado grau de pertinência ao conjunto "frio" e, ao mesmo tempo, ao conjunto "morno". Isso permite que a mudança na velocidade do ventilador aconteça de maneira gradual.

O sistema utiliza três regras principais:
1. SE a temperatura for fria, ENTÃO a velocidade do ventilador será baixa.
2. SE a temperatura for morna, ENTÃO a velocidade do ventilador será média.
3. SE a temperatura for quente, ENTÃO a velocidade do ventilador será alta.
Quando uma temperatura é informada, o sistema calcula seu grau de pertinência em cada conjunto fuzzy. Em seguida, verifica quais regras devem ser ativadas e com qual intensidade.
Após a aplicação das regras, o sistema realiza a defuzzificação, transformando o resultado fuzzy em um valor numérico de velocidade. Dessa forma, em vez de simplesmente determinar que o ventilador deve estar "baixo", "médio" ou "alto", o sistema consegue fornecer uma saída concreta, como 30%, 50% ou 75%.

Isso evita mudanças bruscas de velocidade e demonstra como sistemas fuzzy podem ser utilizados em aplicações de automação e controle, como ventiladores inteligentes, ar-condicionado, climatização de ambientes e sistemas IoT.




Lab02-

1- Ao utilizar o operador E (&), a regra se torna mais restritiva, pois serviço e comida precisam pertencer ao conjunto médio simultaneamente. Para serviço 7 e comida 3, a intensidade da regra é determinada pelo menor grau de pertinência das duas entradas. Isso altera a influência da gorjeta média no resultado final.

2- As funções triangulares possuem segmentos retos e mudanças mais definidas entre os conjuntos. Já uma função gaussiana apresenta curvas suaves, fazendo com que a transição entre "ruim", "médio" e "bom" aconteça de maneira mais gradual. A utilização de funções gaussianas torna as transições entre os conjuntos fuzzy mais suaves. Dessa forma, pequenas mudanças na nota do serviço tendem a gerar mudanças graduais no resultado. Os trapézios também modificam o comportamento porque permitem regiões maiores de pertinência máxima.

3- Os métodos de defuzzificação transformam a saída fuzzy em um valor numérico. O método centroid utiliza o centro de gravidade da área resultante, o bisector encontra o ponto que divide a área em duas partes iguais e o mom utiliza a média dos pontos de máxima pertinência. Por isso, a porcentagem final da gorjeta pode variar entre os métodos.

4- A criação do conjunto "excelente" permite representar melhor notas muito altas de serviço. Uma nota próxima de 9 ou 10 terá forte pertinência nesse conjunto, ativando uma regra específica para recomendar uma gorjeta alta. Isso aumenta o nível de detalhamento do sistema fuzzy.

5-Os resultados apresentam comportamento coerente com as regras definidas. Quando serviço e comida recebem nota 0, o sistema recomenda uma gorjeta baixa. Quando recebem nota 10, recomenda uma gorjeta alta. Para notas 5, o sistema tende a recomendar uma gorjeta média. Isso demonstra que as funções de pertinência e as regras fuzzy estão funcionando de acordo com o esperado.


Nota do serviço (0-10) [7]: 7
Nota da comida (0-10) [3]: 3

============================================================
          RESULTADO DO SISTEMA FUZZY
============================================================
Nota do serviço: 7.0
Nota da comida: 3.0
Gorjeta sugerida: 12.5%

============================================================
     GRAUS DE PERTINÊNCIA DO SERVIÇO
============================================================
Ruim  : 0.00
Médio : 0.60
Bom   : 0.40

============================================================
      GRAUS DE PERTINÊNCIA DA COMIDA
============================================================
Ruim  : 0.40
Médio : 0.60
Bom   : 0.00


Lab03-

O projeto tem como objetivo desenvolver um sistema fuzzy para determinar o tempo ideal de irrigação de uma plantação ou jardim.
Atualmente, a decisão de irrigar pode ser realizada manualmente pelo responsável, considerando principalmente a temperatura ambiente e a umidade do solo.
O sistema utilizará duas entradas numéricas: temperatura ambiente, medida em graus Celsius (°C), e umidade do solo, medida em porcentagem (%).
A saída será o tempo recomendado de irrigação, medido em minutos.
A lógica fuzzy é adequada porque conceitos como solo seco, temperatura quente e irrigação longa não possuem limites exatos. Além disso, a necessidade de água depende da combinação das duas entradas, tornando inadequada uma decisão baseada em apenas uma condição simples.

Base de regras
Eu colocaria 9 regras, porque assim cobrimos praticamente todas as combinações possíveis:
1. SE umidade é seca E temperatura é quente → irrigação longa.
2. SE umidade é seca E temperatura é agradável → irrigação longa.
3. SE umidade é seca E temperatura é fria → irrigação média.
4. SE umidade é média E temperatura é quente → irrigação média.
5. SE umidade é média E temperatura é agradável → irrigação média.
6. SE umidade é média E temperatura é fria → irrigação curta.
7. SE umidade é úmida E temperatura é quente → irrigação curta.
8. SE umidade é úmida E temperatura é agradável → irrigação curta.
9. SE umidade é úmida OU temperatura é fria → irrigação curta.

============================================================
       SISTEMA FUZZY DE IRRIGAÇÃO INTELIGENTE
============================================================
Digite a temperatura ambiente (0 a 40 °C): 35
Digite a umidade do solo (0 a 100%): 58

============================================================
                    RESULTADO
============================================================
Temperatura: 35.0 °C
Umidade do solo: 58.0%
Tempo recomendado de irrigação: 13.4 minutos
