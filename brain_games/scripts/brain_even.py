#!/usr/bin/env python3

from brain_games.games import even
from brain_games.game_engine import launch_engine


def main():
    launch_engine(even)


if __name__ == '__main__':
    main()
