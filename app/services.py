import matplotlib.pyplot as plt

from app.storage import ler_config, ler_gastos, salvar_config, salvar_gastos


def adicionar_gasto(valor, categoria, descricao, data):
    gastos = ler_gastos()

    novo_gasto = {
        "id": len(gastos) + 1,
        "valor": valor,
        "categoria": categoria,
        "descricao": descricao,
        "data": data
    }

    gastos.append(novo_gasto)
    salvar_gastos(gastos)


def listar_gastos():
    return ler_gastos()


def calcular_total():
    gastos = ler_gastos()
    return sum(gasto["valor"] for gasto in gastos)


def remover_gasto(id_gasto):
    gastos = ler_gastos()

    gastos_filtrados = [
        gasto for gasto in gastos
        if gasto["id"] != id_gasto
    ]

    if len(gastos) == len(gastos_filtrados):
        return False

    salvar_gastos(gastos_filtrados)
    return True


def editar_gasto(id_gasto, novo_valor, nova_categoria, nova_descricao, nova_data):
    gastos = ler_gastos()

    for gasto in gastos:
        if gasto["id"] == id_gasto:
            gasto["valor"] = novo_valor
            gasto["categoria"] = nova_categoria
            gasto["descricao"] = nova_descricao
            gasto["data"] = nova_data

            salvar_gastos(gastos)
            return True

    return False


def filtrar_por_categoria(categoria):
    gastos = ler_gastos()

    return [
        gasto for gasto in gastos
        if gasto["categoria"].lower() == categoria.lower()
    ]


def filtrar_por_mes(mes):
    gastos = ler_gastos()

    return [
        gasto for gasto in gastos
        if gasto["data"].startswith(mes)
    ]


def definir_limite_mensal(limite):
    config = ler_config()
    config["limite_mensal"] = limite
    salvar_config(config)


def obter_limite_mensal():
    config = ler_config()
    return config.get("limite_mensal", 0)


def total_do_mes(mes):
    gastos = ler_gastos()

    return sum(
        gasto["valor"]
        for gasto in gastos
        if gasto["data"].startswith(mes)
    )


def grafico_por_categoria():
    gastos = ler_gastos()

    if not gastos:
        print("Nenhum gasto cadastrado.")
        return

    categorias = {}

    for gasto in gastos:
        categoria = gasto["categoria"]
        categorias[categoria] = categorias.get(categoria, 0) + gasto["valor"]

    nomes = list(categorias.keys())
    valores = list(categorias.values())

    plt.figure(figsize=(8, 5))
    plt.bar(nomes, valores)
    plt.title("Gastos por Categoria")
    plt.xlabel("Categoria")
    plt.ylabel("Valor")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()