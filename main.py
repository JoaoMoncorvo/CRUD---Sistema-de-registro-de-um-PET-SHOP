from modulos import (Cadastrar, Menu, AlterarDados, DeletarPet, ListarPets, ListarPorCriterio)  
from time import sleep      
print('BEM VINDO AO SISTEMA DO PETSHOP MONCORVO')
print('-='*10)
while True:
    menu = Menu()
    match menu:
        case 1:
            Cadastrar()
            continue
        case 2:
            AlterarDados()
            continue
        case 3:
            DeletarPet()
        case 4:
            ListarPets()
        case 5:
            ListarPorCriterio()
        case 6:
            print('OBRIGADO POR USAR NOSSO SISTEMAS, VOLTE SEMPRE!')
            sleep(0.5)
            break






