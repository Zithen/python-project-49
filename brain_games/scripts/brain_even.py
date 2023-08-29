#!/usr/bin/env python
from brain_games.games.engine import engine
from brain_games.games.even_game import even_game


def main():
    engine(even_game())


if __name__ == '__main__':
    main()
