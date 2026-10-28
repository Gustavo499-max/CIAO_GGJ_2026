
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


def criar_sistema_triagem_uti():
    fc = ctrl.Antecedent(np.arange(40, 161), "freq_cardiaca")
    spo2 = ctrl.Antecedent(np.arange(70, 101), "spo2")
    risco = ctrl.Consequent(
        np.arange(0, 101), "risco",
        defuzzify_method="centroid"
    )

    fc["bradicardia"] = fuzz.trimf(fc.universe, [40, 40, 60])
    fc["normal"] = fuzz.trimf(fc.universe, [50, 75, 100])
    fc["taquicardia"] = fuzz.trapmf(
        fc.universe, [90, 110, 160, 160]
    )

    spo2["critica"] = fuzz.trapmf(
        spo2.universe, [70, 70, 88, 91]
    )
    spo2["limitrofe"] = fuzz.trimf(
        spo2.universe, [89, 93, 95]
    )
    spo2["normal"] = fuzz.trapmf(
        spo2.universe, [94, 97, 100, 100]
    )

    risco["baixo"] = fuzz.trimf(
        risco.universe, [0, 0, 35]
    )
    risco["moderado"] = fuzz.trimf(
        risco.universe, [25, 50, 75]
    )
    risco["critico"] = fuzz.trapmf(
        risco.universe, [65, 85, 100, 100]
    )

    regras = [
        ctrl.Rule(spo2["critica"], risco["critico"]),
        ctrl.Rule(
            fc["bradicardia"] & spo2["limitrofe"],
            risco["critico"]
        ),
        ctrl.Rule(
            fc["taquicardia"] & spo2["limitrofe"],
            risco["critico"]
        ),
        ctrl.Rule(
            fc["normal"] & spo2["limitrofe"],
            risco["moderado"]
        ),
        ctrl.Rule(
            fc["normal"] & spo2["normal"],
            risco["baixo"]
        )
    ]

    sistema = ctrl.ControlSystem(regras)
    return ctrl.ControlSystemSimulation(sistema)


def avaliar_paciente(simulador, bpm, spo2_val):
    if not 40 <= bpm <= 160:
        raise ValueError("Frequencia cardiaca invalida")

    if not 70 <= spo2_val <= 100:
        raise ValueError("Saturacao de oxigenio invalida")

    simulador.input["freq_cardiaca"] = bpm
    simulador.input["spo2"] = spo2_val
    simulador.compute()

    if "risco" not in simulador.output:
        raise ValueError("Nenhuma regra fuzzy ativada")

    return float(simulador.output["risco"])


if __name__ == "__main__":
    sim = criar_sistema_triagem_uti()
    print("Sistema de UTI instanciado com sucesso!")
    print(f"Risco: {avaliar_paciente(sim, 75, 98):.2f}%")
