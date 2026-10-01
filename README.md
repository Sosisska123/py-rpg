## Quick Start

### Use as a Python library

```python
from pyrpg import *


def main(gm: Game):
    gm.print("Ты находишся в городе")


if __name__ == "__main__":
    game = Game()
    game.start(main, "Добро пожалуйста", game)

```
