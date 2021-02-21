""" 
essa função utiliza a biblioteca string para gerar a lista de caracteres e 
conforme a documentação oficial do Python faz uso da biblioteca secrets para gerar
a partir da lista de strings, alatóriamente os caracters que compõe o password.
"""

import secrets
import string


class Password():
    # inicializador do objeto
    def __init__(self):
        self.password = ""

    def length(self):
        """recebe o comprimento do password
        """
        self.length = int(input("Quantos caracteres deve ter o password? "))
        return self.length

    def password_generator(self, length=6):
        """Gera um password genérico
        comprimento mínimo = 6 se nada for especificado
        retorna string
        """
        letters = string.ascii_letters
        numbers = string.digits
        specials = string.punctuation
        # a partir das listas anteriores gera uma lista alpha-numerica + pontuação
        out = f'{letters}{numbers}{specials}'
        out = list(out)

        # gerando um password randômico
        self.random_password = ''.join(secrets.choice(out)
                                       for i in range(self.length))
        return self.random_password

# teste do objeto Password
# p1 = Password()
# p1.length = int(input("Entre com o tamanho do password necessário: "))
# print(p1.password_generator())
