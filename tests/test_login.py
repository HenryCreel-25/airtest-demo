# -*- coding: utf-8 -*-
"""
登录流程测试。
使用步骤：
  1. 打开 AirtestIDE，连接模拟器
  2. 进入游戏登录界面
  3. 用 AirtestIDE 的截图工具截取本脚本引用的各个按钮图片，
     保存到 screenshots/ 目录
  4. 运行本脚本
"""

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__,
               logdir="./log/login",
               devices=["Android://127.0.0.1:7555"])

# ---- 等待登录界面出现 ----
# 截取游戏登录界面上的"账号输入框"区域保存为 screenshots/login_account_input.png
# 截取"密码输入框"区域保存为 screenshots/login_password_input.png
# 截取"登录按钮"保存为 screenshots/login_btn.png
# 截取"登录后的大厅界面特征"保存为 screenshots/login_lobby.png

def test_login():
    """测试用例：正常登录流程"""
    print("[TEST] 开始登录测试")

    # 1. 等待登录界面加载
    wait(Template(r"screenshots/login_account_input.png",
                  threshold=0.8, record_pos=(0.2, 0.3)),
         timeout=30, interval=1)

    # 2. 点击账号输入框并输入账号
    touch(Template(r"screenshots/login_account_input.png"))
    text("testuser_001")

    # 3. 点击密码输入框并输入密码
    touch(Template(r"screenshots/login_password_input.png"))
    text("password123")

    # 4. 点击登录按钮
    touch(Template(r"screenshots/login_btn.png"))

    # 5. 断言：等待大厅界面出现，验证登录成功
    assert_exists(Template(r"screenshots/login_lobby.png",
                           threshold=0.8),
                  "登录失败：大厅界面未出现")

    print("[PASS] 登录测试通过")


if __name__ == "__main__":
    test_login()
