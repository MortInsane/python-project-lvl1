#!/usr/bin/env python3

from brain_games.games.progression import GAME_CONDITION, progression_logic
from brain_games.game_engine import run_game


def main():
    run_game(game_condition=GAME_CONDITION, game=progression_logic)


if __name__ == '__main__':
    main()
