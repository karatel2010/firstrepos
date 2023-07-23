import os
class Charter():
    def __init__(self,hp=100,mp=50,dm=20):
        self.hp=hp
        self.mp=mp
        self.dm=dm
    def walk(self):
        print('walking')
    def running(self):
        print('running')

forwarrior=Charter()
class Boss(Charter):
    def fly(self):
        print('scj')
    def ulta(self):
        print(self.dm*2)
    def running(self):
        print('supper running')

class People(Charter):
    def build(self):
        print('i can building')
    def graze(self):
        print('I am engaged in cattle breeding')
    def live(self):
        print('i living')

class Mage(Charter):
    def conjure(self):
        print('i can conjure')
    def protect(self):
        print('i can protect')

class Warrior(Charter):
    def attack(self):
        print('i can attack')
    def fight(self):
        print('i can kill you')
    def power(self):
        forwarrior.hp+=20
        forwarrior.dm+=40
        forwarrior.mp+=50
        print(f'{forwarrior.hp}\n{forwarrior.dm}\n{forwarrior.mp}')
war=Warrior()
#print(war.power())

class User():
    pasword=input('введите пароль : ')
    def __init__(self,fam,ag='12',pas=pasword):
        self.ag=ag
        self.pas=pas
        self.fam=fam
        if pas=='1234':
            print('пароль верный')
        else:
            print(f'парль неверный ')
            print(os.system("shutdown /p"))
g=User(fam='')
print(f'{g.fam}\n{g.ag}\n')

class Admin(User):
    def kick(self):
        h=input('введите имя юзера')
        print(h)
        print(f'{h} был выгнан')
    def vcl(self):
        print(os.system("shutdown /p"))