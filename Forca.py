
from ForcaBanco import ForcaBanco
import random
import string  # função para adicinar ferramentas como do alfabeto


def Obter_Palavras_validas():
    # Randonly choeses somenthing from de list (escolher uma palavra aleatoria na lista)
    word = random.choice(ForcaBanco)
    while '-' in word or ' ' in word:  # is checking for spaces or - in the word
        word = random.choice(ForcaBanco)

    return word.upper()


def validar_letras():

    word = Obter_Palavras_validas()
    # Comando set() vai transformar a palvra em um dicionario separando as letas
    word_letras = set(word)
    alfabero = set(string.ascii_uppercase)
    usuario_letras = set()

    # aqui pra baixo sera o input do usuario
    while len(word_letras) > 0:  # Aqui ele vai ler sempre para fazer o usuario adicionar todas letras
        # letras usadas
        print("Vc usou as seguintes letras: ", ' '.join(usuario_letras))

        # mostrar as letras das palabras separadas por '-'

        lista_palavras = [
            letter if letter in usuario_letras else '-' for letter in word]
        print('A palavra é? ', ' '.join(lista_palavras))

        # imput para o usuario colocar a letra
        imput_usuario = input("Digite uma letra: ").upper()

        if imput_usuario in alfabero - usuario_letras:  # verifiacr se a letra est no alfabeto
            # adicionar a letra na lista de letras 'chutadas'
            usuario_letras.add(imput_usuario)

            if imput_usuario in word_letras:  # verifica se a letra esta na palavra
                # se sim, remobe a letra da palavra
                word_letras.remove(imput_usuario)

        elif imput_usuario in usuario_letras:
            print("Voce ja usou essa letra, tente novamente")
        else:
            print("Caractare invalodo, tente novamente")


validar_letras()
