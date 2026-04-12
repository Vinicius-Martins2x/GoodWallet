import json
from pathlib import Path

ARQUIVO = Path(__file__).resolve().parent.parent / "data" / "gastos.json"


def inicializar_arquivo():
    ARQUIVO.parent.mkdir(parents=True, exist_ok=True)

    if not ARQUIVO.exists():
        with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
            json.dump([], arquivo, ensure_ascii=False, indent=4)


def ler_gastos():
    inicializar_arquivo()

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_gastos(gastos):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(gastos, arquivo, ensure_ascii=False, indent=4)