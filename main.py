from sqlalchemy import create_engine, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from time import sleep
import datetime

db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class Veiculo(Base):
    __tablename__ = "veiculos"
    marca = Column(String)
    modelo = Column(String)
    ano = Column(Integer)
    cor = Column(String)
    categoria = Column(String)
    cambio = Column(String)
    valor = Column(Float)
    km = Column(Float)
    placa = Column(String, primary_key=True)

    def __init__(self, marca, modelo, ano, cor, cambio, categoria, valor, placa, km):
        self.set_marca(marca)
        self.set_modelo(modelo)
        self.set_ano(ano)
        self.set_cor(cor)
        self.set_cambio(cambio)
        self.set_categoria(categoria)
        self.set_valor(valor)
        self.set_placa(placa)
        self.set_km(km)

    def set_marca(self, marca):
        while not marca:
            marca = input("Digite uma marca: ").upper()
        self.marca = marca

    def set_modelo(self, modelo):
        while not modelo:
            modelo = input("Digite um modelo: ").upper()
        self.modelo = modelo
    
    def set_ano(self, ano):
        while True:
            try:
                ano = int(ano)
                self.ano = ano  
                break
            except ValueError:
                ano = input("Ano inválido. Por favor, digite um ano válido: ")
    
    def set_cor(self, cor):
        while not cor:
            cor = input("Digite uma cor: ").upper()
        self.cor = cor
    
    def set_cambio(self, cambio):
        while not cambio:
            cambio = input("Digite um cambio: ").upper()
        self.cambio = cambio
    
    def set_categoria(self, categoria):
        while not categoria:
            categoria = input("Digite uma categoria: ").upper()
        self.categoria = categoria

    def set_valor(self, valor):
        while True:
            try:
                valor = float(valor)
                while valor < 0:
                    valor = input("Valor do veículo não pode ser negativo. Digite novamente: ")
                    valor = float(valor)
                self.valor = valor
                break
            except ValueError:
                valor = input("Valor do veículo inválido. Por favor, digite um valor válido: ")

    def set_placa(self, placa):
        while not placa:
            placa = input("Digite a placa: ").upper()
        self.placa = placa
        
    def set_km(self, km):
        while True:
            try:
                km = float(km)
                while km < 0:
                    km = input("KM do veículo não pode ser negativo. Digite novamente: ")
                    km = float(km)
                self.km = km
                break
            except ValueError:
                km = input("KM do veículo inválido. Por favor, digite um KM válido: ")



    
class Venda(Base):

    __tablename__ = "vendas"

    id = Column(Integer, primary_key=True)
    nome_cliente = Column(String, ForeignKey('clientes.nome'))
    marca_veiculo = Column(String, ForeignKey('veiculos.marca'))
    modelo_veiculo = Column(String, ForeignKey('veiculos.modelo'))
    placa_veiculo = Column(String, ForeignKey('veiculos.placa'))
    nome_vendedor = Column(String, ForeignKey('vendedores.nome'))
    cpf_cliente = Column(String, ForeignKey('clientes.cpf'))
    cpf_vendedor = Column(String, ForeignKey('vendedores.cpf'))
    data_venda = Column(String)


    def __init__(self, nome_cliente, modelo_veiculo, marca_veiculo, placa_veiculo, nome_vendedor, cpf_cliente, cpf_vendedor, data_venda):
        self.nome_cliente = nome_cliente
        self.modelo_veiculo = modelo_veiculo
        self.marca_veiculo = marca_veiculo
        self.placa_veiculo = placa_veiculo
        self.nome_vendedor = nome_vendedor
        self.cpf_cliente = cpf_cliente
        self.cpf_vendedor = cpf_vendedor
        self.data_venda = data_venda


