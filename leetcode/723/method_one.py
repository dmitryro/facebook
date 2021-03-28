class Solution:

    #TC: O(TotalRow*TotalCol)
    #SC: O(m) m: total number of candies to be crush

    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        TotalRow = len(board)
        TotalCol = len(board[0]) 

        while True:
            #Find crush candies
            Crush = set([])
            for row in range(TotalRow):
                for col in range(TotalCol):
                    if row >=2 and board[row][col] and board[row][col] == board[row-1][col] == board[row-2][col]:
                        Crush |= {(row, col), (row-1,col),(row-2,col)}

                    if  col >=2 and  board[row][col] and board[row][col] == board[row][col-1] == board[row][col-2]:
                        Crush |= {(row, col), (row,col-1),(row,col-2)}

            if len(Crush) == 0:
                break
            #Assign them to 0
            for row, col in Crush:
                board[row][col] = 0

            #Drop
            for col in range(TotalCol):
                idx = TotalRow - 1

                for row in reversed(range(TotalRow)):                    
                    if board[row][col] > 0:
                        board[idx][col] = board[row][col]
                        idx -= 1

                for i in range(idx+1):
                    board[i][col] = 0
            print(board)

        return board
