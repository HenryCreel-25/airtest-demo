from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir="./log/create_character",
               devices=["Android://127.0.0.1:7555"])

def test_create_character():
    wait(Template(r"screenshots/login_lobby.png", threshold=0.8), timeout=10)

    touch(Template(r"screenshots/character_entry.png"))
    sleep(1)

    wait(Template(r"screenshots/character_list_title.png", threshold=0.7),
         timeout=15)

    swipe((400, 300), (100, 300), duration=0.5)
    sleep(0.5)

    touch(Template(r"screenshots/character_portrait.png", threshold=0.7))

    assert_exists(Template(r"screenshots/character_detail.png", threshold=0.7),
                  "角色详情页未出现")

if __name__ == "__main__":
    test_create_character()
