from Ferramenta import Ferramenta

class Furadeira(Ferramenta):
    def __init__(self,nome,tensao,preco,potencia):
        self._nome = nome
        self._tensao = tensao
        self._preco = preco
        self._potencia = potencia

    @property
    def nome(self):
        return self._nome 
    
    @nome.setter
    def nome(self,valor):
        self._nome = valor


    @property
    def tensao(self):
        return self._tensao

    @tensao.setter
    def tensao(self,valor):
        self._tensao = valor

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self,valor):
        self._preco = valor
    

    @property
    def potencia(self):
        return self._potencia

    @potencia.setter
    def potencia(self,valor):
        self._potencia = valor
    


    def getImprimir(self):
        print("--Furadeira--")
        print("nome:",self._nome)
        print("tensao:",self._tensao)
        print("preco:",self._preco)
        print("potencia:",self._potencia)

    def cadastrar(self):
        print("--------------------")
        print("nome:",self._nome)
        print("tensao:",self._tensao)
        print("preco:",self._preco)
        print("potencia:",self._potencia)
        print("Furadeira cadastrada com sucesso!")

    