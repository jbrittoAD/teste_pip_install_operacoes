class Operacoes:
    def __init__(self, valor_inicial=0):
        self.valor = valor_inicial

    def set_valor(self, novo_valor):
        self.valor = novo_valor

    def soma(self, valor):
        return self.valor + valor

    def subtracao(self, valor):
        return self.valor - valor
