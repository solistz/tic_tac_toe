from board import Board
from user import User_games


def main():
    pole_obj = Board()
    pole_obj.pole_print()
    one_usr = User_games()
    one_usr.user_play()

if __name__ == "__main__":
    main()



