from pyrpg import Action, Game, Location, Player
from pyrpg.components import Bank, Health, MsgStyle


def init_player() -> Player:
    player_health = Health(value=100)
    player_money = Bank(value=100, currency="$")

    return Player(health=player_health, money=player_money)


def init_locations() -> dict[str, Location]:
    outside_actions = [
        Action(action="Осмотреться", code=1),
        Action(action="Идти вперед", code=2),
        Action(action="Выйти", code=3),
        Action(action="Меню", code=4),
    ]
    outside_loc = Location(name="Улица", actions=outside_actions)

    cafe_actions = [
        Action(action="Купить кофе", code=1),
        Action(action="Выйти из кафе", code=2),
        Action(action="Статус", code=3),
    ]
    cafe_loc = Location(name="Кафе", message="ты зашел в кафе", actions=cafe_actions)

    return {"start": outside_loc, "cafe": cafe_loc}


def start_game():
    player = init_player()
    locations = init_locations()

    game = Game(
        start_message="добро пожаловать",
        message_style=MsgStyle.EMPTY,
        save_path="",
        start_location=locations.get("start", Location(name="void")),
        player=player,
    )
    game.load(path="")

    game.start()
    while game.is_playing():
        result = game.current_location().ask_actions()

        match result:
            case 1:
                game.print("ты увидел кафе")
            case 2:
                game.print("ты идшеь вперед")
            case 3:
                game.print("сохранение...")
                game.close_and_save()
            case 4:
                game.print(player.stats())


if __name__ == "__main__":
    start_game()
