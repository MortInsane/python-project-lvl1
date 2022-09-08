#!/usr/bin/env python3

from brain_games.games import gcd
from brain_games.game_engine import run_game


def main():
    run_game(game=gcd)


if __name__ == '__main__':
    main()
