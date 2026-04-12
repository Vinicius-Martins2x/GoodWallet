from app.services import (
    adicionar_gasto,
    listar_gastos,
    calcular_total,
    remover_gasto,
    editar_gasto,
    filtrar_por_categoria,
    filtrar_por_mes,
    definir_limite_mensal,
    obter_limite_mensal,
    total_do_mes
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
    print("10. Sair")


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

            mostrar_gastos(listar_gastos())

        elif opcao == "3":

            print(f"Total gasto: R$ {calcular_total():.2f}")

        elif opcao == "4":

            try:

                id_gasto = int(input("ID do gasto: "))

                if remover_gasto(id_gasto):
                    print("Gasto removido.")
                else:
                    print("ID não encontrado.")

            except ValueError:
                print("ID inválido.")

        elif opcao == "5":

            try:

                id_gasto = int(input("ID do gasto: "))

                novo_valor = float(input("Novo valor: R$ "))
                nova_categoria = input("Nova categoria: ")
                nova_descricao = input("Nova descrição: ")
                nova_data = input("Nova data (AAAA-MM-DD): ")

                if editar_gasto(
                    id_gasto,
                    novo_valor,
                    nova_categoria,
                    nova_descricao,
                    nova_data
                ):
                    print("Gasto atualizado.")
                else:
                    print("ID não encontrado.")

            except ValueError:
                print("Dados inválidos.")

        elif opcao == "6":

            categoria = input("Categoria: ")

            mostrar_gastos(
                filtrar_por_categoria(categoria)
            )

        elif opcao == "7":

            mes = input("Mês (AAAA-MM): ")

            mostrar_gastos(
                filtrar_por_mes(mes)
            )

        elif opcao == "8":

            try:

                limite = float(input("Limite mensal: R$ "))

                definir_limite_mensal(limite)

                print("Limite definido.")

            except ValueError:
                print("Valor inválido.")

        elif opcao == "9":

            mes = input("Mês (AAAA-MM): ")

            total = total_do_mes(mes)

            limite = obter_limite_mensal()

            print(f"Total gasto no mês: R$ {total:.2f}")
            print(f"Limite mensal: R$ {limite:.2f}")

            if limite > 0 and total > limite:
                print("⚠️ Você ultrapassou o limite mensal.")
            elif limite > 0:
                print("Você ainda está dentro do limite.")

        elif opcao == "10":

            print("Encerrando o GoodWallet.")

            break

        else:

            print("Opção inválida.")


if __name__ == "__main__":
    main()