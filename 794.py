from typing import List

class Solution:

  def win(self, board: List[str], p: str) -> bool:
    return any(board[i][0] == p and board[i][1] == p and board[i][2] == p or
                board[0][i] == p and board[1][i] == p and board[2][i] == p for i in range(3)) or \
                board[0][0] == p and board[1][1] == p and board[2][2] == p or \
                board[0][2] == p and board[1][1] == p and board[2][0] == p

  def validTicTacToe(self, board: List[str]) -> bool:
    oCount = sum([row.count('O') for row in board])
    xCount = sum([row.count('X') for row in board])
    if xCount - oCount != 1 and xCount - oCount != 0:
      return False
    if self.win(board, 'X') and self.win(board, 'O'):
      return False
    if self.win(board, 'X') and xCount - oCount != 1:
      return False
    if self.win(board, 'O') and xCount != oCount:
      return False
    return True

