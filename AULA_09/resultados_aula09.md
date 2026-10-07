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
