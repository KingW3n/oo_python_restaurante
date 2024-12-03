from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    '''
        A classe trata de um cadastro de restaurante. 
        Para instancia é necessairo informar nome e categoria, todos os restaurantes são cadastrados inicialmente como false 
    '''

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._status = False
        self._avaliacao = []
        self._cardapio = []
        
        self.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}' 
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.status}')

    @property
    def status(self):
        return '✅' if self._status else '❌'
    
    def alternar_status(self):
        self._status = not self._status 

    def receber_avalidacao(self, cliente, nota):
        if 0<= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
            
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas  = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media  = soma_das_notas / quantidade_de_notas
        return "{:.2f}".format(media)
    
    def adicionar_no_cardapio(self, item):
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)

    def exibir_cardapio(self):
        print(f'Cardapio do restaruante {self._nome} \n')
        for i,item in enumerate(self._cardapio, start=1):
            if hasattr(item, '_descricao'):
                print(f'{i}. Nome: {item._nome.ljust(20)} | Preço: R$ {str(item._preco).ljust(20)} | {item._descricao}')
            else:
                print(f'{i}. Nome: {item._nome.ljust(20)} | Preço: R$ {str(item._preco).ljust(20)} | {item._tamanho}')