from abc import ABCMeta,abstractmethod
#O sistema possuirá uma classe abstrata chamada de Ferramenta que deve conteros atributos/propriedades nome, tensão e preço. 
# Esta classe também deve possuir um método getInformacoes() que retorna todos os valores dos atributos. Esta classe também possui um método abstrato cadastrar().


class Ferramenta(metaclass=ABCMeta):
    @property
    def nome(self):
        pass

    @nome.setter
    def nome (self,valor):
        pass

    @property
    def tensao(self):
        pass

    @tensao.setter
    def tesao (self,valor):
        pass

    @property
    def preco(self):
        pass

    @preco.setter
    def preco (self,valor):
        pass

    def getImprimir(self):
        print("nome:",self.nome)
        print("tensao:",self.tensao)
        print("preco:",self.preco)

    
    @abstractmethod
    def cadastrar(self):
        pass



