from modulos import (Cadastrar, Menu, AlterarDados, DeletarPet, ListarPets, ListarPorCriterio)        
print('BEM VINDO AO SISTEMA DO PETSHOP MONCORVO')
print('-='*10)
while True:
    menu = Menu()
    if menu== 1:
        Cadastrar()
        continue
    elif menu == 2:
        AlterarDados()w
        continue
    elif menu == 3:
        DeletarPet()
        continue
    elif menu == 4:
        ListarPets()
        continue
    elif menu == 5:
        ListarPorCriterio()
        continue
    elif menu == 6:
        print('OBRIGADO POR USAR NOSSO SISTEMAS, VOLTE SEMPRE!')
        sleep(0.)
        break






