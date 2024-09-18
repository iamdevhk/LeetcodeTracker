class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res=[]
        for i in range(len(board)):
            for j in range(len(board[0])):
                element=board[i][j]
                if element!=".":
                    res+=[(i,element),(element,j),(i//3,j//3,element)]
        return len(res)==len(set(res))