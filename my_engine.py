import chess
import sys

def main():
    board = chess.Board()

    for line in sys.stdin:
        line = line.strip()

        if line == "uci":
            print("id name RomeFish")
            print("uciok")
            sys.stdout.flush()

        elif line == "isready":
            print("readyok")
            sys.stdout.flush()

        elif line.startswith("position"):
            parts = line.split()
            if "moves" in parts:
                moves = parts[parts.index("moves") + 1:]
                for m in moves:
                    board.push_uci(m)

        elif line.startswith("go"):
            move = next(iter(board.legal_moves))
            print(f"bestmove {move.uci()}")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
