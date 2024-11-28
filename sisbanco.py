class conta:

    def __init__(self, numero:str):
        self.__numero = numero
        self.__saldo = 0.0

    def creditar(self, valor:float) -> None:
        self.__saldo += valor
    def debitar(self, valor:float) -> None:
        self.__saldo -= valor   
    def get_numero(self) ->str:
        return self.__numero
    def get_saldo(self) ->str:
        return self.__saldo
class banco:
    
    def __init__(self):
        pass
    def cadastrar(self, conta:conta) -> str:
        pass
    def procura(self,  numero:str) -> conta:
        pass
    def creditar(self, valor: float) ->None:
        pass
    def debitar(self, valor: float) ->None:
        pass
    def saldo(self, numero: str)-> float:
        pass
    def transferir( self, origem:str, destino:str, valor:float)->None:
        pass



