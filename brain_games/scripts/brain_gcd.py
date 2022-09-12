#!/usr/bin/env python3

from brain_games.games import gcd
from brain_games.game_engine import launch_engine


def main():
    launch_engine(gcd)


if __name__ == '__main__':
    main()
