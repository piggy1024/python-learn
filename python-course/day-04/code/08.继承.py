# 08.继承.py


class Animal:
    def run(self):
        print('动物会跑~~~')

    def sleep(self):
        print('动物睡觉~~~')

    def  bark(self):
        print('动物嚎叫~~~')

class Dog(Animal):
    def bark(self):
        print('wangwangwang~~')
    
class HaShiQi(Dog):
    def fan_sha(self):
        print('我是一致莎莎的哈士奇')

d = Dog()

h = HaShiQi()
