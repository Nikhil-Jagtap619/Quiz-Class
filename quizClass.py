import random
class quiz:
    def __init__(self):
        self.games = {"call of duty": "activision",
                      "Pubg":"tencent",
                      "fortnite":"epic games",
                      "tom clancy series": "ubisoft",
                      "resident evil": "capcom"}

    def game(self):
        self.attemp = 0
        print("Welcome To Guessing Game")
        while True:
            g, c = random.choice(list(self.games.items()))
            ques = input(f"what commpany created the game {g.title()}: ")
            if ques.lower() == c.lower():
                print("bingo!")
                self.attemp += 1
            else:
                print("Booo")
                self.attemp+=1
            opt = input("Give another shot? [y/n]: ")
            if opt.lower()!="y":
                break
obj = quiz()
obj.game()
print(obj.attemp)