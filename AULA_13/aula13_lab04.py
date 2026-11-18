import numpy as np

from pymoo.core.problem import ElementwiseProblem
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize
from pymoo.indicators.hv import HV


class RedeSensoresProblem(ElementwiseProblem):

    def __init__(self):
        super().__init__(
            n_var=2,
            n_obj=2,
            xl=np.array([1.0, 1.0]),
            xu=np.array([100.0, 60.0])
        )

    def _evaluate(self, x, out, *args, **kwargs):
        potencia, intervalo = x[0], x[1]

        f1_consumo_bateria = (potencia * 2.5) + (120.0 / intervalo)
        f2_perda_pacotes = (500.0 / potencia) + (intervalo * 0.8)

        out["F"] = [f1_consumo_bateria, f2_perda_pacotes]


res_curto = minimize(
    RedeSensoresProblem(),
    NSGA2(),
    termination=('n_gen', 10),
    seed=42
)

res_longo = minimize(
    RedeSensoresProblem(),
    NSGA2(),
    termination=('n_gen', 80),
    seed=42
)

ref_point = np.array([400.0, 600.0])
metrica_hv = HV(ref_point=ref_point)

hv_10_gen = metrica_hv(res_curto.F)
hv_80_gen = metrica_hv(res_longo.F)

print("EXERCICIO 4 - HIPERVOLUME")
print(f"Hipervolume (10 geracoes): {hv_10_gen:.6f}")
print(f"Hipervolume (80 geracoes): {hv_80_gen:.6f}")

if hv_80_gen > hv_10_gen:
    print("80 geracoes apresentou maior hipervolume.")
elif hv_80_gen < hv_10_gen:
    print("10 geracoes apresentou maior hipervolume.")
else:
    print("Hipervolumes iguais.")

print("Solucoes com 10 geracoes:", len(res_curto.F))
print("Solucoes com 80 geracoes:", len(res_longo.F))
