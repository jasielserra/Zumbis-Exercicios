'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as
informações.
'''
while True:
    print('Senha deve ser diferente do Usuário')
    usuario = input('Login: ')
    senha = input('Senha: ')
    
    if senha != usuario:
        break
