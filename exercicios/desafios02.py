class ContaBancaria:

    def __init__(self, titular, saldo, ativo = False):
        self.titular = titular
        self.saldo = saldo
        self._ativo = ativo

    def __str__(self):
        return f'{self.titular} | {self.saldo} | {self._ativo}'

    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True
        print(f'{conta.titular} | {conta.saldo} | {conta._ativo}')

conta1 = ContaBancaria('Polyana', 2000)

ContaBancaria.ativar_conta(conta1)

class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

conta2 = ContaBancariaPythonica('Matheus',3000)

print(conta2.saldo)







