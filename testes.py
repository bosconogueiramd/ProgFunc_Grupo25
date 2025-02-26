import unittest
from main import adicionar_usuario, listar_usuarios, filtrar_maiores, calcular_media_idades, gerar_mensagem_personalizada, limpar_usuarios

class TesteSistema(unittest.TestCase):

    def setUp(self):
        """Executado antes de cada teste para garantir que a lista de usuários esteja vazia."""
        limpar_usuarios()

    def test_adicionar_usuario(self):
        """Testa a adição de um novo usuário."""
        adicionar_usuario("Carlos", 30)
        self.assertEqual(len(listar_usuarios()), 1)
        self.assertEqual(listar_usuarios()[0]["nome"], "Carlos")

    def test_listar_usuarios(self):
        """Testa se a listagem retorna uma lista."""
        adicionar_usuario("Ana", 22)
        adicionar_usuario("Bruno", 25)
        lista = listar_usuarios()
        self.assertIsInstance(lista, list)
        self.assertEqual(len(lista), 2)

    def test_filtrar_maiores(self):
        """Testa se apenas maiores de idade são retornados."""
        adicionar_usuario("Ana", 17)
        adicionar_usuario("Marcos", 20)
        adicionar_usuario("João", 25)
        maiores = filtrar_maiores()
        self.assertEqual(len(maiores), 2)
        self.assertTrue(all(user["idade"] >= 18 for user in maiores))

    def test_calcular_media_idades(self):
        """Testa o cálculo da média das idades."""
        adicionar_usuario("Eduardo", 30)
        adicionar_usuario("Fernanda", 20)
        media = calcular_media_idades()
        self.assertEqual(media, 25)

    def test_gerar_mensagem_personalizada(self):
        """Testa a geração de mensagem personalizada."""
        msg_func = gerar_mensagem_personalizada("Oi")
        self.assertEqual(msg_func("Carlos"), "Oi, Carlos!")

if __name__ == '__main__':
    unittest.main()
