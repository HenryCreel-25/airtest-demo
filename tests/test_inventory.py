from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir="./log/inventory",
               devices=["Android://127.0.0.1:7555"])

def test_inventory():
    wait(Template(r"screenshots/login_lobby.png", threshold=0.8), timeout=10)

    touch(Template(r"screenshots/inventory_entry.png"))

    wait(Template(r"screenshots/inventory_title.png", threshold=0.7), timeout=10)

    assert_exists(Template(r"screenshots/inventory_has_items.png", threshold=0.7),
                  "背包列表为空")

    touch(Template(r"screenshots/inventory_item.png", threshold=0.7))
    sleep(0.5)

    assert_exists(Template(r"screenshots/inventory_item_detail.png", threshold=0.7),
                  "物品详情弹窗未出现")

if __name__ == "__main__":
    test_inventory()
