Resultado
Lab 01-


RESULTADOS DO LAB 01
 Partículas         w1         w2         w3         w4         w5         w6  Soma dos pesos  Fitness (°C)
         10 0.00000000 0.00000000 0.00000000 1.00000000 0.00000000 0.00000000      1.00000000   30.00000000
         30 0.00000000 0.00000000 0.00000000 1.00000000 0.00000000 0.00000000      1.00000000   30.00000000
         50 0.00000000 0.00000000 0.00000000 1.00000000 0.00000000 0.00000000      1.00000000   30.00000000

Mínimo teórico: 30 °C (100% do tráfego na AZ4).


Lab02- 


DADOS DOS MICROSSERVIÇOS (ILUSTRATIVOS):
servico  valor  ram  cpu
   MS01     24  2.0  1.0
   MS02     18  1.5  0.5
   MS03     35  3.5  1.5
   MS04     29  2.0  1.0
   MS05     14  1.0  0.5
   MS06     40  4.0  2.0
   MS07     22  1.5  1.0
   MS08     31  3.0  1.5
   MS09     16  1.0  0.5
   MS10     37  3.5  1.5
   MS11     26  2.5  1.0
   MS12     20  1.5  1.0
   MS13     33  3.0  1.5
   MS14     15  1.0  0.5
   MS15     28  2.0  1.0

MELHORES SOLUÇÕES VIÁVEIS POR ESTRATÉGIA:
estrategia  repeticao  valor  ram  cpu      cromossomo                                                   servicos
         A          0  212.0 16.0  8.0 110110101011011 MS01, MS02, MS04, MS05, MS07, MS09, MS11, MS12, MS14, MS15
         B          0  212.0 16.0  8.0 110110101011011 MS01, MS02, MS04, MS05, MS07, MS09, MS11, MS12, MS14, MS15

MÉTRICAS FINAIS MÉDIAS EM 20 EXECUÇÕES:
estrategia  geracao  fitness_medio  fitness_dp_entre_execucoes  dp_populacional_medio  diversidade_media  melhor_viavel_medio
         A      120     136.379167                   11.042163              84.563896           0.212814                212.0
         B      120     199.804063                    1.502969              13.087372           0.212531                212.0


         
Serviços: MS01, MS02, MS04, MS05, MS07, MS09, MS11, MS12, MS14, MS15
RAM: 16.0 CPU: 8.0

CONCLUSÃO BASEADA NAS EXECUÇÕES:
Maior diversidade genética final média: A
Melhor valor viável: empate entre A e B: 212.0
Atenção: desvio-padrão de fitness não é, sozinho, medida de diversidade genética.

