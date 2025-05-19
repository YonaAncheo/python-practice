import random

class Game:
  playerChoice: str
  cpuChoice: str
  playerCount: int
  options: tuple
  history: dict
  round: int
  
  def __init__(self):
    self.playerCount = 0
    self.round = 1
    self.options = ('rock','scisor','paper')
    self.history = {}
  
  def PlayerWin(self) -> bool:
    condition1: bool = self.playerChoice == self.options[0] and self.cpuChoice == self.options[1]
    condition2: bool = self.playerChoice == self.options[1] and self.cpuChoice == self.options[2]
    condition3: bool = self.playerChoice == self.options[2] and self.cpuChoice == self.options[0]
    if condition1 or condition2 or condition3:
      return True
    else:
      return False

  def CpuChoice(self) -> None:
    self.cpuChoice = random.choice(self.options)
  
  def AddToHistory(self) -> dict:
    self.history[f'Round {self.round}'] = {'player':self.playerChoice, 'cpu': self.cpuChoice}
    self.round += 1
    return self.history
  
  def Draw(self) -> bool:
    if self.playerChoice == self.cpuChoice:
      return True
    return False
  
game: Game = Game()

while(True):
  print('GAME START')
  print(f'Round {game.round}: Enter an option')
  game.playerChoice = input().lower()
  game.CpuChoice()
  game.AddToHistory()
  print(game.history)
  if game.Draw():
    print ('IS A DRAW')
    continue
  if game.PlayerWin():
    game.playerCount +=1
    print('You win this Round')
  else:
    print('You lose this round')
  print(f'Score: {game.playerCount}')