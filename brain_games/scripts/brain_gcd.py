#!/usr/bin/env python3

from brain_games.games import gcd
from brain_games.game_engine import launch_game


def main():
    launch_game(gcd)


if __name__ == '__main__':
    main()
