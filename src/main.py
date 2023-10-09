from domain.dog import Dog
from domain.cat import Cat


if __name__ == "__main__":
    fido = Dog("Fido")
    duda = Cat("Duda")
    print(fido.drink())
    print(fido.eat())
    print(fido.poop())
    #print(fido.peed())
    #print(duda.drink())
    #print(duda.eat())
    #print(duda.poop())
   # print(duda.peed())