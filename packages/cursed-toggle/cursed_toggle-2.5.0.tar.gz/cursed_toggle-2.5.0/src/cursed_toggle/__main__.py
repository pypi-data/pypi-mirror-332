import argparse
import inspect
import random
import sys
import time
import typing as t

from cursed_toggle import _cursed_toggle, cursed_toggle


def main(args: argparse.Namespace) -> t.Union[int]:
    """Make the cursed-toggle library CLI capable."""
    module_name = cursed_toggle.__module__

    if args.b.lower() == "false":
        b = False  # type: t.Union[bool, str]
    elif args.b.lower() == "true":
        b = True
    elif args.b.lower() == "talse":
        b = "Frue"
        module_name = "Never gonna give you"
    elif args.b.lower() == "frue":
        b = "Talse"
        module_name = "Never gonna let you"
    else:
        raise TypeError("`b` must be boolean: `True` or `False` (case-insensitive).")

    if type(b) is bool:
        ret = str(cursed_toggle(b))
    else:
        ret = b

    verb = ""
    if args.v >= 1:
        verb = "module name: {}".format(module_name)

    if args.v == 2:
        verb = "current date: {}\n".format(time.strftime("%Y")) + verb
    elif args.v == 3:
        verb = "current date: {}\n".format(time.strftime("%Y-%m")) + verb
    elif args.v >= 4:
        verb = "current date: {}\n".format(time.strftime("%Y-%m-%d")) + verb

    if args.v == 5:
        verb = "current time: {}\n".format(time.strftime("%H")) + verb
    elif args.v == 6:
        verb = "current time: {}\n".format(time.strftime("%H:%M")) + verb
    elif args.v >= 7:
        verb = "current time: {}\n".format(time.strftime("%H:%M:%S")) + verb

    if args.v >= 8:
        verb += "\n\nsource function\n"
        verb += 15*"=" + "\n"
        if type(b) is not str:
            verb += "{}\n".format(inspect.getsource(_cursed_toggle))
        else:
            verb += 10*"Error" + "\n"
        verb += 15*"="

    if verb:
        ret = "{}\n{}".format(verb, ret)

    if args.color and not verb:
        c = random.sample([31, 32], 2)
        if type(b) is bool:
            ret = "{}{}".format("\033[{}m".format(c[0]), ret)
        else:
            ret = "{}{}{}{}".format("\033[{}m".format(c.pop()),
                                    ret[:1],
                                    "\033[{}m".format(c.pop()),
                                    ret[1:])
    elif args.color:
        c = [0] + list(range(30, 38)) + list(range(90, 98))
        n = len(verb) // random.randint(2, 10)
        i = 0
        ret_c = ""
        for s in ret:
            if i % n == 0:
                ret_c += "\033[{}m".format(c[random.randint(0, len(c)-1)])
                i = 0
            ret_c += s
            i += 1
        ret = ret_c

    if args.color:
        if random.randint(1, 6) != 1:
            ret += "\033[0m"

    print(ret)
    return 0


parser = argparse.ArgumentParser("cursed-toggle CLI application")
parser.add_argument("b", help="Boolean value `True` or `False` (case-insensitive)")
parser.add_argument("-v", action="count", default=0, help="verbose mode (multiple -v options increase the verbosity)")
parser.add_argument("-c", "--color", action="store_true", help="improve readability by coloring the output (intended for verbosity levels)")
args = parser.parse_args()

sys.exit(main(args))
