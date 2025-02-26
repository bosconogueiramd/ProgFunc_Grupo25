from functools import reduce

# Função Pura: Adicionar usuário sem modificar lista original
def adicionar_usuario(usuarios, nome, idade):
    return usuarios + [{"nome": nome, "idade": idade}]

# Função Pura: Retorna uma cópia da lista de usuários
def listar_usuarios(usuarios):
    return usuarios.copy()

# List Comprehension: Filtra maiores de idade
def filtrar_maiores(usuarios):
    return [user for user in usuarios if user["idade"] >= 18]

# Função de Alta Ordem: Calcula média de idades com reduce
def calcular_media_idades(usuarios):
    idades = list(map(lambda user: user["idade"], usuarios))
    return reduce(lambda acc, idade: acc + idade, idades, 0) / len(idades) if idades else 0

# Closure: Gera função personalizada para mensagens
def gerar_mensagem_personalizada(saudacao):
    return lambda nome: f"{saudacao}, {nome}!"

# Função Pura: Reseta a lista sem mutá-la
def limpar_usuarios():
    return []

# Menu funcional usando dicionário de funções
def menu():
    usuarios = []
    
    opcoes = {
        "1": lambda usuarios: adicionar_usuario(usuarios, input("Nome: "), int(input("Idade: "))),
        "2": lambda usuarios: print("\n".join([f"- {user['nome']} ({user['idade']} anos)" for user in listar_usuarios(usuarios)])) or usuarios,
        "3": lambda usuarios: print("\n".join([f"- {user['nome']} ({user['idade']} anos)" for user in filtrar_maiores(usuarios)])) or usuarios,
        "4": lambda usuarios: print(f"Média de idades: {calcular_media_idades(usuarios):.2f}") or usuarios,
        "5": lambda usuarios: print(gerar_mensagem_personalizada(input("Saudação: "))(input("Nome: "))) or usuarios,
        "6": lambda usuarios: exit("Saindo..."),
    }
    
    while True:
        print("\n📌 MENU DO SISTEMA DE GESTÃO DE USUÁRIOS")
        print("1 - Adicionar usuário")
        print("2 - Listar usuários")
        print("3 - Filtrar maiores de idade")
        print("4 - Calcular média de idades")
        print("5 - Gerar mensagem personalizada")
        print("6 - Sair")
        
        opcao = input("Escolha uma opção: ")
        usuarios = opcoes.get(opcao, lambda usuarios: print("Opção inválida!") or usuarios)(usuarios)

# Executa o menu
if __name__ == "__main__":
    menu()
