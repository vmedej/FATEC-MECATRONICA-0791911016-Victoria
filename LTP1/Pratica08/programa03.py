def mostrarUsuario(nome, cpf, idade):
    print("\nDados do usuário:")
    print("Nome:", nome)
    print("CPF:", cpf)
    print("Idade:", idade)
    
def lerNovoUsuario():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    idade = input("Idade: ")
    return nome, cpf, idade
    
n,c,i = lerNovoUsuario()
mostrarUsuario(n,c,i)
