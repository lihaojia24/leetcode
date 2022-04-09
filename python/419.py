from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        return sum(ch == 'X' and not (i > 0 and board[i - 1][j] == 'X' or j > 0 and board[i][j - 1] == 'X')
                   for i, row in enumerate(board) for j, ch in enumerate(row))
