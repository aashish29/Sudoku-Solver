import Sudoku

sudoku_obj = Sudoku.Sudoku()
sudoku_obj.read_game_file("game2.sudoku")
start = time.time()
sudoku_obj.get_zero_list()
sudoku_obj.solve_sudoku(0)
elapsed = (time.time() - start)
print (elapsed)
sudoku_obj.print_matrix()
