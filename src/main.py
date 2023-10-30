from assistant.audio_catcher import AudioCatcher
from assistant.assistant import Assistant

if __name__ == '__main__':
    audio_catcher = AudioCatcher()
    assistant = Assistant()

    while True:
        audio_recorded = audio_catcher.listen
        assistant.doComand(audio_recorded)