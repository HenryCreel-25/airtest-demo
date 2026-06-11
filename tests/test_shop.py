# -*- coding: utf-8 -*-
"""
商店购买流程测试。
前提：已登录进入大厅。
"""

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__,
               logdir="./log/shop",
               devices=["Android://127.0.0.1:7555"])


def test_shop():
    """测试用例：进入商店，浏览商品，验证购买界面"""
    print("[TEST] 开始商店测试")

    # 1. 确认在大厅
    wait(Template(r"screenshots/login_lobby.png", threshold=0.8), timeout=10)

    # 2. 点击商店入口
    touch(Template(r"screenshots/shop_entry.png"))

    # 3. 等待商店界面加载
    wait(Template(r"screenshots/shop_title.png", threshold=0.7), timeout=15)

    # 4. 切换到不同商品分类（如有 Tab 栏）
    touch(Template(r"screenshots/shop_tab_costume.png"))
    sleep(1)

    # 5. 点击一个商品查看详情
    touch(Template(r"screenshots/shop_item.png", threshold=0.7))

    # 6. 断言：购买按钮出现（说明商品详情正常加载）
    assert_exists(Template(r"screenshots/shop_buy_btn.png", threshold=0.8),
                  "商品详情加载失败：购买按钮未出现")

    # 7. 返回商店列表
    touch(Template(r"screenshots/common_back_btn.png"))

    print("[PASS] 商店测试通过")


if __name__ == "__main__":
    test_shop()
