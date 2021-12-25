from aocd import get_data

data = get_data(day=21, year=2021)
data = data.splitlines()

startingPositions = []
for line in data:
    startingPositions.append(int(line.split(": ")[1]))

diceValue = 0
diceTotalRolled = 0
grid = list(range(1, 11))

def diceAdd():
    global diceValue
    if(diceValue == 100):
        diceValue = 1
        return
    diceValue += 1

class Player:
    def __init__(self, num, position, score=0):
        self.score = score
        self.position = position
        self.num = num
    def __str__(self):
        return "Player #{} has score {}".format(self.num, self.score)

firstPlayer = Player(1, startingPositions[0])
secondPlayer = Player(2, startingPositions[1])

while True:
    for playerTurn in range(2):
        positionsToMove = 0
        for i in range(3):
            diceAdd()
            diceTotalRolled += 1
            positionsToMove += diceValue
        if(playerTurn == 0):
            firstPlayer.position += positionsToMove
            if(firstPlayer.position > 10):
                firstPlayer.position = firstPlayer.position%10
            firstPlayer.score += grid[firstPlayer.position-1]
            if(firstPlayer.score >= 1000):
                print(diceTotalRolled * secondPlayer.score)
                exit()
        else:
            secondPlayer.position += positionsToMove
            if(secondPlayer.position > 10):
                secondPlayer.position = secondPlayer.position%10
            secondPlayer.score += grid[secondPlayer.position-1]
            if(secondPlayer.score >= 1000):
                print(diceTotalRolled * firstPlayer.score)
                exit()
