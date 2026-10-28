
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


def criar_modelo():
    impacto = ctrl.Antecedent(
        np.arange(0, 101, 1), "impacto"
    )
    explorabilidade = ctrl.Antecedent(
        np.arange(0, 10.1, 0.1), "explorabilidade"
    )
    urgencia = ctrl.Consequent(
        np.arange(0, 101, 1),
        "urgencia",
        defuzzify_method="centroid"
    )

    impacto["baixo"] = fuzz.trapmf(
        impacto.universe, [0, 0, 20, 40]
    )
    impacto["medio"] = fuzz.trimf(
        impacto.universe, [20, 50, 80]
    )
    impacto["alto"] = fuzz.trapmf(
        impacto.universe, [60, 80, 100, 100]
    )

    explorabilidade["baixa"] = fuzz.trapmf(
        explorabilidade.universe, [0, 0, 2, 4]
    )
    explorabilidade["media"] = fuzz.trimf(
        explorabilidade.universe, [2, 5, 8]
    )
    explorabilidade["alta"] = fuzz.trapmf(
        explorabilidade.universe, [6, 8, 10, 10]
    )

    urgencia["baixa"] = fuzz.trapmf(
        urgencia.universe, [0, 0, 15, 35]
    )
    urgencia["moderada"] = fuzz.trimf(
        urgencia.universe, [25, 50, 75]
    )
    urgencia["critica"] = fuzz.trapmf(
        urgencia.universe, [65, 85, 100, 100]
    )

    regras = [
        ctrl.Rule(
            impacto["baixo"] & explorabilidade["baixa"],
            urgencia["baixa"]
        ),
        ctrl.Rule(
            impacto["baixo"] & explorabilidade["media"],
            urgencia["baixa"]
        ),
        ctrl.Rule(
            impacto["baixo"] & explorabilidade["alta"],
            urgencia["moderada"]
        ),
        ctrl.Rule(
            impacto["medio"] & explorabilidade["baixa"],
            urgencia["moderada"]
        ),
        ctrl.Rule(
            impacto["medio"] & explorabilidade["media"],
            urgencia["moderada"]
        ),
        ctrl.Rule(
            impacto["medio"] & explorabilidade["alta"],
            urgencia["critica"]
        ),
        ctrl.Rule(
            impacto["alto"] & explorabilidade["baixa"],
            urgencia["moderada"]
        ),
        ctrl.Rule(
            impacto["alto"] & explorabilidade["media"],
            urgencia["critica"]
        ),
        ctrl.Rule(
            impacto["alto"] & explorabilidade["alta"],
            urgencia["critica"]
        )
    ]

    return ctrl.ControlSystem(regras)

