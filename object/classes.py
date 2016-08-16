class Enemy:
    life = 3
    def attack(self):
        print("ouch!")
        self.life -= 1
    def lifecheck(self):
        if self.life <= 0:
            print("dead")
        else:
            print(self.life, "life left!")


enemy1 = Enemy
enemy2 = Enemy()
enemy3 = Enemy

enemy1.attack(enemy2)
enemy1.lifecheck(enemy2)
enemy1.lifecheck(enemy1)
enemy1.attack(enemy1)
enemy1.lifecheck(enemy1)
enemy3.lifecheck(enemy3)

