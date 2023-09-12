import random
import sys

colors = "\033[1;31m", "\033[1;34m", "\033[1;36m", "\033[0;32m", "\033[1;35m"


def color():
    sys.stdout.write(random.choice(colors))
    return
