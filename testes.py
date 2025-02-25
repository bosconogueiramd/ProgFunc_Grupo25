import unittest
from main import adicionar_usuario, listar_usuarios, filtrar_maiores, calcular_media_idades, gerar_mensagem_personalizada

class TesteSistema(unittest.TestCase):
    def test_adicionar_usuario(self):
        adicionar_usuario("Carlos", 30)
        self.assertEqual(len(listar_usuarios()), 1)

    def test_listar_usuarios(self):
        self.assertIsInstance(listar_usuarios(), list)

    def test_filtrar_maiores(self):
        adicionar_usuario("Ana", 17)
        self.assertEqual(len(filtrar_maiores()), 1)

    def test_calcular_media_idades(self):
        self.assertGreaterEqual(calcular_media_idades(), 0)

    def test_gerar_mensagem_personalizada(self):
        msg_func = gerar_mensagem_personalizada("Oi")
        self.assertEqual(msg_func("Carlos"), "Oi, Carlos!")

if __name__ == '__main__':
    unittest.main()

