class EightQueens:
  def __init__(self):
    self.temperature = 4000

    self.temperature_decrease = 0.99

  def hill_climb(self, node):
    while True:
      node.generate_best_neighbour()
      if node.attacks == node.neighbour_node.attacks:
        break
      node.copy_board(node.temp_neighbour)

  def simulated_annealing(self, node):

    solution_found = False
    cost_answer = node.attacks
    while self.temperature > 0:
      self.temperature *= self.temperature_decrease
      node.neighbour_node.copy_board(node)
      if cost_answer == 0:
        solution_found = True
        break
      node.generate_random_neighbour()
      heuristic_difference = node.neighbour_node.attacks - cost_answer

      if heuristic_difference < 0 or random.uniform(0, 1) < math.exp(-heuristic_difference / self.temperature):
        node.copy_board(node.neighbour_node)
        cost_answer = node.attacks

    if solution_found == False:
      print("Failed to obtain solution")
