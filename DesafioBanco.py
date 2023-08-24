def menu():
    menu = '''\n\n\n
   ================ MENU ================
    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q]  Sair
    => '''
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Deposito: {valor:.2f}'
        print('Deposito realizado com sucesso')
    else: 
        print('Deposito falhou')
    
    return saldo, extrato

def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    #excedeu_saque = numero_saques >= limite_saques
    excedeu_limite = valor > limite

    if excedeu_saldo:
        print('Operação falhou! Você está sem saldo suficiente.')
    elif numero_saques >= limite_saques:
        print('Operação falhou! Você excedeu o número de saques.')
    elif excedeu_limite:
        print('Operação falhou! O valor do saque excede o limite.')
    elif valor > 0:
        saldo -= valor
        extrato += f'\nSaque: {valor:.2f}'
        numero_saques += 1
        print('Saque realizado com sucesso')
    else:
        print('Saque falhou')
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *,extrato):
    print('\n================ Extrato ================')
    print('\nNão foram realizadas movimentações' if not extrato else extrato)
    print(f'\nSaldo: R${saldo:.2f}')
    print('\n=========================================')
    
def criar_usuario(usuarios):
    cpf = input('Digite seu cpf (apenas números): ')
    usuario = user_filtrado(cpf, usuarios)
    
    if usuario:
        print('Cpf já cadastrado')
        return
    
    nome = input('Digite seu nome completo: ')
    data_nasc = input('Digite sua data de nascimento: ')
    endereco = input('Digite seu endereço: ')

    usuarios.append({'cpf': cpf, 'nome': nome, 'data de nascimento': data_nasc, 'endereço': endereco})

    print('usuario criado')

def user_filtrado(cpf, usuarios):
    user_filter = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return user_filter[0] if user_filter else None

def criar_conta(agencia,n_conta, usuarios):

    cpf = input('Informe seu CPF: ')
    usuario = user_filtrado(cpf, usuarios)

    if usuario:
        print('Conta criada')
        return {'agencia': agencia, 'numero de conta': n_conta, 'usuario': usuario}
    
    print('Usuario não encontrado')

def listar_contas(contas):
    for conta in contas:
        linha = f'''
        Agencia: {conta['agencia']}
        C_C: {conta['n_conta']}
        Titular: {conta['usuario']['conta']}
        '''
        print(linha)


def main():
    LIMITE_SAQUE = 3
    AGENCIA = '0001'
    LIMITE = 500

    saldo = 0
    extrato = ''
    numero_saques = 0
    contas = []
    usuario = []
    numero_contas = 0

    while True:
        opcao = menu() 
        
        if opcao == 'd':
           valor = float(input('Digite o valor a ser depositado: R$ '))

           saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == 's':
           valor = float(input('Digite o valor a ser sacado: R$ '))
           
           saldo, extrato = sacar(
               saldo=saldo,
               valor=valor,
               extrato=extrato,
               limite=LIMITE,
               numero_saques=numero_saques,
               limite_saques=LIMITE_SAQUE
           )
        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == 'nu':
            criar_usuario(usuario)
        
        elif opcao == 'nc':
            numero_contas = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_contas, usuario)

            if conta:
                contas.append(conta)

        elif opcao == 'lc':
            listar_contas(contas)
        
        elif opcao == 'q':
            break

main()