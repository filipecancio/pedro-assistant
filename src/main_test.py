import unittest
from assistant.audio_catcher import AudioCatcher
from assistant.assistant import Assistant

audio_catcher = AudioCatcher()
assistant = Assistant()

class TesteErrosNome(unittest.TestCase):

    def testar_nome_errado(self):
        # configuration
        errado_1 =  audio_catcher.play_recorded_audio("/util/audio/agua_amanda.wav")

        # execution
        response = assistant.doComand(errado_1)

        # assertion
        self.assertTrue(response == "Nome de assistente incorreto.")

    def testar_sem_nome(self):
        # configuration
        errado_2 =  audio_catcher.play_recorded_audio("/util/audio/verifica_racao_gato_errado.wav")

        # execution
        response = assistant.doComand(errado_2)

        # assertion
        self.assertTrue(response == "Nome de assistente incorreto.")

    def testar_comando_errado(self):
        # configuration
        errado_3 =  audio_catcher.play_recorded_audio("/util/audio/me_acorde_daqui_minutos.wav")

        # execution
        response = assistant.doComand(errado_3)

        # assertion
        self.assertTrue(response == "Comando não encontrado.")

class TesteGato(unittest.TestCase):

    def testar_colocar_racao_gato(self):
        # configuration
        audio_mock =  audio_catcher.play_recorded_audio("/util/audio/colocar_racao_gato.wav")

        # execution
        response = assistant.doComand(audio_mock)

        # assertion
        self.assertTrue(response == "Colocando a ração para o gato")

    def testar_verificar_racao_gato(self):
        # configuration
        audio_mock =  audio_catcher.play_recorded_audio("/util/audio/verificar_racao_gato.wav")

        # execution
        response = assistant.doComand(audio_mock)

        # assertion
        self.assertTrue(response == "Verificando ração para o gato, Ainda há 20% de ração no pote")

    def testar_trocar_racao_gato(self):
        # configuration
        audio_mock =  audio_catcher.play_recorded_audio("/util/audio/trocar_racao_gato.wav")

        # execution
        response = assistant.doComand(audio_mock)

        # assertion
        self.assertTrue(response == "Trocando a ração velha no pote do gato")

class TesteCachorro(unittest.TestCase):

    def testar_colocar_racao_cachorro(self):
        # configuration
        audio_mock =  audio_catcher.play_recorded_audio("/util/audio/colocar_racao_cachorro.wav")

        # execution
        response = assistant.doComand(audio_mock)

        # assertion
        self.assertTrue(response == "Colocando a ração para o cachorro")

    def testar_verificar_racao_cachorro(self):
        # configuration
        audio_mock =  audio_catcher.play_recorded_audio("/util/audio/verificar_racao_cachorro.wav")

        # execution
        response = assistant.doComand(audio_mock)

        # assertion
        self.assertTrue(response == "Verificando ração para o cachorro, Ainda há 10% de ração no pote")

    def testar_trocar_racao_cachorro(self):
        # configuration
        audio_mock =  audio_catcher.play_recorded_audio("/util/audio/trocar_racao_cachorro.wav")

        # execution
        response = assistant.doComand(audio_mock)

        # assertion
        self.assertTrue(response == "Trocando a ração velha no pote do cachorro")

class TesteAgua(unittest.TestCase):

    def testar_colocar_agua(self):
        # configuration
        audio_mock =  audio_catcher.play_recorded_audio("/util/audio/colocar_agua.wav")

        # execution
        response = assistant.doComand(audio_mock)
        print(f"response: {response}")

        # assertion
        self.assertTrue(response == "Colocando mais agua no pote")

    def testar_verificar_agua(self):
        # configuration
        audio_mock =  audio_catcher.play_recorded_audio("/util/audio/verificar_agua.wav")

        # execution
        response = assistant.doComand(audio_mock)

        # assertion
        self.assertTrue(response == "Verificando se tem água no pote. Ainda há metade de água no pote")

    def testar_trocar_agua(self):
        # configuration
        audio_mock =  audio_catcher.play_recorded_audio("/util/audio/trocar_agua.wav")

        # execution
        response = assistant.doComand(audio_mock)

        # assertion
        self.assertTrue(response == "Trocando a água do pote pra uma fresquinha")

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    
    #testes.addTest(carregador.loadTestsFromTestCase(TesteErrosNome))
    #testes.addTest(carregador.loadTestsFromTestCase(TesteGato))
    #testes.addTest(carregador.loadTestsFromTestCase(TesteCachorro))
    testes.addTest(carregador.loadTestsFromTestCase(TesteAgua))

    executor = unittest.TextTestRunner()
    executor.run(testes)