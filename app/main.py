from app.services import (
    adicionar_gasto,
    listar_gastos,
    calcular_total,
    remover_gasto,
    editar_gasto
)

from app.storage import inicializar_arquivo


def exibir_menu():
    print("\n=== GOODWALLET ===")
    print("1. Adicionar gasto")
    print("2. Listar gastos")
    print("3. Mostrar total gasto")
    print("4. Remover gasto")
    print("5. Editar gasto")
    print("6. Sair")


def main():
    inicializar_arquivo()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        # ADICIONAR GASTO
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
                print("Valor inválido. Digite um número válido.")

        # LISTAR GASTOS
        elif opcao == "2":
            gastos = listar_gastos()

            if not gastos:
                print("Nenhum gasto cadastrado.")
            else:
                print("\n--- Lista de Gastos ---")
                for gasto in gastos:
                    print(
                        f'ID: {gasto["id"]} | '
                        f'Valor: R$ {gasto["valor"]:.2f} | '
                        f'Categoria: {gasto["categoria"]} | '
                        f'Descrição: {gasto["descricao"]} | '
                        f'Data: {gasto["data"]}'
                    )

        # TOTAL GASTO
        elif opcao == "3":
            total = calcular_total()
            print(f"Total gasto: R$ {total:.2f}")

        # REMOVER GASTO
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

        # EDITAR GASTO
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

        # SAIR
        elif opcao == "6":
            print("Encerrando o GoodWallet.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()