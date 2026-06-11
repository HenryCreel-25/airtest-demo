from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir="./log/shop",
               devices=["Android://127.0.0.1:7555"])

def test_shop():
    wait(Template(r"screenshots/login_lobby.png", threshold=0.8), timeout=10)

    touch(Template(r"screenshots/shop_entry.png"))

    wait(Template(r"screenshots/shop_title.png", threshold=0.7), timeout=15)

    touch(Template(r"screenshots/shop_tab_costume.png"))
    sleep(1)

    touch(Template(r"screenshots/shop_item.png", threshold=0.7))

    assert_exists(Template(r"screenshots/shop_buy_btn.png", threshold=0.8),
                  "购买按钮未出现")

    touch(Template(r"screenshots/common_back_btn.png"))

if __name__ == "__main__":
    test_shop()
