def main():
  eight_queens = EightQueens()

  starting_node = Node(8)
  starting_node2 = deepcopy(starting_node)

  starting_node.print_board()
  starting_node.print_state()
  starting_node.print_attacks()

  print("\nExecuting Hill Climbing")
  eight_queens.hill_climb(starting_node)
  starting_node.print_board()
  starting_node.print_state()
  starting_node.print_attacks()

  print("\nExecuting Simulated Annealing")
  eight_queens.simulated_annealing(starting_node2)
  starting_node2.print_board()
  starting_node2.print_state()
  starting_node2.print_attacks()
