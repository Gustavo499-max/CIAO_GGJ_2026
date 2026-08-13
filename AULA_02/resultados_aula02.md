
Lab01:

Total de solucoes avaliadas: 64
Tempo de execucao: 0.000365 segundos
Melhor valor encontrado: 8
Combinacao otima (0=nao leva, 1=leva): (1, 0, 1, 1, 0, 0)

Itens escolhidos:
 - Livro (peso: 2 , valor: 3 )
 - Camiseta (peso: 1 , valor: 2 )
 - Carregador (peso: 2 , valor: 3 )

 Relatorio:
1 - O resultado é 32 pois pois tem 5 itens e cada item tem 2 possibilidades então é feita a seguinte conta, 2x2x2x2x2= 32, agora caso a gente adicione mais um item com as mesmas 2 possibilidades a conta fica 2x2x2x2x2x2= 64 possiveis resultados
2 - O numero de resultados aumentaria para 32.768$ combinações, computador ainda resolveria isso em milissegundos, mas a complexidade aumentaria muito
3 - Investimentos: Um investimento com limite financeiro (capacidade) onde você escolhe em quais projetos aplicar dinheiro para obter o maior retorno possível, ou tambem em mapeamento de uma frota de caminhoes em uma operaçao logistica


Lab02: 

=================================================================
RESULTADOS DA FORCA-BRUTA NO TSP
=================================================================

>>> 4 cidades
    Rotas avaliadas : 6
    Melhor custo    : 80
    Melhor rota     : (0, 1, 3, 2, 0)
    Tempo (segundos): 0.000108

>>> 5 cidades
    Rotas avaliadas : 24
    Melhor custo    : 41
    Melhor rota     : (0, 1, 2, 3, 4, 0)
    Tempo (segundos): 0.000148

>>> 6 cidades
    Rotas avaliadas : 120
    Melhor custo    : 91
    Melhor rota     : (0, 1, 3, 4, 5, 2, 0)
    Tempo (segundos): 0.000415

=================================================================
OBSERVE: o numero de rotas cresce como (n-1)!  (fatorial)
4 cidades -> 6 rotas | 5 -> 24 | 6 -> 120 | 10 -> 362880 | 15 -> 87 bilhoes
=================================================================


 Relatorio:
 1 - podemos ver que o numero de rotas cresce bem mais rapido do que de forma linear ou quadratica, ele cresce de forma fatorial, de 4 pra 5 cidades ele cresceu 4x mais e de 5 pra 6 cidades ele cresceu 5x mais
 2 - levando em consideração que o numero de rotas esta crescendo de forma fatorial, caso fosse 10 cidades o numero de rotas seria de 362.880 rotas, com isso usando como base o tempo de 6 cidades o tempo estimado de 10 ciaddes seria de aproximadamente de 1.25 segundos
 3 - Por conta do crescimento do tempo


