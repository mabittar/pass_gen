# GUI Password-Generator - 

Python 3, Tkinter, slide bar and copy button without Pyperclip library.

US:

A password generator using Python 3 and the tkinter library.


From the scale bar, set the desired password length and use the copy button to transfer the generated password to the target application.

## Requirements

The installed dependencies listed in `requirements.txt` were used only to facilitate the development of the application. I have insisted on leaving them exposed to allow the exact reproduction of this repository as a form of study.

Python 3 already has the `tkinter` and `secrets` modules and no additional module is needed to make `app.py` work correctly.

## Characters for Password Generation

The word list is generated from concatenating strings, generated from the `string` library using uppercase and lowercase characters, special symbols and punctuation.

The random way the characters are selected uses the `secrets` library. From the official documentation:


*"The secrets module is used for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.
In particular, secrets should be used in preference to the default pseudo-random number generator in the random module, which is designed for modelling and simulation, not security or cryptography. "*

## Visual Elements

The color composition of the visual elements was also observed in order to favor user usability.

## Usage

## Clone with HTTPs:

    git clone https://github.com/mabittar/pass_gen.git

### Clone with GIT CLI:

    gh repo clone mabittar/pass_gen

Download or clone the repository using the above commands

### Running the application

 1. Run the `app.py` application with, from the installed folder:

        python app.py


 2. In the slider bar enter the length of the password you need.

 3. Click the Generate Password button

 4. Click the copy password button to copy the generated password to the clipboard.

 5. Copy the generated password into the desired application.


The `password.py` file is the implementation of the object that will generate the password.

PT-Br:

Um gerador de password usando Python 3 e a biblioteca tkinter.


A partir da barra de escala, ajuste o comprimento do password desejado e utilize o botão copiar para transferir o password gerado para a aplicação de destino.

## Requirements

As dependências instaladas relacionadas em `requirements.txt` foram utilizadas apenas para facilitar o desenvolvimento do aplicativo. Fiz questão de deixar exposto para possibilitar a exata reprodução desse repositório como uma forma de estudo.

O Python 3 já possui os módulos `tkinter` e `secrets` não sendo necessário nenhum outro módulo adicional para que o aplicativo `app.py` funcione corretamente.

## Caracteres para geração do Password

A lista de palavras é gerada a partir da concatenação de strings, gerados a partir da biblioteca `string` utilizando caracteres maiúsculas e minúsculas, símbolos especiais e pontuação.

A forma randômica como os caracteres são selecionados utiliza a biblioteca `secrets`. Da documentação oficial:


*"O módulo `secrets` é usado para gerar números criptográficos aleatórios fortes adequados para gerenciar dados como senhas, autenticação de contas, tokens de segurança e segredos relacionados.
Em particular, `secrets` deve ser usado em preferência ao gerador de números pseudo-aleatórios padrão no módulo `random`, que é projetado para modelagem e simulação, e não para segurança ou criptografia."*

## Elementos Visuais

Foi observado também a composição de cores dos elementos visuais a fim de favorecer a utilização do usuário.

## Utilização

### Clone com HTTPs:

    git clone https://github.com/mabittar/pass_gen.git

### Clone com GIT CLI:

    gh repo clone mabittar/pass_gen

Faça o download ou clone o repositório utilizando os comandos acima

### Rodando o aplicativo

 1. Rode o aplicativo `app.py` com, a partir da pasta instalada:

        python app.py


 2. Na barra slider informe o comprimento do password necessário.

 3. Clique no botão Gerar Password

 4. Clique no botão copiar password para copiar o password gerado para a área de transferência.

 5. Copie o password gerado na aplicação desejada.


O arquivo `password.py` é a implementação do objeto que irá gerar o password.