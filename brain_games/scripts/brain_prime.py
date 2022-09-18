#!/usr/bin/env python3

from brain_games.games import prime
from brain_games.game_engine import launch_game


def main():
    launch_game(prime)


if __name__ == '__main__':
    main()
