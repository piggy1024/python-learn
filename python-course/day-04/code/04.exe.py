# exe.py
class Dog():
    '''
        表示狗的类
    '''
    # 狗的名字
    name = ''
    # 狗的年龄
    age = 0
    # 狗的性别
    gender = ''
    #狗的体重
    weight = 0
    #初始化方法
    def __init__(self , name , age , gender , weight    ):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = weight

    # the introduce of dog
    def selfIntro(self):
        print(f'my name is {self.name},I am {self.age}, I am a good {self.gender},my weight is {self.weight}')
    # 狗的方法--叫
    def bark(self):
        print('汪汪汪')
    # 狗的方法--咬人
    def bit(self):
        print('狗咬人了！！')
    # 狗的方法--跑
    def run(self):
        print('The dong is running!')

first_dog = Dog('哈巴狗',2,'boy',29)
first_dog.selfIntro()
first_dog.bark()
first_dog.bit()
first_dog.run()