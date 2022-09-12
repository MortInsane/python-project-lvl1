#!/usr/bin/env python3

from brain_games.games import calc
from brain_games.game_engine import launch_engine


def main():
    launch_engine(calc)


if __name__ == '__main__':
    main()
