class Greet():
    def hello(self):
        print("hello")
    def hi(self):
        print("hi")
human1=Greet()
human2=Greet()
human1.hello()
human2.hi()

class Student():
    def __init__(self,name,age,like):
        self.name=name
        self.age=age
        self.like=like
    def studentInfo(self):
        print(f"이름:{self.name}, 나이:{self.age}, 좋아하는것:{self.like}")
김철수=Student("김철수",17,"축구")
김철수.studentInfo()

class Mother():
    def characteristic(self):
        print("키가 크다")
        print("공부를 잘한다")
class Daughter(Mother):
    def characteristic(self):
        super().characteristic()
        print("운동을 잘한다")
엄마=Mother()
딸=Daughter()
print("엄마는")
엄마.characteristic()
print("딸은")
딸.characteristic()

class Mother2():
    def __init__(self):
        print("키가 크다")
        print("공부를 잘한다")
class Daughter2(Mother2):
    def __init(self):
        super().__init__()
        print("운동을 잘한다")
print("엄마는")
엄마=Mother2()
print("딸은")
딸=Daughter2()