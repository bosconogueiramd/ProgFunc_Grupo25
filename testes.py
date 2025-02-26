import unittest
from main import adicionar_usuario, listar_usuarios, filtrar_maiores, calcular_media_idades, gerar_mensagem_personalizada, limpar_usuarios

class TesteSistema(unittest.TestCase):

    def setUp(self):
        """Reseta a lista de usuários antes de cada teste"""
        self.usuarios = limpar_usuarios()

    def test_adicionar_usuario(self):
        """Testa a adição de um novo usuário."""
        self.usuarios = adicionar_usuario(self.usuarios, "Carlos", 30)
        self.assertEqual(len(listar_usuarios(self.usuarios)), 1)
        self.assertEqual(listar_usuarios(self.usuarios)[0]["nome"], "Carlos")

    def test_listar_usuarios(self):
        """Testa se a listagem retorna uma lista."""
        self.usuarios = adicionar_usuario(self.usuarios, "Ana", 22)
        self.usuarios = adicionar_usuario(self.usuarios, "Bruno", 25)
        lista = listar_usuarios(self.usuarios)
        self.assertIsInstance(lista, list)
        self.assertEqual(len(lista), 2)

    def test_filtrar_maiores(self):
        """Testa se apenas maiores de idade são retornados."""
        self.usuarios = adicionar_usuario(self.usuarios, "Ana", 17)
        self.usuarios = adicionar_usuario(self.usuarios, "Marcos", 20)
        self.usuarios = adicionar_usuario(self.usuarios, "João", 25)
        maiores = filtrar_maiores(self.usuarios)
        self.assertEqual(len(maiores), 2)
        self.assertTrue(all(user["idade"] >= 18 for user in maiores))

    def test_calcular_media_idades(self):
        """Testa o cálculo da média das idades."""
        self.usuarios = adicionar_usuario(self.usuarios, "Eduardo", 30)
        self.usuarios = adicionar_usuario(self.usuarios, "Fernanda", 20)
        media = calcular_media_idades(self.usuarios)
        self.assertEqual(media, 25)

    def test_gerar_mensagem_personalizada(self):
        """Testa a geração de mensagem personalizada."""
        msg_func = gerar_mensagem_personalizada("Oi")
        self.assertEqual(msg_func("Carlos"), "Oi, Carlos!")

if __name__ == '__main__':
    unittest.main()
