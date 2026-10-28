
import pytest
from src.uti_triagem import (
    criar_sistema_triagem_uti,
    avaliar_paciente
)


@pytest.fixture
def simulador_uti():
    return criar_sistema_triagem_uti()


def test_paciente_saudavel_baixo_risco(simulador_uti):
    risco = avaliar_paciente(simulador_uti, 75, 98)

    print(f"Paciente saudavel: {risco:.2f}%")

    assert risco < 30.0


def test_salto_nao_linear_queda_spo2(simulador_uti):
    risco_95 = avaliar_paciente(simulador_uti, 75, 95)
    risco_89 = avaliar_paciente(simulador_uti, 75, 89)

    print(f"SpO2 95% - Risco: {risco_95:.2f}%")
    print(f"SpO2 89% - Risco: {risco_89:.2f}%")

    assert risco_95 < 35.0
    assert risco_89 > 65.0
    assert risco_89 > risco_95


def test_validacao_limites_fisiologicos(simulador_uti):
    with pytest.raises(ValueError):
        avaliar_paciente(simulador_uti, 35, 98)

    with pytest.raises(ValueError):
        avaliar_paciente(simulador_uti, 75, 105)

    print("Validacao de limites: OK")
