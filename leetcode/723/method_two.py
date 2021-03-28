class Solution:
    #TC: O(TotalRow*TotalCol)
    #SC: O(1)

    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        TotalRow = len(board)
        TotalCol = len(board[0]) 

        while True:
            #Find crush candies
            Crush = set([])
            Flag = False
            for row in range(TotalRow):
                for col in range(TotalCol):
                    if row >=2 and board[row][col]!=0 and abs(board[row][col]) == abs(board[row-1][col]) == abs(board[row-2][col]):
                        board[row][col] = -abs(board[row][col])
                        board[row-1][col] = -abs(board[row-1][col])
                        board[row-2][col] = -abs(board[row-2][col])
                        Flag = True


                    if  col >=2 and board[row][col]!=0 and abs(board[row][col]) == abs(board[row][col-1]) == abs(board[row][col-2]):
                        board[row][col] = -abs(board[row][col])
                        board[row][col-1] = -abs(board[row][col-1])
                        board[row][col-2] = -abs(board[row][col-2])
                        Flag = True

            if not Flag:
                break
            #Assign them to 0
            for row in range(TotalRow):
                for col in range(TotalCol):
                    if board[row][col] < 0:
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
