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

def filtrar_por_categoria(categoria):
    gastos = ler_gastos()
    return [
        gasto for gasto in gastos
        if gasto["categoria"].lower() == categoria.lower()
    ]

def remover_gasto(id_gasto):
    gastos = ler_gastos()

    gastos_filtrados = [gasto for gasto in gastos if gasto["id"] != id_gasto]

    if len(gastos) == len(gastos_filtrados):
        return False

    salvar_gastos(gastos_filtrados)
    return True
    