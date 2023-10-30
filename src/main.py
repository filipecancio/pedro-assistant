from assistant.audio_catcher import AudioCatcher
from domain.dog import Dog
from domain.cat import Cat

if __name__ == '__main__':
    fido = Dog("Fido")
    print(fido.eat())
    print(fido.seeHungry())
    print(fido.eat())
    print(fido.seeHungry())
    #audio_catcher = AudioCatcher()

    #example = audio_catcher.play_recorded_audio("/util/audio/agua.wav")
    #print(example)

#if __name__ == "__main__":
    #fido = Dog("Fido")
    #duda = Cat("Duda")
    #print(fido.drink())
    #print(fido.eat())
    #print(fido.poop())
    #print(fido.peed())
    #print(duda.drink())
    #print(duda.eat())
    #print(duda.poop())
   # print(duda.peed())