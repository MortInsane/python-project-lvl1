#!/usr/bin/env python3

from brain_games.games.gcd import game_logic
from brain_games.game_engine import run_game


def main():
    run_game(game=game_logic)


if __name__ == '__main__':
    main()
