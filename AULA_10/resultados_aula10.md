1. Por que o método do Centroide com triângulos não atinge matematicamente os 
   extremos 0% e 100%?

   O método Centroide calcula o centro de massa da área formada pelas funções de pertinência, como os triângulos possuem uma área distribuída ao longo de um intervalo, o centro de massa fica dentro dessa região, e não exatamente nas extremidades, por isso, mesmo com entradas mínimas (0, 0), o resultado pode ser 4,33% em vez de 0%, da mesma forma, com entradas máximas (100, 10), pode resultar em 87,5% em vez de 100%.



2. O que acontece com o resultado final se alterarmos a função da Urgência 
   Crítica para Trapézio (trapmf) na borda superior?

   Ao utilizar uma função trapezoidal (trapmf), a Urgência Crítica passa a ter uma região de pertinência máxima mais ampla, permitindo representar melhor os valores elevados, essa alteração modifica a distribuição da área e pode deslocar o resultado do Centroide para valores maiores, entretanto, não garante que o resultado alcance exatamente 100%, pois o Centroide continua calculando o centro de massa da região.


3. O que acontece se alterarmos o método de defuzzificação para 'MOM' 
   (Mean of Maximum)? Qual abordagem é mais recomendável e por quê?


   O método MOM calcula a média dos valores em que a função de pertinência atinge seu grau máximo, em vez de calcular o centro de massa de toda a área, isso pode aproximar ou levar o resultado aos extremos de 0% e 100%, dependendo do formato das funções de pertinência. Porém, o MOM pode provocar mudanças bruscas na saída, prejudicando a suavidade do sistema, a abordagem mais recomendável é manter o Centroide para preservar a suavidade das decisões, utilizando funções trapezoidais quando necessário, caso seja obrigatório atingir exatamente 0% e 100%, pode-se aplicar um tratamento específico para os extremos.



 4. Análise interpretativa da Superfície de Decisão 3D

A superfície de decisão 3D representa como a urgência varia de acordo com o Impacto e a Explorabilidade de um incidente, quando os dois valores são baixos, a urgência também é baixa, conforme o Impacto e a Explorabilidade aumentam, o sistema eleva gradualmente o nível de urgência, quando o Impacto é alto, a urgência se torna crítica, independentemente da Explorabilidade, conforme as regras estabelecidas, a superfície apresenta transições predominantemente suaves, demonstrando que o sistema Fuzzy Mamdani consegue tomar decisões graduais, evitando classificações rígidas.
