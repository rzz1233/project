# 四、面向对象实现人狗大战
# 1.人狗初始血量值100，人攻击力10，狗攻击力8；
# 2.可以普通攻击和技能攻击（每攻击三次发动一次技能）；
# 3.人狗均可以防御，防御减伤本次所受伤害的50%。（30%概率防御）。
import random
class People(object):
    def __init__(self):
        self.hp = 100
        self.peo_gj = 10
        self.peo_gj_pro = 30
        self.num = 0
    def attack_main(self,dog):
        self.num += 1
        if self.num == 3:
            self.num = 0
            print("人发动技能")
            self.attack_pro(dog)
        else:
            print("人普通攻击")
            self.attack(dog)
    def attack(self,dog):
        a = random.random()
        if a < 0.3:
            dog.hp -= self.peo_gj *0.5
            print(f"狗防御成功,剩下{dog.hp}血量")
        else:
            dog.hp -= self.peo_gj
            print(f"狗收到普通攻击剩下{dog.hp}血量")

    def attack_pro(self,dog):
        a = random.random()
        if a < 0.3:
            dog.hp -= self.peo_gj_pro *0.5
            print(f"狗防御成功,剩下{dog.hp}血量")
        else:
            dog.hp -= self.peo_gj_pro
            print(f"狗受到到技能攻击剩下{dog.hp}血量")

class Dog(object):
    def __init__(self):
        self.hp = 100
        self.dog_gj = 8
        self.dog_gj_pro = 28
        self.num = 0
    def attack_main(self,people):
        self.num += 1
        if self.num == 3:
            self.num = 0
            print("狗发动技能")
            self.attack_pro(people)
        else:
            print("狗普通攻击")
            self.attack(people)
    def attack(self,people):
        a = random.random()
        if a < 0.3:
            people.hp -= self.dog_gj *0.5
            print(f"人防御成功,剩下{people.hp}血量")
        else:
            people.hp -= self.dog_gj
            print(f"人收到普通攻击剩下{people.hp}血量")

    def attack_pro(self,people):
        a = random.random()
        if a < 0.3:
            people.hp -= self.dog_gj_pro *0.5
            print(f"人防御成功,剩下{people.hp}血量")
        else:
            people.hp -= self.dog_gj_pro
            print(f"人受到技能攻击剩下{people.hp}血量")


def run(people, dog):
    while True:
        # 人攻击狗
        people.attack_main(dog)
        if dog.hp <= 0:
            print("人获胜!")
            break

        # 狗攻击人
        dog.attack_main(people)
        if people.hp <= 0:
            print("狗获胜!")
            break



if __name__ == '__main__':
    people = People()
    dog = Dog()
    run(people,dog)






