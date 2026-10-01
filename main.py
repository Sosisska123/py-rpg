from pyrpg.action import Action
from pyrpg.game import Game
from pyrpg.location import Location


def main(gm: Game):
    loc = Location(name="City")
    gm.print(f"Ты находишся в {loc}")
    choice = gm.choice([Action("", lambda: "end")], message="Что ты выберешь?")
    if choice.handler() == "end":
        gm.end()
        # gm.end("Хороашя концовка")


if __name__ == "__main__":
    game = Game()
    game.start(main, "Добро пожалуйста", game)
