from pyrpg import Action, Game, Location, Player
from pyrpg.components import *


def init_player(start_loc: Location) -> Player:
    player_health = Health(value=100)
    player_money = Bank(value=100, currency="$")

    return Player(name="", location=start_loc, health=player_health, money=player_money)


def init_locations() -> dict[str, Location]:
    outside_actions = [
        Action(name="Осмотреться", code=1),
        Action(name="Идти вперед", code=2),
        Action(name="Выйти", code=3),
        Action(name="Меню", code=4),
    ]
    outside_loc = Location(name="Улица", actions=outside_actions)

    cafe_actions = [
        Action(name="Купить кофе", code=1),
        Action(name="Выйти из кафе", code=2),
        Action(name="Статус", code=3),
    ]
    cafe_loc = Location(name="Кафе", actions=cafe_actions)

    return {"start": outside_loc, "cafe": cafe_loc}


def init_game():
    start_location = Location(name="void", actions=[])
    player = init_player(start_loc=start_location)

    game = Game(
        player=player,
        message_style=AngleBracketMsgStyle(),
        auto_capitalize=True,
        timeout=1,
    )

    return game


def start_game():
    yes_no_acts = [Action(name="да", code="да"), Action(name="нет", code="нет")]

    while game.is_playing():
        location = game.get_current_location()
        game.print(f"ты находишся в {location}!")
        choice = game.choice("что ты выберешь?", location.actions, show_variants=True)
        match choice:
            case 1:
                game.print("ты увидел кафе.")
                choice = game.choice("зайти?", yes_no_acts)

                if choice == "да":
                    game.print("ты зашел кафе.")
                elif choice == "нет":
                    game.print("ты не зашел кафе.")
            case 2:
                game.print("ты идешь вперед")
            case 3:
                game.print("меню")
            case 4:
                game.print("вихiхд")
            case _:
                pass


if __name__ == "__main__":
    game = init_game()
    game.start(start_game, message="добро пожаловать в город")
