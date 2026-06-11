# -*- coding: utf-8 -*-
"""
角色创建 / 选择测试。
前提：已登录进入大厅。
"""

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__,
               logdir="./log/create_character",
               devices=["Android://127.0.0.1:7555"])


def test_create_character():
    """测试用例：在大厅中进入角色界面，选择一名角色"""
    print("[TEST] 开始角色创建测试")

    # 1. 等待大厅界面（确保已登录）
    wait(Template(r"screenshots/login_lobby.png", threshold=0.8),
         timeout=10)

    # 2. 点击"角色/幸存者"入口按钮
    touch(Template(r"screenshots/character_entry.png"))
    sleep(1)

    # 3. 等待角色列表界面加载
    wait(Template(r"screenshots/character_list_title.png", threshold=0.7),
         timeout=15)

    # 4. 滑动选择角色（假设列表支持横向滑动）
    swipe((400, 300), (100, 300), duration=0.5)
    sleep(0.5)

    # 5. 点击一个具体角色
    touch(Template(r"screenshots/character_portrait.png", threshold=0.7))

    # 6. 断言：角色详情页出现
    assert_exists(Template(r"screenshots/character_detail.png", threshold=0.7),
                  "角色选择失败：详情页未出现")

    print("[PASS] 角色创建测试通过")


if __name__ == "__main__":
    test_create_character()
