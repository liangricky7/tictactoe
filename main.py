class Board():
  def __init__(self):
    self.state = [[None for i in range(3)] for j in range(3)]
    self.currentPlayer = "X"
    print(self.state)

  def checkWin(self):
    return True

  def playPiece(self, x, y):
    if self.state[y][x] == None:
      self.state[y][x] = self.currentPlayer
    return self.checkWin()



def main():
  print("Playing TicTacToe...")
  board = Board()
  ended = False
  while not ended:
    x = int(input("enter the x coordinate of your move "))
    y = int(input("enter the y coordinate of your move "))
    ended = board.playPiece(x, y)
    print(ended)

if __name__ == "__main__":
  main()


