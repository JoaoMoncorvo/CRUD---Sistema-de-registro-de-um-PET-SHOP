from time import sleep
import json

def Cadastrar():
    while True:
        nome = str(input('me diga o nome e sobrenome do pet: '))
        tipo = str(input('qual tipo do pet? [cachorro/gato]')).lower()
        endereco = str(input('qual endereco o pet mora: ')).lower()
        idade = float(input('qual idade aproximada do pet(em anos): '))
        peso = float(input('qual o peso aproximado do pet? (em kg)'))
        raca = str(input('qual a raca do pet? ')).lower()
        animal = {
            'nome': nome,
            'tipo': tipo,
            'endereco': endereco,
            'idade': idade,
            'peso': peso,
            'raca': raca,
        }
        with open('db.json', 'r', encoding='utf-8') as formulario:
            pets = json.load(formulario)
        pets.append(animal)
        with open('db.json', 'w', encoding='utf-8') as db:
            json.dump(pets, db, indent=4)
        escolhaFinal = int(input('voce deseja: Regitrar mais um pet[1] ou Voltar ao menu [2]: '))
        if escolhaFinal == 1:
            continue
        elif escolhaFinal == 2:
            break
def Menu():
    while True:
        print('1. Cadastrar um novo pet')
        print('2. Alterar os dados do pet cadastrado')
        print('3. Deletar um pet cadastrado ')
        print('4. listar todos os pets cadastrados ')
        print('5. Listar pets por algum criterio (idade, nome, raca)')
        print('6. Sair')
        escolha = int(input('digite sua opcao: '))
        if escolha >= 1 and escolha <= 6:
            return escolha
            break
        else:
            print('Opcao invalida! lista de opcoes: 1, 2, 3, 4, 5 e 6')
            sleep(2)
            continue
def AlterarDados():
    while True:
        while True:
            escolha = str(input('me diga o nome do PET que voce quer alterar os dados: '))
            lista = []
            with open('db.json', 'r', encoding='utf-8') as arquivo:
                db = json.load(arquivo)
                for pet in db:
                    if escolha == pet['nome']:
                        petAchado = {
                            **pet
                        }
                        lista.append(petAchado)
                for i, pet in enumerate(lista):
                    print(f'{i + 1} - {pet}')
                escolhaFinal = int(input(f'me diga, qual o indice do pet nomeado {escolha} voce quer alterar os dados: '))      #numero
                if 1<=escolhaFinal<=len(lista):
                    escolhaDado = str(input(f'me diga qual dado voce quer alterar do pet {escolha}: ')).lower()         # tipo
                    escolhaDadoSwitch = input(f'quer substituir o {escolhaDado} por qual? ').lower()  #troca
                    break
                else:
                    print('numero invalido, tende novamente: ')
                    continue

        for pet in db:
            if pet == lista[escolhaFinal - 1]:
                pet[f'{escolhaDado}'] = escolhaDadoSwitch.lower()
                print(f'troca feita com sucesso, agora o registro ficou assim: {pet}')
            
        with open('db.json', 'w', encoding='utf-8') as arquivo2:
            json.dump(db, arquivo2, indent=4)         
        
        perguntaFinal = int(input('Quer alterar mais um dado[1] ou voltar ao menu inicial[2] (digite apenas [1/2])? '))
        if perguntaFinal == 1:
            continue
        elif perguntaFinal == 2:
            break
def DeletarPet():
        continuar = True
        achou = False
        while continuar:
            petPergunta = str(input('diga o nome do pet completo do pet que voce quer excluir do sistema: '))
            with open('db.json', 'r', encoding='utf-8') as dados:
                pets = json.load(dados)
            for pet in pets:
                if pet['nome'] == petPergunta:
                    achou = True
                    break
            if achou == False:
                escolha = int(input(f'o pet {petPergunta} nao foi encontrado no sistema, deseja pesquisar outro ou voltar ao menu? [1/2]'))
                if escolha == 1:
                        continue
                else:
                    print('voltando ao menu inicial...')
                    continuar = False
                    break
            if achou:
                escolhaFinal = str(input(f'tem certeza que deseja excluir o pet {petPergunta} do sistema?[S/N]'))
                if escolhaFinal == 'S':
                    with open('db.json', 'r') as exclusao:
                        pets = json.load(exclusao)
                        for pet in pets:
                            if pet['nome'].lower() == petPergunta.lower():
                                with open('db.json', 'w', encoding='utf-8') as arquivosaida:
                                    pets.remove(pet)
                                    json.dump(pets, arquivosaida, indent=4)
                    print(f'o pet {petPergunta} foi excluido com sucesso.')
                    continuar = False
                    break
                else:
                    print('saindo da tela de exclusao, voltando ao menu inicial...')
                    continuar = False
                    break 
def ListarPets(): 
    while True:
        with open('db.json', 'r', encoding='utf-8') as arquivo:
            db = json.load(arquivo)
            print('SEGUE ABAIXO, A LISTA DE TODOS OS PETS REGISTRADOS:\n')
            for pet in db:
                print(f'{pet['nome']}, {pet['tipo']} da raca {pet['raca']}')
            pergunta = int(input('quer repetir ou voltar a tela inicial?? [1/2]'))
            if pergunta == 1:
                continue
            elif pergunta == 2:
                break
def ListarPorCriterio(): 
    encontrou = False
    while True:
        while True:
            filtro = str(input('me diga o criterio que voce quer filtrar: [nome/endereco/idade/peso/raca/tipo] ')).lower()
            filtro2 = str(input(f'agora me diga, pets com qual {filtro} voce quer listar? [escreva exatamente]'))
            with open('db.json', 'r', encoding='utf-8') as arquivo:                                                                                                   
                listagem = json.load(arquivo)
                for pet in listagem:
                    if pet[f'{filtro}'] == filtro2:
                        print(pet)
                        encontrou = True
                if encontrou:
                    break
                else:
                    print('pets nao encontrados, tente novamente. ')
                    encontrou = False
                    continue
        escolha = int(input('quer filtrar mais alguma coisa[1] ou quer voltar ao Menu principal[2]? [1/2]'))
        if escolha == 1:
            continue
        elif escolha == 2:
            break