###############################################################################
from model import Pedido
from view import View
###############################################################################


class Controle:
    def inicio(self):
        escolhido = View.inicio()
        while escolhido != 5:
            # Inserir pedido
            if escolhido == 1:
                valores = View.coletaDadosPedido()
                dados = Pedido.criaPedido(valores)
                status = Pedido.cadastraPedido(dados)
                ###
                View.imprimeStatus(status)
                escolhido = View.inicio()
            # Remover pedido
            elif escolhido == 2:
                orderid = View.coletaId()
                status = Pedido.deletaPedido(orderid)
                ###
                View.imprimeStatus(status)
                escolhido = View.inicio()
            # Buscar pedido
            elif escolhido == 3:
                orderid = View.coletaId()
                registro = Pedido.consultaPedido(orderid)
                ###
                View.imprimePedido(registro)
                escolhido = View.inicio()
            # Alterar pedido
            elif escolhido == 4:
                valores = View.coletaDadoAtualizar()
                status = Pedido.atualizaPedido(valores)
                ###
                View.imprimeStatus(status)
                escolhido = View.inicio()
                controller = Controle()
                controller.inicio()
###############################################################################