class Cliente(Base):
    __tablename__ = "clientes"
    nome = Column(String)
    idade = Column(Integer)
    cpf = Column(String, primary_key=True)

    def __init__(self, nome, idade, cpf):
        self.set_nome(nome)
        self.set_idade(idade)
        self.set_cpf(cpf)

    def set_nome(self, nome):
        while not nome:
            nome = input("Digite o nome do cliente: ").title()
        self.nome = nome

    def set_idade(self, idade):
        while True:
            try:
                idade = int(idade)
                while idade < 18:
                    idade = int(input("Idade inválida, deve ser +18 anos: "))
                self.idade = idade
                break
            except ValueError:
                idade = input("Idade inválida. Por favor, digite uma idade válida: ")



    def set_cpf(self, cpf):
        while len(cpf) != 11:
            cpf = input("CPF inválido, tente novamente: ")
        self.cpf = cpf


class Vendedor(Base):
    __tablename__ = "vendedores"
    nome = Column(String)
    idade = Column(Integer)
    cpf = Column(String, primary_key=True)
    salario = Column(Float)
    comissao = Column(Float)

    def __init__(self, nome, idade, cpf, salario, comissao):
        self.set_nome(nome)
        self.set_idade(idade)
        self.set_cpf(cpf)
        self.set_salario(salario)
        self.comissao = comissao

    def set_nome(self, nome):
        while not nome:
            nome = input("Digite o nome do vendedor: ").title()
        self.nome = nome

    def set_idade(self, idade):

        while True:
            try:
                idade = int(idade)
                while idade < 16:
                    idade = int(input("Idade inválida, deve ser +16 anos: "))
                self.idade = idade
                break
            except ValueError:
                idade = input("Idade inválida. Por favor, digite uma idade válida: ")
    

    def set_cpf(self, cpf):
        while len(cpf) != 11:
            cpf = input("CPF inválido, tente novamente: ")
        self.cpf = cpf

    
    def set_salario(self, salario):
        while True:
            try:
                salario = float(salario)
                while salario < 0:
                    salario = input("Salário não pode ser negativo. Digite novamente: ")
                    salario = float(salario)
                self.salario = salario
                break
            except ValueError:
                salario = input("Salário inválido. Por favor, digite um salário válido: ")


Base.metadata.create_all(bind=db)

