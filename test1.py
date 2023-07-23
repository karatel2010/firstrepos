import random
# class User():
#     def __init__(self,name):
#         self.name=name
#         self.id=random.randint(1,777777777777777777)
#
# user=User(name='федор')
# print(user.id)
class Phone():
    username = "Kate"                # public variable
    __how_many_times_turned_on = 0   # private variable

    def call(self):                  # public method
        print( "Ring-ring!" )
        self.__turn_on()
    def __turn_on(self):             # private method
        self.__how_many_times_turned_on += 1
        print( "Times was turned on: ", self.__how_many_times_turned_on)
        # my_phone.__turn_on()
my_phone = Phone()

my_phone.call()
print( "The username is ", my_phone.username)