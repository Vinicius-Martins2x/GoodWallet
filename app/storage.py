import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

ARQUIVO_GASTOS = BASE_DIR / "data" / "gastos.json"
ARQUIVO_CONFIG = BASE_DIR / "data" / "config.json"


def inicializar_arquivo():
    ARQUIVO_GASTOS.parent.mkdir(parents=True, exist_ok=True)

    if not ARQUIVO_GASTOS.exists():
        with open(ARQUIVO_GASTOS, "w", encoding="utf-8") as arquivo:
            json.dump([], arquivo, ensure_ascii=False, indent=4)

    if not ARQUIVO_CONFIG.exists():
        with open(ARQUIVO_CONFIG, "w", encoding="utf-8") as arquivo:
            json.dump({"limite_mensal": 0}, arquivo, ensure_ascii=False, indent=4)


def ler_gastos():
    inicializar_arquivo()

    with open(ARQUIVO_GASTOS, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_gastos(gastos):
    with open(ARQUIVO_GASTOS, "w", encoding="utf-8") as arquivo:
        json.dump(gastos, arquivo, ensure_ascii=False, indent=4)


def ler_config():
    inicializar_arquivo()

    with open(ARQUIVO_CONFIG, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_config(config):
    with open(ARQUIVO_CONFIG, "w", encoding="utf-8") as arquivo:
        json.dump(config, arquivo, ensure_ascii=False, indent=4)