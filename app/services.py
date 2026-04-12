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