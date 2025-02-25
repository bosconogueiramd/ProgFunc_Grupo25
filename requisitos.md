# Requisitos do Sistema

## Requisitos Funcionais
1. O sistema deverá permitir a adição de usuários. *(Função: adicionar_usuario)*
2. O sistema deverá listar os usuários cadastrados. *(Função: listar_usuarios)*
3. O sistema deverá filtrar usuários maiores de idade. *(Função: filtrar_maiores)*
4. O sistema deverá calcular a média de idades. *(Função: calcular_media_idades)*
5. O sistema deverá oferecer uma mensagem personalizada para cada usuário. *(Função: gerar_mensagem_personalizada)*

## Requisitos Não Funcionais
1. O sistema deverá ser implementado em Python.
2. O sistema deverá ser eficiente e utilizar recursos da programação funcional.
3. O sistema deverá ser testado com casos de teste. *(Arquivo: testes.py)*

## Conceitos de Programação Funcional Aplicados
- **Função Lambda**: Utilizada na função `calcular_media_idades`.
- **List Comprehension**: Utilizada na função `filtrar_maiores`.
- **Closure**: Implementada na função `gerar_mensagem_personalizada`.
- **Função de Alta Ordem**: Implementada na função `calcular_media_idades`.

## Casos de Teste
- Testar adição de usuário.
- Testar listagem de usuários.
- Testar filtragem de maiores de idade.
- Testar cálculo da média de idades.
- Testar geração de mensagem personalizada.
