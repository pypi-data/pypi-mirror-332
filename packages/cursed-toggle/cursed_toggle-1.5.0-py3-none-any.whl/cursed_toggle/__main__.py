import argparse
import sys

from cursed_toggle import cursed_toggle


def main(args: argparse.Namespace) -> int:
    """Make the cursed-toggle library CLI capable."""
    if args.b.lower() == "false":
        b = False
    elif args.b.lower() == "true":
        b = True
    else:
        raise TypeError("`b` must be boolean: `True` or `False` (case-insensitive).")

    ret = cursed_toggle(b)
    if args.verbose:
        print("{} {}".format(cursed_toggle.__module__, ret))
    else:
        print(ret)
    return 0


parser = argparse.ArgumentParser("cursed-toggle CLI application")
parser.add_argument("b", help="Boolean value `True` or `False` (case-insensitive)")
parser.add_argument("-v", "--verbose", action="store_true", help="show the cursed_toggle source")
args = parser.parse_args()

sys.exit(main(args))
