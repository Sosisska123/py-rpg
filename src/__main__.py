from pyrpg.action import Action
from pyrpg.game import Game

game = Game()


def actions_start():
    actions = [
        Action(name="Осмотретсья", handler=look_around),
        Action(name="меню", handler=lambda: print("Menu")),
    ]
    return actions


def look_around() -> None:
    return


def main():
    while game.is_playing():
        pass


game.start(main, "Добро пожалуйста")
