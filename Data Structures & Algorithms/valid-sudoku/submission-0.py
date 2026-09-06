"""
Some important mentioned in the description. 
The board does not need to be full. 
I understand with the information that is present we need to validate
that not exist duplicates by row, colum and sub-matrix.
"""
class Solution:
    def isValidRows(self, board:List[List[str]]) ->bool:
        for i in range(0,len(board)):
            set_current_row = set()
            for j in range(0,len(board)):
                current_val = board[j][i]
                if current_val!='.':
                    if current_val in set_current_row:
                        return False
                    else:
                        set_current_row.add(current_val)
        return True

    def isValidColums(self, board:List[List[str]]) ->bool:
        for i in range(0,len(board)):
            set_curret_col = set()
            for j in range(0,len(board)):
                current_val = board[i][j]
                if current_val!='.':
                    if current_val in set_curret_col:
                        return False
                    else:
                        set_curret_col.add(current_val)
        return True

    def isValidSubMatrix(self, board: List[List[str]]) -> bool:
        set_id_box = dict()
        for i in range(0,9):
            set_id_box[i] = set()

        for i in range(0,len(board)):
            for j in range(0,len(board)):
                br = i//3
                bc = j//3
                index_box = (br*3) + bc
                current_val = board[i][j]
                if current_val!='.':
                    if current_val in set_id_box[index_box]:
                        return False
                    else:
                        set_id_box[index_box].add(current_val)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isValidSubMatrix(board) and self.isValidColums(board) and self.isValidRows(board)

