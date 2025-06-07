class Character:
  def __init__(self, name: str, attack: int, defense: int, speed: int, weapon: str ) -> None:
    self._name= name
    self._attack = attack
    self._defense = defense
    self._speed = speed
    self._weapon = weapon
    pass

  def toStr(self) -> str:
    return f'''name: {self._name}
attack: {self._attack}
defense: {self._defense}
speed: {self._speed}
weapon: {self._weapon}
            '''
    pass

player = Character('Jhon', 10, 7, 8, 'Hands')
print(player.toStr())