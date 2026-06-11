# -*- coding: utf-8 -*-
"""
设置页面测试。
前提：已登录进入大厅。
"""

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__,
               logdir="./log/settings",
               devices=["Android://127.0.0.1:7555"])


def test_settings():
    """测试用例：打开设置页面，修改一项设置"""
    print("[TEST] 开始设置页面测试")

    # 1. 确认在大厅
    wait(Template(r"screenshots/login_lobby.png", threshold=0.8), timeout=10)

    # 2. 点击设置入口（通常是齿轮图标）
    touch(Template(r"screenshots/settings_entry.png"))

    # 3. 等待设置界面加载
    wait(Template(r"screenshots/settings_title.png", threshold=0.7), timeout=10)

    # 4. 断言：设置界面存在音量滑块（验证设置界面正常）
    assert_exists(Template(r"screenshots/settings_volume_slider.png", threshold=0.7),
                  "设置界面加载失败")

    # 5. 点击音效开关切换状态
    touch(Template(r"screenshots/settings_sound_toggle.png"))
    sleep(0.5)

    # 6. 断言：切换后的状态显示正确
    assert_exists(Template(r"screenshots/settings_sound_off.png", threshold=0.7),
                  "音效开关切换失败")

    # 7. 关闭设置页
    touch(Template(r"screenshots/common_back_btn.png"))

    print("[PASS] 设置页面测试通过")


if __name__ == "__main__":
    test_settings()
