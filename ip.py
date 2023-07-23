class Character():
    def __init__(self,hp=100,dm=50,df=20):
        self.hp=hp
        self.dm=dm
        self.df=df
    def walk(self):
        print('I can catch up with you')
    def fight(self):
        print('i can kill you')
    def speak(self):
        print('I_m talking to you')

class Goblin(Character):
    def steal(self):
        print('I_m steal your money')

class Goblin2(Goblin):
    def __init__(self,hp=100,dm=50,df=20,stamina=10):
        self.stamina=stamina
        self.hp = hp
        self.dm = dm
        self.df = df
    def agrresive(self):
        print('i_m agrresive')
    def summongoblin():
        print('summoning goblins')
h=Goblin2()
print(h.hp)
class Goblin3(Goblin2):
    def __init__(self,hp=100,dm=50,df=25,mana=100):
        super().__init__(hp,dm,df)
        self.mana=mana
    def nvis(self):
        print('I_m in the inviz')
    def throwfirebol(self):
        print('I_m throwing a fireball')
f=Goblin3()
print(f.df)
class Goblin4(Goblin3):
    def fly(self):
        print("I'm taking off")
    def dropbomb(self):
        print("I'm dropping bombs")


class Spiderman():
    def __init__(self,hp=120'):
        self.hp=hp
    def splitweb(self):
        print("I'm throwing a web")
    def bite(self):
        print("i'm shall bite ")

class Spiderman2(Spiderman):
    def jump(self):
        print("i'm jumping")

class Spiderman3(Spiderman2):
    def __init__(self,hp=120,venom='20s'):
        super().__init__(hp)
        self.venom=venom
    def __summonsp(self):
        print("i'm summon of spider-man")
