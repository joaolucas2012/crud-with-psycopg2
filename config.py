###############################################################################
import psycopg2
###############################################################################
# De acordo com o que ela fez no vídeo


class config():
    def __init__(self, dadosconexao):
        self.dadosconexao = dadosconexao
    ###############################################################################

    def setParametros(self):
        self.dadosconexao = "host='localhost' dbname='Northwind' user='postgres' password='frankenstrike1212'"
        return self
    ###############################################################################

    def alteraBD(self, stringSQL, valores):
        conn = None
        try:
            conexao = psycopg2.connect(config.setParametros(self).dadosconexao)
            sessao = conexao.cursor()
            sessao.execute(stringSQL, valores)
            conexao.commit()
            sessao.close()
        except psycopg2.Error:
            return psycopg2.Error
        finally:
            if conn is not None:
                conn.close()
            return 'transição bem-sucedida'
    ###############################################################################

    def consultaBD(self, stringSQL, valores):
        conn = None
        try:
            conexao = psycopg2.connect(config.setParametros(self).dadosconexao)
            sessao = conexao.cursor()
            sessao.execute(stringSQL, valores)
            registros = sessao.fetchall()
            colnames = [desc[0] for desc in sessao.description]
            conexao.commit()
            sessao.close()
        except psycopg2.Error:
            return psycopg2.Error
        else:
            if conn is not None:
                conn.close()
            return(colnames, registros)
###############################################################################