class Concessionaria:
    def __init__(self, veiculo: Veiculo, cliente: Cliente, vendedor: Vendedor):
        self.veiculo = veiculo
        self.cliente = cliente
        self.vendedor = vendedor

    def listar_veiculos(self):
        print('--- LISTA DE VEÍCULOS ---\n')
        carros = session.query(Veiculo).all()
        for carro in carros:
            print(f"--- {carro.marca} {carro.modelo} ---\n Ano: {carro.ano}\n "
                  f"Cor: {carro.cor}\n Categoria: {carro.categoria}\n Cambio: {carro.cambio}\n "
                  f"Valor: R${carro.valor:,.2f}\n KM: {carro.km}\n Placa: {carro.placa}\n")
            sleep(0.3)

    def set_placa(self, placa):
        veiculo = session.query(Veiculo).filter_by(placa=placa).first()
        if veiculo:
            print("Veículo ja cadastrado.")
            return False
        else:
            self.placa = placa
            return True
        
    def cadastrar_veiculo(self):
        print("--- DADOS DO VEÍCULO --- \n")
        marca = input("Marca: ").upper()
        modelo = input("Modelo: ").upper()
        ano = input("Ano: ")
        cor = input("Cor: ").upper()
        cambio = input("Câmbio: ").upper()
        categoria = input("Categoria: ").upper()
        valor = input("Valor: ")
        km = input("Quilometragem aproximada: ")
        placa = input("Placa: ").upper()
        print()

        if not self.set_placa(placa):
            return
        
        carro = Veiculo(marca, modelo, ano, cor, cambio, categoria, valor, placa, km)
        session.add(carro)
        session.commit()
        print("Veiculo cadastrado com sucesso!\n")

    def set_cpf_cliente(self, cpf_cliente):
        cliente = session.query(Cliente).filter_by(cpf=cpf_cliente).first()
        if cliente:
            print("Cliente já cadastrado.")
            return False
        else:
            self.cpf_cliente = cpf_cliente
            return True

    def cadastrar_cliente(self):
        print("--- DADOS DO CLIENTE --- \n")
        cpf_cliente = input("Digite o CPF do cliente: ")

        if not self.set_cpf_cliente(cpf_cliente):
            return
        
        nome_cliente = input("Digite o nome do cliente: ").title()
        idade_cliente = input("Digite a idade do cliente: ")
        
        cliente = Cliente(nome_cliente, idade_cliente, cpf_cliente)
        session.add(cliente)
        session.commit()
        print("\nCliente cadastrado com sucesso!\n")
        

    def set_cpf_vendedor(self, cpf):
        vendedor = session.query(Vendedor).filter_by(cpf=cpf).first()
        if vendedor:
            print("\nVendedor já cadastrado.\n")
            return False
        else:
            self.cpf = cpf
            return True

    def cadastrar_vendedor(self):
        print("--- DADOS DO VENDEDOR --- \n")
        cpf = input("Digite seu CPF: ")
        nome = input("Digite seu nome: ").title()
        idade = input("Digite sua idade: ")
        

        if not self.set_cpf_vendedor(cpf):
            return

        salario = input("Digite o salário do vendedor: ")
        comissao = 0
        vendedor = Vendedor(nome, idade, cpf, salario, comissao)
        session.add(vendedor)
        session.commit()
        print("\nVendedor cadastrado com sucesso!\n")
        


    def vender(self):
      print("--- VENDER VEÍCULO ---\n")
      placa = input("Digite a placa do veículo a ser vendido: ").upper()

      veiculo = session.query(Veiculo).filter_by(placa=placa).first()
      if not veiculo:
        print("Veículo não encontrado.")
        return

      cpf_vendedor = input("Digite o CPF do vendedor: ")
      vendedor = session.query(Vendedor).filter_by(cpf=cpf_vendedor).first()
      if not vendedor:
          print("Vendedor não encontrado. Por favor, cadastre o vendedor primeiro.\n")
          return

      cpf_cliente = input("Digite o CPF do cliente: ")
      cliente = session.query(Cliente).filter_by(cpf=cpf_cliente).first()
      if not cliente:
          print("Cliente não encontrado. Por favor, cadastre o cliente primeiro.")
          return

        # Calcula a comissão e adiciona ao vendedor
      comissao = veiculo.valor * 0.05
      vendedor.comissao += comissao

        # Cria uma nova venda e adiciona ao banco de dados
      data_venda = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
      venda = Venda(nome_cliente=cliente.nome, modelo_veiculo=veiculo.modelo, marca_veiculo=veiculo.marca, placa_veiculo=placa, nome_vendedor=vendedor.nome, cpf_cliente=cpf_cliente, cpf_vendedor=cpf_vendedor, data_venda=data_venda)
      session.add(venda)
        
        # Remove o veículo vendido do banco de dados
      session.delete(veiculo)

        # Commit das alterações
      session.commit()
      print(f"\nVenda registrada com sucesso: {veiculo.marca} {veiculo.modelo} vendido para {cliente.nome} por R${veiculo.valor:,.2f}.\n")


    def listar_vendas(self):
        vendas = session.query(Venda).all()
        if not vendas:
            print("Nenhuma venda registrada.")
            return

        print('--- Vendas ---\n')

        for venda in vendas:
            print(f"Veículo: {venda.marca_veiculo} {venda.modelo_veiculo} \n"
                f"Placa: {venda.placa_veiculo}\n"
                f"Cliente: {venda.nome_cliente}\n"
                f"Vendedor: {venda.nome_vendedor}\n"
                f"Data: {venda.data_venda}\n")
            sleep(0.3)

            
    def listar_vendedores(self):
        vendedores = session.query(Vendedor).all()
        if not vendedores:
            print("Nenhum vendedor registrado.")
            return
        print("--- VENDEDORES ---\n")
        for vendedor in vendedores:
            print(f"Nome: {vendedor.nome}\n"
                  f"Idade: {vendedor.idade}\n"
                  f"CPF: {vendedor.cpf}\n"
                  f"Salário: R${vendedor.salario:,.2f}\n"
                  f"Comissao: R${vendedor.comissao:,.2f}\n"
                  f"Total a receber: R${vendedor.salario + vendedor.comissao:,.2f}\n")
            sleep(0.3)
            
            
    def listar_clientes(self):
        clientes = session.query(Cliente).all()

        if not clientes:
            print("Nenhum cliente registrado.\n")
            return
        
        print(f"--- CLIENTES CADASTRADOS ---\n")
        print(f' {len(clientes)} Clientes encontrados\n')
        for cliente in clientes:
            print(f"Nome: {cliente.nome}\n"
                  f"Idade: {cliente.idade}\n"
                  f"CPF: {cliente.cpf}\n")
            sleep(0.3)

    def deletar_vendedor(self):
        print(f"--- APAGAR VENDEDOR ---\n")
        cpf = str(input('Digite o CPF do vendedor:'))

        vendedor = session.query(Vendedor).filter_by(cpf=cpf).first()
        if vendedor:

            confirm = str(input(f'Apagar vendedor:{vendedor.nome}?[s/n]:')).lower()
            while confirm not in ('n', 's'):
                print('Opção inválida!')
                confirm = str(input(f'Apagar vendedor:{vendedor.nome}?[s/n]:')).lower()

            if confirm == 's':
                print(f'Vendedor "{vendedor.nome}" deletado com sucesso!\n')
                session.delete(vendedor)
                session.commit()
                return

            else:
                print('Deletagem cancelada!\n')
                return

        else:
            print('\nVendedor não encontrado!\n')
            return

    def filtrar_cliente(self):
        print(f"--- PESQUISAR CLIENTES ---\n")
        print('[1] Encontrar por Nome')
        print('[2] Encontrar por CPF')

        while True:
            try:
                escolha = int(input('>>>>>>>>>>>>>>>>>>>'))
                while escolha not in range(1, 3):
                    print('Opção inválida!')
                    escolha = int(input('>>>>>>>>>>>>>>>>>>>'))
                break
            except ValueError:
                print('Opção inválida!')

        match(escolha):
            case 1:
                print('\n--- ENCONTRAR POR NOME ---\n')
                nome_filtrar = str(input('Nome:')).title()
                clientes_encontrados = session.query(Cliente).filter(Cliente.nome.like(f'%{nome_filtrar}%')).all()

                if len(clientes_encontrados) == 0:
                    print('Nenhum cliente com esse nome foi encontrado!\n')
                    return
                else:
                    print(f'\n {len(clientes_encontrados)} cliente(s) encontrado(s) com este nome\n')

                    for cliente in clientes_encontrados:
                        print(f'Nome: {cliente.nome}')
                        print(f'Idade: {cliente.idade}')
                        print(f'CPF: {cliente.cpf}\n')
                        sleep(0.3)

            case 2:
                print('\n--- ENCONTRAR POR CPF ---\n')
                cpf_filtrar = str(input('CPF:'))
                cliente_encontrados = session.query(Cliente).filter_by(cpf=cpf_filtrar).all()
                if len(cliente_encontrados) != 0:
                    cliente = cliente_encontrados[0]
                    print('\n- Vendedor encontrado\n')
                    print(f'Nome: {cliente.nome}')
                    print(f'Idade {cliente.idade}')
                    print(f'CPF {cliente.cpf}\n')
                    sleep(0.3)

                else:
                    print('\nVendedor não encontrado!\n')
            
    def atualizar_salario(self):
        print('\n--- ATUALIZAR SALARIO DO VENDEDOR ---\n')
        cpf_filtrar = str(input('CPF:'))
        vendedores_encontrados = session.query(Vendedor).filter_by(cpf=cpf_filtrar).all()
        if len(vendedores_encontrados) != 0:
            vendedor = vendedores_encontrados[0]
            while True:
                try:
                    novo_salario = float(input(f"novo salario do {vendedor.nome}: "))
                    break
                except ValueError:
                    print("Salário inválido. Digite novamente")
            
            session.query(Vendedor).filter_by(cpf=cpf_filtrar).update({"salario": novo_salario})
            session.commit()
            print("\nAtualização realizada com sucesso\n")
            
        else:
            print('\nVendedor não encontrado!\n')

