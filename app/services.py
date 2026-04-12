from app.storage import ler_gastos, salvar_gastos


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

    gastos_filtrados = [gasto for gasto in gastos if gasto["id"] != id_gasto]

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