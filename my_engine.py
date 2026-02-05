import chess

def choose_move(board):
    # Pick first legal move (replace with points-based system later)
    legal_moves = list(board.legal_moves)
    if not legal_moves:
        return None
    return legal_moves[0].uci()
