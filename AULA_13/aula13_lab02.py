import numpy as np

from pymoo.core.problem import ElementwiseProblem
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.operators.sampling.rnd import IntegerRandomSampling
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.operators.repair.rounding import RoundingRepair
from pymoo.optimize import minimize


class KubernetesClusterProblem(ElementwiseProblem):

    def __init__(self):
        super().__init__(
            n_var=2,
            n_obj=2,
            xl=np.array([2, 1]),
            xu=np.array([40, 12]),
            vtype=int
        )

    def _evaluate(self, x, out, *args, **kwargs):
        replicas, nodes = x[0], x[1]

        f1_tempo = (600 / replicas) + (200 / nodes)
        f2_custo = (replicas * 12) + (nodes * 85)

        out["F"] = [f1_tempo, f2_custo]


algorithm = NSGA2(
    pop_size=25,
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

res2 = minimize(
    KubernetesClusterProblem(),
    algorithm,
    termination=('n_gen', 35),
    seed=10
)

print("EXERCICIO 2 - CLUSTER KUBERNETES")

for x, f in zip(res2.X, res2.F):
    print(
        f"Replicas: {x[0]:.0f} | "
        f"Nodes: {x[1]:.0f} | "
        f"Tempo: {f[0]:.2f} ms | "
        f"Custo: US$ {f[1]:.2f}"
    )
