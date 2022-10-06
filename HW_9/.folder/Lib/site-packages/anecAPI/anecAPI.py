from modern_jokes import modern_jokes
from soviet_jokes import soviet_jokes
import random
import argparse


def soviet_joke():
    return random.choice(soviet_jokes)


def modern_joke():
    return random.choice(modern_jokes)


def random_joke():
    return random.choice(soviet_jokes + modern_jokes)


# TODO: Auto-generated jokes

if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=True,
                                     description='Displays a funny (or not) USSR/Russian joke (also called anecdote).')

    parser.add_argument("-m", "--modern", action="store_true", help="display a modern Russian joke")
    parser.add_argument("-s", "--soviet", action="store_true", help="display an old USSR joke")
    parser.add_argument("-a", "--any", action="store_true", help="display a USSR/Russian joke (default)")
    args = parser.parse_args()

    if args.modern:
        print(modern_joke())
    elif args.soviet:
        print(soviet_joke())
    else:
        print(random_joke())
