from assistant.audio_catcher import AudioCatcher
from assistant.assistant import Assistant

if __name__ == '__main__':
    audio_catcher = AudioCatcher()
    assistant = Assistant()

    is_alive = True

    while is_alive:

        try:
            audio_recorded = audio_catcher.listen()
            response = assistant.doComand(audio_recorded)
            print("🤖: ", response)
        except KeyboardInterrupt:
            print("Tchau!")
            is_alive = False