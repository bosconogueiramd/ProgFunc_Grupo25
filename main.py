# Lista de usuários
usuarios = []

# Adicionar usuário
def adicionar_usuario(nome, idade):
    usuarios.append({"nome": nome, "idade": idade})

# Listar usuários
def listar_usuarios():
    return usuarios

# Filtrar maiores de idade (List Comprehension)
def filtrar_maiores():
    return [user for user in usuarios if user["idade"] >= 18]

# Função de alta ordem para calcular a média de idades
def calcular_media_idades():
    return (lambda lista: sum(lista) / len(lista) if lista else 0)([user["idade"] for user in usuarios])

# Closure para gerar mensagem personalizada
def gerar_mensagem_personalizada(saudacao):
    def mensagem(nome):
        return f"{saudacao}, {nome}!"
    return mensagem

# Testes
def testes():
    adicionar_usuario("João", 25)
    adicionar_usuario("Maria", 17)
    assert len(listar_usuarios()) == 2
    assert len(filtrar_maiores()) == 1
    assert calcular_media_idades() == 21
    msg_func = gerar_mensagem_personalizada("Olá")
    assert msg_func("João") == "Olá, João!"
    print("Todos os testes passaram!")

testes()
