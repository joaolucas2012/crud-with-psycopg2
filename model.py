###############################################################################
from decimal import *
import psycopg2
from psycopg2.extensions import AsIs
###############################################################################
from config import config
from datetime import datetime
###############################################################################
# Tratamento para o caso de uma consultar retornar a colunar shiperid como NULL


def shiperidTratamento(valores):
    if valores[13] == None:
        return -1
    else:
        return valores[13]
###############################################################################


class funcionarioNaoEncontrado(Exception):
    pass


class clienteNaoEncontrado(Exception):
    pass
###############################################################################


class Pedido():
    def __init__(self, orderid, customerid, employeeid, orderdate, requireddate, shippeddate, freight, shipname, shipadress, shipcity, shipregion, shippostalcode, shipcountry, shipperid):
        ###
        self.pedido = orderid
        ###
        self.cliente = customerid
        ###
        self.empregadoId = employeeid
        ###
        self.data = orderdate
        ###
        self.requisicao = requireddate
        ###
        self.dataEnvio = shippeddate
        ###
        self.frete = freight
        ###
        self.remetente = shipname
        ###
        self.endereco = shipadress
        ###
        self.cidade = shipcity
        ###
        self.regiao = shipregion
        ###
        self.postal = shippostalcode
        ###
        self.pais = shipcountry
        ###
        self.remetenteId = shipperid
    ###############################################################################

    def criaPedido(valores):
        return Pedido(int(valores[0]), str(valores[1]), int(valores[2]), valores[3], valores[4], valores[5], Decimal(valores[6]), str(valores[7]), str(valores[8]), str(valores[9]), str(valores[10]), str(valores[11]), str(valores[12]), int(shiperidTratamento(valores)))
    ###############################################################################

    def cadastraPedido(pedido):
        stringSQL = string_SQL_pedido = 'INSERT INTO northwind.orders(orderid, customerid, employeeid, orderdate, requireddate, shippeddate, freight, shipname, shipaddress, shipcity, shipregion, shippostalcode, shipcountry, shipperid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        registros = (pedido.pedido, pedido.cliente, pedido.empregadoId, pedido.data, pedido.requisicao, pedido.dataEnvio, pedido.frete,
                     pedido.remetente, pedido.endereco, pedido.cidade, pedido.regiao, pedido.postal, pedido.pais, pedido.remetenteId)
        try:
            if Costumers.consultaCostumers(pedido.cliente):
                raise clienteNaoEncontrado()
            elif Employees.consultaEmployees(pedido.empregadoId):
                raise funcionarioNaoEncontrado()
        except clienteNaoEncontrado:
            return('cliente nao encontrado')
        except funcionarioNaoEncontrado:
            return('funcionario nao encontrado')
        else:
            status = config.alteraBD(config, stringSQL, registros)
            return status
    ###############################################################################

    def deletaPedido(id):
        oders_details.deletarorders_details(id)
        stringSQL = 'DELETE FROM northwind.orders WHERE orderid = %s;'
        status = config.alteraBD(config, stringSQL, [id])
        return status
    ###############################################################################

    def consultaPedido(id):
        stringSQL = 'SELECT * FROM northwind.orders WHERE orderid = %s;'
        registro = config.consultaBD(config, stringSQL, [id])
        if(len(registro[1]) != 0):
            pedido = Pedido.criaPedido(registro[1][0])
            return pedido
        else:
            return None
    ###############################################################################

    def atualizaPedido(l):
        stringSQL = 'UPDATE northwind.orders SET %s = %s WHERE orderid = %s'
        parametros = ((AsIs(l[1])), str(l[2]), int(l[0]))
        if l[1] == 'employeeid' or l[1] == 'customerid':
            try:
                if l[1] == 'customerid':
                    if Costumers.consultaCostumers(l[2]):
                        raise clienteNaoEncontrado()
                else:
                    if Employees.consultaEmployees(l[2]):
                        raise funcionarioNaoEncontrado()
            except clienteNaoEncontrado:
                return('cliente nao encontrado')
            except funcionarioNaoEncontrado:
                return('funcionario nao encontrado')
            else:
                status = config.alteraBD(config, stringSQL, parametros)
                return status
        else:
            status = config.alteraBD(config, stringSQL, parametros)
            return status
###############################################################################


class Costumers():
    def consultaCostumers(id):
        stringSQL = 'SELECT * FROM northwind.customers WHERE customerid = %s;'
        registro = config.consultaBD(config, stringSQL, [id])
        if(len(registro[1]) != 0):
            return False
        else:
            return True
###############################################################################


class Employees():
    def consultaEmployees(id):
        stringSQL = 'SELECT * FROM northwind.employees WHERE employeeid = %s;'
        registro = config.consultaBD(config, stringSQL, [id])
        if(len(registro[1]) != 0):
            return False
        else:
            return True
###############################################################################


class oders_details():
    def deletarorders_details(id):
        stringSQL = 'DELETE FROM northwind.order_details WHERE orderid = %s;'
        status = config.alteraBD(config, stringSQL, [id])
###############################################################################
