from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir="./log/login",
               devices=["Android://127.0.0.1:7555"])

def test_login():
    wait(Template(r"screenshots/login_account_input.png",
                  threshold=0.8, record_pos=(0.2, 0.3)),
         timeout=30, interval=1)

    touch(Template(r"screenshots/login_account_input.png"))
    text("testuser_001")

    touch(Template(r"screenshots/login_password_input.png"))
    text("password123")

    touch(Template(r"screenshots/login_btn.png"))

    assert_exists(Template(r"screenshots/login_lobby.png", threshold=0.8),
                  "大厅未出现")

if __name__ == "__main__":
    test_login()
