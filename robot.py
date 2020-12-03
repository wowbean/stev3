directions = {"u":"^ ","l":"< ","r":"> ","d":"v "}

class Robot:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.pos = (5,5)
    self.direc = "u"
    self.updaterobot()
    self.out()

  def updaterobot(self):
    rx,ry = self.pos
    if rx > (self.x) or ry > (self.y) or rx == -1 or ry == -1:
      print("The robot crashed!");exit()
    char = directions[self.direc]
    grid = [["x " for _ in range(self.x)]  for _ in range(self.y)]
    grid[ry][rx] = char
    self.grid = grid
    print("")

  def out(self):
    print("\n".join(["".join(x) for x in self.grid]))

  def l(self):
    self.direc = "l"
    rx,ry = self.pos
    self.pos = (rx-1,ry)
    self.updaterobot()
    self.out()

  def r(self):
    self.direc = "r"
    rx,ry = self.pos
    self.pos = (rx+1,ry)
    self.updaterobot()
    self.out()

  def u(self):
    self.direc = "u"
    rx,ry = self.pos
    self.pos = (rx,ry-1)
    self.updaterobot()
    self.out()

  def d(self):
    self.direc = "d"
    rx,ry = self.pos
    self.pos = (rx,ry+1)
    self.updaterobot()
    self.out()


### Program starts here

robot = Robot(11,11)
while True:
  instruction = input("Enter your instruction: ")
  eval(f'robot.{instruction}()')