from modelos.restaurante import Restaurante
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


# Bebidas
bebidas  = [
    Bebida('Coca-Cola 350 ML', 8.0, 'p'),
    Bebida('Coca-Cola 600 ML', 10.0, 'm'),
    Bebida('Coca-Cola 2 LT', 15.0, 'g')
]

# Pratos
pratos  = [
    Prato('Macarrão a bolonhesa', 36.50, 'um prato italiano com macarrão, molho de tomate e carne moida'),
    Prato('Feijoada', 40.0, 'um tipico prato Brasileiro, com feijão e partes de porco'),
    Prato('Sorvete de pitaia', 15.0, 'um sorvete perfeito para refrescar o calor do nosso estado.')
]

# Restaurante Praça 
restaurante_praca = Restaurante('Praça', 'Gourmet')
# Ativa o restaurante
restaurante_praca.alternar_status()
#Insere avaliaçoes
restaurante_praca.receber_avalidacao('Wendel', 4.5)
restaurante_praca.receber_avalidacao('Thaina', 3)

#insere os pratos no cardapio
for prato in pratos:
    restaurante_praca.adicionar_no_cardapio(prato)
#insere as bebidas no cardapio
for bebida in bebidas:
    #aplicando desconto nas bebidas
    bebida.aplicar_desconto()
    restaurante_praca.adicionar_no_cardapio(bebida)


# Restaurante PIZZA
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')
restaurante_pizza.receber_avalidacao('Wendel', 5)

# Restaurante japa 
restaurante_japa = Restaurante('Hiro Sushi', 'Japonesa')
restaurante_japa.alternar_status()

def main():
    Restaurante.listar_restaurantes()
    print('\n')
    restaurante_praca.exibir_cardapio()

if __name__ == '__main__':
    main()
