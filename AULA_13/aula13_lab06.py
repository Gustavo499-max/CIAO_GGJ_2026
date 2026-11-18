import numpy as np

from pymoo.core.problem import ElementwiseProblem
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.operators.sampling.rnd import IntegerRandomSampling
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.operators.repair.rounding import RoundingRepair
from pymoo.optimize import minimize
from pymoo.mcdm.pseudo_weights import PseudoWeights


class EscalaHospitalarProblem(ElementwiseProblem):

    def __init__(self):
        super().__init__(
            n_var=2,
            n_obj=2,
            n_ieq_constr=1,
            xl=np.array([2, 4]),
            xu=np.array([20, 40]),
            vtype=int
        )

    def _evaluate(self, x, out, *args, **kwargs):
        medicos, enfermeiros = x[0], x[1]

        f1_custo = (medicos * 1200.0) + (enfermeiros * 450.0)
        f2_espera = (180.0 / medicos) + (240.0 / enfermeiros)

        g1 = f2_espera - 25.0

        out["F"] = [f1_custo, f2_espera]
        out["G"] = [g1]


algorithm = NSGA2(
    pop_size=40,
    sampling=IntegerRandomSampling(),
    crossover=SBX(
        prob=0.9,
        eta=15,
        vtype=float,
        repair=RoundingRepair()
    ),
    mutation=PM(
        prob=0.2,
        eta=20,
        vtype=float,
        repair=RoundingRepair()
    ),
    eliminate_duplicates=True
)

res6 = minimize(
    EscalaHospitalarProblem(),
    algorithm,
    termination=('n_gen', 50),
    seed=42
)

solucoes_validas = res6.X[res6.G[:, 0] <= 0]
objetivos_validos = res6.F[res6.G[:, 0] <= 0]

if len(solucoes_validas) == 0:
    raise RuntimeError("Nenhuma solucao valida encontrada!")

pesos = np.array([0.40, 0.60])

indice_escolhido = PseudoWeights(pesos).do(objetivos_validos)

melhor_x = solucoes_validas[indice_escolhido]
melhor_f = objetivos_validos[indice_escolhido]

print("EXERCICIO 6 - ESCALA HOSPITALAR")
print("-" * 50)

print(f"Medicos: {melhor_x[0]:.0f}")
print(f"Enfermeiros: {melhor_x[1]:.0f}")
print(f"Custo do plantao: R$ {melhor_f[0]:.2f}")
print(f"Tempo de espera: {melhor_f[1]:.2f} minutos")

if melhor_f[1] <= 25.0:
    print("APROVADO: espera dentro do limite.")
else:
    print("REPROVADO: espera acima do limite.")

print("Total de solucoes validas:", len(solucoes_validas))
