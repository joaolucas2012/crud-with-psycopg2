###############################################################################
from model import Pedido
from view import view
###############################################################################


class Controle:
    def inicio(self):
        escolhido = view.inicio()
        while escolhido != 5:
            # Inserir pedido
            if escolhido == 1:
                valores = view.coletaDadosPedido()
                dados = Pedido.criaPedido(valores)
                status = Pedido.cadastraPedido(dados)
                ###
                view.imprimeStatus(status)
                escolhido = view.inicio()
            # Remover pedido
            elif escolhido == 2:
                orderid = view.coletaId()
                status = Pedido.deletaPedido(orderid)
                ###
                view.imprimeStatus(status)
                escolhido = view.inicio()
            # Buscar pedido
            elif escolhido == 3:
                orderid = view.coletaId()
                registro = Pedido.consultaPedido(orderid)
                ###
                view.imprimePedido(registro)
                escolhido = view.inicio()
            # Alterar pedido
            elif escolhido == 4:
                valores = view.coletaDadoAtualizar()
                status = Pedido.atualizaPedido(valores)
                ###
                view.imprimeStatus(status)
                escolhido = view.inicio()


controller = Controle()
controller.inicio()
###############################################################################
