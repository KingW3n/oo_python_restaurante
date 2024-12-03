from modelos.restaurante import Restaurante
  
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.alternar_status()
restaurante_praca.receber_avalidacao('Wendel', 4.5)
restaurante_praca.receber_avalidacao('Thaina', 3)

restaurante_pizza = Restaurante('Pizza Express', 'Italiana')
restaurante_pizza.receber_avalidacao('Wendel', 5)

restaurante_japa = Restaurante('Hiro Sushi', 'Japonesa')
restaurante_japa.alternar_status()



def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()
