
class Shark():
    def swim(self):
        return('shark is swimming')
    def swimbackword(self):
        return("акула назад не плывет")
    def skeleton(self):
        return("скелет акулы состоит из хрящей")


class Clownfish():
    def swim(self):
        return('clownshark is swimming')
    def swimbackword(self):
        return("clownfish is swimming backword")
    def skeleton(self):
        return("скелет рыбы клоуна состоит из костей")

u=Shark()
p=Clownfish()
# jkdbfsjldfvshfysivfysidfvyusdgukhfkasd,ajsdkaswfwefs
for fish in (u,p):
    f"{fish.skeleton()} {fish.swim()}  {fish.swimbackword()}"
=
def hello(fish):
    return(fish.swim()+fish.swimbackword())

print(hello(u))





