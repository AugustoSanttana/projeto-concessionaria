from main import *

concessionaria = Concessionaria(Veiculo, Cliente, Vendedor)

def menu():
    print('-=' * 13)
    print('--- Menu Concessionária ---')
    print('-=' * 13)
    print('[1] Cadastrar Veículo')
    print('[2] Cadastrar Vendedor')
    print('[3] Cadastrar Cliente')
    print('[4] Listar Veículos')
    print('[5] Listar Vendedores')
    print('[6] Listar Clientes')
    print('[7] Efetuar Venda')
    print('[8] Listar Vendas')
    print('[9] Apagar Vendedor')
    print('[10] Pesquisar Clientes')
    print('[11] Atualizar Salário Vendedor')
    print('[12] Sair')

    while True:
        try:
            escolha = int(input('>>>>>>>>>>>>>>>>>>>'))
            while escolha not in range(1, 13):
                print('Opção inválida!')
                escolha = int(input('>>>>>>>>>>>>>>>>>>>'))
            break
        except ValueError:
            print('Opção inválida!')
                  
    match(escolha):
        case 1:
            concessionaria.cadastrar_veiculo()

        case 2:
            concessionaria.cadastrar_vendedor()

        case 3:
            concessionaria.cadastrar_cliente()

        case 4:
            concessionaria.listar_veiculos()

        case 5:
            concessionaria.listar_vendedores()

        case 6:
            concessionaria.listar_clientes()

        case 7:
            concessionaria.vender()

        case 8:
            concessionaria.listar_vendas()

        case 9:
            concessionaria.deletar_vendedor()

        case 10:
            concessionaria.filtrar_cliente()

        case 11:
            concessionaria.atualizar_salario()

        case 12:
            input('Programa finalizado!')
            quit()

while True:
    menu()
            