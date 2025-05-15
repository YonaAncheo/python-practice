import random

class Game:
  
  def __init__(self):
    self._player_choice: str = ''
    self._cpu_choice: str = ''
    self._player_count: int = 0
    self._round: int = 1
    self._OPTIONS: tuple = ('rock','scissors','paper')
    self._historial: dict = {}
  
  def player_win(self) -> bool:
    wins: dict = {
      'rock': 'scissors',
      'scissors': 'paper',
      'paper': 'rock'
    }
    return wins[self._player_choice] == self._cpu_choice

  def set_cpu_choice(self) -> None:
    self._cpu_choice = random.choice(self._OPTIONS)
  
  def add_to_historial(self) -> dict:
    self._historial[f'Round {self._round}'] = {'player':self._player_choice, 'cpu': self._cpu_choice}
    self._round += 1
    return self._historial
  
  def draw(self) -> bool:
    return self._player_choice == self._cpu_choice
  
  def valid_option(self) -> bool:
    return self._player_choice in game._OPTIONS
  
game: Game = Game()

while(True):
  print('GAME START')
  print(f"Round {game._round}: Enter 'rock', 'paper', or 'scissors' (or 'q' to quit)")
  game._player_choice = input().lower()
  if game._player_choice == 'q':
    break
  if not game.valid_option():
    print(f'YOU ENTER A INVALID OPTION: {game._player_choice}. TRY AGAIN...')
    continue
  
  game.set_cpu_choice()
  game.add_to_historial()
  print(game._historial)
  if game.draw():
    print ('IS A DRAW')
    continue
  if game.player_win():
    game._player_count +=1
    print('You win this Round')
  else:
    print('You lose this round')
  print(f'Score: {game._player_count}')
print(f'GAME OVER. YOUR SCORE FINAL IS {game._player_count}')