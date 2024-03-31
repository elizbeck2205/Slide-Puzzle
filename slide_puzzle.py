import random

class Board:
    def __init__(self, n):
        self.arr = list(range(1, n*n+1))
        self.n = n
        self.blank_index = n*n-1

        self.configureBoard()
    
    # def swap(self, i):
    #     if self.isValidSwap(i):
    #         # swap
    #         self.arr[self.blank_index] = self.arr[i]
    #         self.arr[i] = self.n**2

    #         # update blank index
    #         self.blank_index = i


    # def isValidSwap(self, i):
    #     valid = False
    #     n = self.n
    #     blank_tile = n*n
    #     blank_index = self.blank_index

    #     if abs(i-blank_index) <= 4:
    #         # Is i adjacent to the blank?
    #         if self.arr[i-1] == blank_tile or self.arr[i+1] == blank_tile or i%n == blank_index%n:
    #             valid = True

    #     return valid

    def configureBoard(self):
        random.shuffle(self.arr)

        self.blank_index = self.arr.index(self.n**2)

        solvable = self.isSolvable()
        print('Is Solvable? ', solvable)

        if not solvable:
            # Add another transposition to make the configuration an even permutation
            r = list(range(0, self.blank_index)) + list(range(self.blank_index + 1, self.n**2))

            indices = random.sample(r, 2)

            # swap indices
            temp = self.arr[indices[0]]
            self.arr[indices[0]] = self.arr[indices[1]]
            self.arr[indices[1]] = temp

            solvable = self.isSolvable()

            # todo is it solvable when blank can be swapped?
            # todo a regular 'swap'?

            print('Is Solvable (new iter)? ', solvable)


    def isSolvable(self):
        # check if array is solvable

        solvable = False
        even_inversions = self.countInversions() % 2 == 0
        blank_on_even_row = True if (self.blank_index // self.n) % 2 == 1 else False
        
        if self.n % 2 == 0:
            solvable = not even_inversions if blank_on_even_row else even_inversions
        elif even_inversions:
            solvable = True

        return solvable
    
    def countInversions(self):
        N = self.n**2
        inversions = 0

        for i in range(N-1):
            for j in range(i+1, N):
                if self.arr[i] > self.arr[j]:
                    inversions += 1        
        return inversions