from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir="./log/settings",
               devices=["Android://127.0.0.1:7555"])

def test_settings():
    wait(Template(r"screenshots/login_lobby.png", threshold=0.8), timeout=10)

    touch(Template(r"screenshots/settings_entry.png"))

    wait(Template(r"screenshots/settings_title.png", threshold=0.7), timeout=10)

    assert_exists(Template(r"screenshots/settings_volume_slider.png", threshold=0.7),
                  "设置界面未加载")

    touch(Template(r"screenshots/settings_sound_toggle.png"))
    sleep(0.5)

    assert_exists(Template(r"screenshots/settings_sound_off.png", threshold=0.7),
                  "音效开关状态未切换")

    touch(Template(r"screenshots/common_back_btn.png"))

if __name__ == "__main__":
    test_settings()
