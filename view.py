###############################################################################
from datetime import datetime
###############################################################################


class View():
    def inicio(self):
        return self.menu()
    ###############################################################################

    def menu(self):
        print('1 para inserir pedido')

        print('2 para remover pedido')

        print('3 para buscar pedido')

        print('4 para alterar pedido')

        print('5 para sair\n')
        escolhido = int(input('digite aqui: '))
        return escolhido
    ###############################################################################

    def coletaDadosPedido(self):
        # 1º atributo da tabela
        orderid = input('digite - identificador do pedido: ')
        # 2º atributo da tabela
        customerid = input('digite - cliente: ')
        # 3º atributo da tabela
        employeeid = input('digite - identificador do funcionario: ')
        # 4º atributo da tabela
        orderdate = input('digite - data do pedido ano-mes-dia: ')
        # 5º atributo da tabela
        requireddate = input(
            'digite - data de fechamento do pedido ano-mes-dia: ')
        # 6º atributo da tabela
        shippeddate = input('digite - data de envio do pedido ano-mes-dia: ')
        # 7º atributo da tabela
        freight = input('digite - valor do frete: ')
        # 8º atributo da tabela
        shipname = input('digite - localização para envio: ')
        # 9º atributo da tabela
        shipaddress = input('digite - endereço: ')
        # 10º atributo da tabela
        shipcity = input('digite - cidade para envio: ')
        # 11º atributo da tabela
        shipregion = input('digite - regiao para envio: ')
        # 12º atributo da tabela
        shippostalcode = input('digite - CEP: ')
        # 13º atributo da tabela
        shipcountry = input('digite - pais: ')
        # 14º atributo da tabela
        shipperid = input('digite - id do endereço para envio: ')
        # De acordo com o que ela fez no vídeo
        ano, mes, dia = map(int, orderdate.split('-'))
        orderdate = datetime(ano, mes, dia)
        ano, mes, dia = map(int, requireddate.split('-'))
        requireddate = datetime(ano, mes, dia)
        ano, mes, dia = map(int, shippeddate.split('-'))
        shippeddate = datetime(ano, mes, dia)
        valores = [orderid, customerid, employeeid, orderdate, requireddate, shippeddate, freight,
                   shipname, shipaddress, shipcity, shipregion, shippostalcode, shipcountry, shipperid]
        return valores
    ###############################################################################

    def coletaId(self):
        orderid = input('digite o id do pedido: ')
        return orderid
    ###############################################################################

    def coletaDadoAtualizar(self):
        orderid = input('digite o id do pedido: ')
        campo = input('digite o campo que deseja atualizar: ')
        valoratualizado = input('digite o novo valor: ')

        valores = [orderid, campo, valoratualizado]
        return valores
    ###############################################################################

    def imprimePedido(self, pedido):
        if pedido is not None:
            print(f'id: {pedido.pedido}')
            ###
            print(f'cliente: {pedido.cliente}')
            ###
            print(f'funcionario: {pedido.empregadoId}')
            ###
            print(f'data do pedido: {pedido.data}')
            ###
            print(f'data para fechamento do pedido: {pedido.requisicao}')
            ###
            print(f'data para envio do pedido: {pedido.dataEnvio}')
            ###
            print(f'valor do frete: {pedido.frete}')
            ###
            print(f'local para envio: {pedido.remetente}')
            ###
            print(f'endereco: {pedido.endereco}')
            ###
            print(f'cidade: {pedido.cidade}')
            ###
            print(f'regiao: {pedido.regiao}')
            ###
            print(f'cep: {pedido.postal}')
            ###
            print(f'pais: {pedido.pais}')
            ###
            print(f'id do endereço para envio: {pedido.remetenteId}')
        else:
            print('algo deu errado ou id do pedido não confere com algum cadastrado\n')
    ###############################################################################

        def imprimeStatus(self, status):
            if status is not None:
                print(status)
            else:
                print('algo deu errado')
                view = View()
###############################################################################
