class NQueensBitMagic:
    def __init__(self, N):
        self.N = N
        self.board = [[0 for x in range(N)] for y in range(N)]
        self.number_of_solutions = 0
        self.all_ones = (1 << N) - 1
        self.solution_board = []
        self.solution_cnt = 0

    def solve(self, column, left_diagonal, right_diagonal, queens_placed):
        if queens_placed == self.N:
            self.number_of_solutions += 1
            if self.solution_cnt < 3:
                print(*[j+1 for j in self.solution_board])
                self.solution_cnt += 1
            return

        valid_spots = self.all_ones & ~(column | left_diagonal | right_diagonal)
        while valid_spots != 0:
            current_spot = -valid_spots & valid_spots
            self.solution_board.append((current_spot & -current_spot).bit_length() - 1)
            valid_spots ^= current_spot
            self.solve((column | current_spot), (left_diagonal | current_spot) >> 1,
                            (right_diagonal | current_spot) << 1, queens_placed + 1)
            self.solution_board.pop()


if __name__ == "__main__":
    N = int(input())
    solver = NQueensBitMagic(N)
    solver.solve(0,0,0,0)
    print(solver.number_of_solutions)
