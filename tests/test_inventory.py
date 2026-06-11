# -*- coding: utf-8 -*-
"""
背包 / 物品栏查看测试。
前提：已登录进入大厅。
"""

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__,
               logdir="./log/inventory",
               devices=["Android://127.0.0.1:7555"])


def test_inventory():
    """测试用例：打开背包，验证物品列表"""
    print("[TEST] 开始背包测试")

    # 1. 确认在大厅
    wait(Template(r"screenshots/login_lobby.png", threshold=0.8), timeout=10)

    # 2. 点击背包入口
    touch(Template(r"screenshots/inventory_entry.png"))

    # 3. 等待背包界面加载
    wait(Template(r"screenshots/inventory_title.png", threshold=0.7), timeout=10)

    # 4. 断言：背包中有物品图标（证明物品列表正常显示）
    assert_exists(Template(r"screenshots/inventory_has_items.png", threshold=0.7),
                  "背包为空或加载失败")

    # 5. 点击一个物品查看详情
    touch(Template(r"screenshots/inventory_item.png", threshold=0.7))
    sleep(0.5)

    # 6. 断言：物品详情弹窗出现
    assert_exists(Template(r"screenshots/inventory_item_detail.png", threshold=0.7),
                  "物品详情弹窗未出现")

    print("[PASS] 背包测试通过")


if __name__ == "__main__":
    test_inventory()
