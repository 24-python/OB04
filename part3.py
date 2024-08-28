# #Метод постановки Барбары ЛИСКОВ
#
# class Bird():
#     def __init__(self, name):
#         self.name = name
#
#     def fly(self):
#         print("птица летает")
#
# class Ping(Bird):
#     pass
#
# p = Ping("Сара")
# p.fly()
#
#
class Bird():
    def fly(self):
        print("птица летает")

class Duck(Bird):
    def fly(self):
        print("Утка летает")

class Ping(Bird):
    def fly(self):
        print("Пингвин не летает")

def fly_in_the_sky(animal):
    animal.fly()



b = Bird()
d = Duck()
p = Ping()
fly_in_the_sky(b)
fly_in_the_sky(d)
fly_in_the_sky(p)

