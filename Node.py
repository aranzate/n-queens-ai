EMPTY = 0
QUEEN = 1

class Node:
  def __init__(self, n):
    self.board = numpy.zeros([n, n])
    self.n = n
    self.state = []
    self.attacks = 0
    self.generate_random_state()
    self.attacks_happening()
    self.neighbour_node = deepcopy(self)
    self.temp_neighbour = deepcopy(self)

  
  
  def copy_board(self, source):
    self.state = deepcopy(source.state)
    self.board = deepcopy(source.board)
    self.attacks = deepcopy(source.attacks)
  
  def generate_neighbour(self):
    self.neighbour_node.copy_board(self)
  
  def generate_random_neighbour(self):
    self.neighbour_node = Node(len(self.board))
    self.neighbour_node.copy_board(self)
    while True:
      random_col = random.randint(0, len(self.board)-1)
      random_row = random.randint(0, len(self.board)-1)
      if random_col != random_row:
        break
    self.neighbour_node.board[self.neighbour_node.state[random_col]][random_col] = EMPTY
    self.neighbour_node.state[random_col] = random_row
    self.neighbour_node.board[self.neighbour_node.state[random_col]][random_col] = QUEEN
    self.neighbour_node.generate_board()
    self.neighbour_node.attacks_happening() 

  def print_board(self):
    print(self.board)
    
  def print_state(self):
    print("Estado: ", end="")
    print(self.state)
  
  def print_attacks(self):
    print("Pares de rainha se atacando: ", end="")
    print(self.attacks)
  
  def compare_states(self, state):
    return True if self.state == state else False

  def generate_random_state(self):
    for col in range(len(self.board)):
      self.state.append(random.randint(0, len(self.board)-1))
    self.generate_board()
  
  def generate_board(self):
    self.board = numpy.zeros([len(self.state), len(self.state)])
    for col in range(len(self.state)):
      self.board[self.state[col]][col] = QUEEN

  def generate_best_neighbour(self):
    for col in range(self.n):
      self.neighbour_node.copy_board(self)
      for row in range(self.n):
        if row == self.neighbour_node.state[col]:
          continue
        self.neighbour_node.state[col] = row
        self.neighbour_node.generate_board()
        self.neighbour_node.attacks_happening()

        if self.neighbour_node.attacks < self.temp_neighbour.attacks:
          self.temp_neighbour.copy_board(self.neighbour_node)
    self.neighbour_node.copy_board(self.temp_neighbour)


  def attacks_happening(self):
    self.attacks = 0
    for col in range(len(self.board)):

      diagonalCol = col - 1
      diagonalRow = self.state[col]
      while True:
        if diagonalCol < 0:
          break
        if self.board[diagonalRow][diagonalCol] == QUEEN:
          self.attacks += 1
          break
        diagonalCol -= 1
      
      diagonalCol = col + 1
      while True:
        if diagonalCol >= len(self.board):
          break
        if self.board[diagonalRow][diagonalCol] == QUEEN:
          self.attacks += 1
          break
        diagonalCol += 1

      diagonalCol = col - 1
      diagonalRow = self.state[col] - 1
      while True:

        if diagonalCol < 0 or diagonalRow < 0:
          break
        if self.board[diagonalRow][diagonalCol] == QUEEN:
          self.attacks += 1
          break
        diagonalCol -= 1
        diagonalRow -= 1

      diagonalCol = col + 1
      diagonalRow = self.state[col] + 1

      while True:
        if diagonalCol >= len(self.board) or diagonalRow >= len(self.board):
          break
        if self.board[diagonalRow][diagonalCol] == QUEEN:
          self.attacks += 1
          break
        diagonalCol += 1
        diagonalRow += 1

      diagonalCol = col + 1
      diagonalRow = self.state[col] - 1

      while True:
        if diagonalCol >= len(self.board) or diagonalRow < 0:
          break
        if self.board[diagonalRow][diagonalCol] == QUEEN:
          self.attacks += 1
          break
        diagonalCol += 1
        diagonalRow -= 1

      diagonalCol = col - 1
      diagonalRow = self.state[col] + 1

      while True:
        if diagonalCol < 0 or diagonalRow >= len(self.board):
          break
        if self.board[diagonalRow][diagonalCol] == QUEEN:
          self.attacks += 1
          break
        diagonalCol -= 1
        diagonalRow += 1

    self.attacks = int(self.attacks / 2)
