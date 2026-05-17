from unittest.mock import patch
import requests

from app.services import (
    adicionar_gasto,
    calcular_total,
    definir_limite_mensal,
    editar_gasto,
    filtrar_por_categoria,
    filtrar_por_mes,
    listar_gastos,
    obter_limite_mensal,
    remover_gasto,
    total_do_mes,
)
from app.storage import salvar_config, salvar_gastos


def setup_function():
    salvar_gastos([])
    salvar_config({"limite_mensal": 0})


def test_adicionar_e_listar_gastos():
    adicionar_gasto(50.0, "Alimentação", "Almoço", "2026-04-12")

    gastos = listar_gastos()

    assert len(gastos) == 1
    assert gastos[0]["valor"] == 50.0
    assert gastos[0]["categoria"] == "Alimentação"
    assert gastos[0]["descricao"] == "Almoço"
    assert gastos[0]["data"] == "2026-04-12"


def test_calcular_total():
    adicionar_gasto(50.0, "Alimentação", "Almoço", "2026-04-12")
    adicionar_gasto(20.0, "Transporte", "Ônibus", "2026-04-12")

    total = calcular_total()

    assert total == 70.0


def test_remover_gasto():
    adicionar_gasto(50.0, "Alimentação", "Almoço", "2026-04-12")
    adicionar_gasto(20.0, "Transporte", "Ônibus", "2026-04-12")

    removido = remover_gasto(1)
    gastos = listar_gastos()

    assert removido is True
    assert len(gastos) == 1
    assert gastos[0]["id"] == 2


def test_remover_gasto_inexistente():
    adicionar_gasto(50.0, "Alimentação", "Almoço", "2026-04-12")

    removido = remover_gasto(999)

    assert removido is False


def test_editar_gasto():
    adicionar_gasto(50.0, "Alimentação", "Almoço", "2026-04-12")

    editado = editar_gasto(1, 80.0, "Lazer", "Cinema", "2026-04-13")

    gastos = listar_gastos()

    assert editado is True
    assert gastos[0]["valor"] == 80.0
    assert gastos[0]["categoria"] == "Lazer"
    assert gastos[0]["descricao"] == "Cinema"
    assert gastos[0]["data"] == "2026-04-13"


def test_filtrar_por_categoria():
    adicionar_gasto(50.0, "Alimentação", "Almoço", "2026-04-12")
    adicionar_gasto(20.0, "Transporte", "Ônibus", "2026-04-12")
    adicionar_gasto(30.0, "Alimentação", "Jantar", "2026-04-13")

    gastos_filtrados = filtrar_por_categoria("Alimentação")

    assert len(gastos_filtrados) == 2
    assert all(g["categoria"] == "Alimentação" for g in gastos_filtrados)


def test_filtrar_por_mes():
    adicionar_gasto(50.0, "Alimentação", "Almoço", "2026-04-12")
    adicionar_gasto(20.0, "Transporte", "Ônibus", "2026-05-12")
    adicionar_gasto(30.0, "Lazer", "Cinema", "2026-04-20")

    gastos_filtrados = filtrar_por_mes("2026-04")

    assert len(gastos_filtrados) == 2
    assert all(g["data"].startswith("2026-04") for g in gastos_filtrados)


def test_definir_e_obter_limite_mensal():
    definir_limite_mensal(500.0)

    limite = obter_limite_mensal()

    assert limite == 500.0


def test_total_do_mes():
    adicionar_gasto(50.0, "Alimentação", "Almoço", "2026-04-12")
    adicionar_gasto(20.0, "Transporte", "Ônibus", "2026-04-15")
    adicionar_gasto(30.0, "Lazer", "Cinema", "2026-05-01")

    total = total_do_mes("2026-04")

    assert total == 70.0

@patch("requests.get")
def test_obter_cotacao_moedas_com_sucesso(mock_get):
    """Testa a integridade da comunicação externa simulando a AwesomeAPI."""
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL"
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "USDBRL": {"bid": "5.10"},
        "EURBRL": {"bid": "5.50"},
    }

    response = requests.get(url)
    dados = response.json()

    assert response.status_code == 200
    assert "USDBRL" in dados
    assert dados["USDBRL"]["bid"] == "5.10"