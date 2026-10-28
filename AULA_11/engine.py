
from skfuzzy import control as ctrl
from model import criar_modelo


def avaliar_risco(impacto, explorabilidade):
    if not 0 <= impacto <= 100:
        raise ValueError("Impacto deve estar entre 0 e 100")

    if not 0 <= explorabilidade <= 10:
        raise ValueError(
            "Explorabilidade deve estar entre 0 e 10"
        )

    sistema = criar_modelo()
    simulador = ctrl.ControlSystemSimulation(sistema)

    simulador.input["impacto"] = impacto
    simulador.input["explorabilidade"] = explorabilidade
    simulador.compute()

    return float(simulador.output["urgencia"])


if __name__ == "__main__":
    cenarios = [
        (0, 0),
        (50, 5),
        (100, 10)
    ]

    for impacto, explorabilidade in cenarios:
        risco = avaliar_risco(impacto, explorabilidade)
        print(
            f"Impacto={impacto}% | "
            f"Explorabilidade={explorabilidade} | "
            f"Urgencia={risco:.2f}%"
        )

