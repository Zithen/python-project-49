#!/usr/bin/env python3
from brain_games.scripts import brain_calc
from brain_games.games import gcd_game


def main():
    brain_calc.engine(gcd_game)


if __name__ == '__main__':
    main()
