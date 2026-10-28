
import pytest
from engine import avaliar_risco


def test_01_baixo_risco():
    risco = avaliar_risco(0, 0)
    print(f"\nTeste 1 - Baixo risco: {risco:.2f}%")
    assert 0 <= risco < 35


def test_02_alto_risco():
    risco = avaliar_risco(100, 10)
    print(f"\nTeste 2 - Alto risco: {risco:.2f}%")
    assert 65 < risco <= 100


def test_03_validacao_entrada():
    with pytest.raises(ValueError):
        avaliar_risco(120, 5)

    with pytest.raises(ValueError):
        avaliar_risco(50, 15)

    print("\nTeste 3 - Validacao de limites: OK")

