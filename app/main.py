import requests
from app.services import (
    adicionar_gasto,
    calcular_total,
    definir_limite_mensal,
    editar_gasto,
    filtrar_por_categoria,
    filtrar_por_mes,
    grafico_por_categoria,
    listar_gastos,
    obter_limite_mensal,
    remover_gasto,
    total_do_mes,
)
from app.storage import inicializar_arquivo


def exibir_menu():
    print("\n=== GOODWALLET ===")
    print("1. Adicionar gasto")
    print("2. Listar gastos")
    print("3. Mostrar total gasto")
    print("4. Remover gasto")
    print("5. Editar gasto")
    print("6. Filtrar por categoria")
    print("7. Filtrar por mês")
    print("8. Definir limite mensal")
    print("9. Verificar limite do mês")
    print("10. Mostrar gráfico por categoria")
    print("11. Consultar cotação do Dólar/Euro (API Externa)")
    print("12. Sair")


def obter_cotacao_moedas():
    """Busca a cotação atual do USD e EUR para BRL usando a AwesomeAPI."""
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL"
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        
        dolar = float(dados['USDBRL']['bid'])
        euro = float(dados['EURBRL']['bid'])
        
        print("\n--- Cotações do Dia ---")
        print(f"Dólar (USD): R$ {dolar:.2f}")
        print(f"Euro (EUR): R$ {euro:.2f}")
        print("-----------------------")
        
    except requests.exceptions.RequestException:
        print("\nErro ao buscar cotações de moedas. Verifique sua conexão com a internet.")


def mostrar_gastos(gastos):
    if not gastos:
        print("Nenhum gasto encontrado.")
        return

    print("\n--- Lista de Gastos ---")

    for gasto in gastos:
        print(
            f'ID: {gasto["id"]} | '
            f'Valor: R$ {gasto["valor"]:.2f} | '
            f'Categoria: {gasto["categoria"]} | '
            f'Descrição: {gasto["descricao"]} | '
            f'Data: {gasto["data"]}'
        )


def main():
    inicializar_arquivo()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                valor = float(input("Valor: R$ "))
                categoria = input("Categoria: ").strip()
                descricao = input("Descrição: ").strip()
                data = input("Data (AAAA-MM-DD): ").strip()

                if valor <= 0:
                    print("O valor deve ser maior que zero.")
                    continue

                adicionar_gasto(valor, categoria, descricao, data)
                print("Gasto adicionado com sucesso.")

            except ValueError:
                print("Valor inválido.")

        elif opcao == "2":
            gastos = listar_gastos()
            mostrar_gastos(gastos)

        elif opcao == "3":
            total = calcular_total()
            print(f"Total gasto: R$ {total:.2f}")

        elif opcao == "4":
            try:
                id_gasto = int(input("Digite o ID do gasto que deseja remover: "))
                removido = remover_gasto(id_gasto)

                if removido:
                    print("Gasto removido com sucesso.")
                else:
                    print("ID não encontrado.")

            except ValueError:
                print("Digite um ID válido.")

        elif opcao == "5":
            try:
                id_gasto = int(input("Digite o ID do gasto que deseja editar: "))
                novo_valor = float(input("Novo valor: R$ "))
                nova_categoria = input("Nova categoria: ").strip()
                nova_descricao = input("Nova descrição: ").strip()
                nova_data = input("Nova data (AAAA-MM-DD): ").strip()

                if novo_valor <= 0:
                    print("O valor deve ser maior que zero.")
                    continue

                editado = editar_gasto(
                    id_gasto,
                    novo_valor,
                    nova_categoria,
                    nova_descricao,
                    nova_data
                )

                if editado:
                    print("Gasto editado com sucesso.")
                else:
                    print("ID não encontrado.")

            except ValueError:
                print("Dados inválidos.")

        elif opcao == "6":
            categoria = input("Digite a categoria para filtrar: ").strip()
            gastos_filtrados = filtrar_por_categoria(categoria)
            mostrar_gastos(gastos_filtrados)

        elif opcao == "7":
            mes = input("Digite o mês (AAAA-MM): ").strip()
            gastos_filtrados = filtrar_por_mes(mes)
            mostrar_gastos(gastos_filtrados)

        elif opcao == "8":
            try:
                limite = float(input("Digite o limite mensal: R$ "))

                if limite <= 0:
                    print("O limite deve ser maior que zero.")
                    continue

                definir_limite_mensal(limite)
                print("Limite mensal definido com sucesso.")

            except ValueError:
                print("Digite um valor válido.")

        elif opcao == "9":
            mes = input("Digite o mês para verificar (AAAA-MM): ").strip()
            total = total_do_mes(mes)
            limite = obter_limite_mensal()

            print(f"Total gasto no mês: R$ {total:.2f}")
            print(f"Limite mensal: R$ {limite:.2f}")

            if limite > 0 and total > limite:
                print("Atenção: você ultrapassou o limite mensal.")
            elif limite > 0:
                print("Você ainda está dentro do limite mensal.")
            else:
                print("Nenhum limite mensal foi definido.")

        elif opcao == "10":
            grafico_por_categoria()

        elif opcao == "11":  
            obter_cotacao_moedas()

        elif opcao == "12":  
            print("Encerrando o GoodWallet.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()