from pyrpg import *

_default_actions = {
    "nest": [
        Action(name="меню", code="меню"),
        Action(name="выйти из игры", code="выйти из игры"),
        Action(name="выйти", code="выйти"),
    ]
}


def main(gm: Game):
    while gm.is_playing():
        outside_actions = {
            "outside_start": [
                Action(name="осмотреться", code="осмотреться"),
            ],
            "outside_look_around": [
                Action(name="зайти в кафе", code="зайти в кафе"),
                Action(name="зайти в бк", code="бк"),
                Action(name="подойти к бомжу", code="бомж"),
            ],
        }

        cafe_actions = {
            "cafe": [
                Action(name="купить кофе", code="кофе"),
                Action(name="купить раф", code="рай"),
            ]
        }

        fight_club_actions = {
            "fk_start": [
                Action(name="купить кофе", code="кофе"),
                Action(name="купить раф", code="рай"),
            ]
        }

        outside_loc = Location(name="улитса", actions=outside_actions)
        _cafe_loc = Location(name="кафе", actions=cafe_actions)
        _fight_club_loc = Location(name="БК", actions=fight_club_actions)

        outside_loc.enter()


if __name__ == "__main__":
    game = Game()
    game.start(main, "Добро пожалуйста")
