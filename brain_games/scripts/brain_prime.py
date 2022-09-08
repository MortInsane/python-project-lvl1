#!/usr/bin/env python3

from brain_games.games import prime
from brain_games.game_engine import run_game


def main():
    run_game(game=prime)


if __name__ == '__main__':
    main()
