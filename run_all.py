# -*- coding: utf-8 -*-
"""
一键运行所有测试用例。
用法：python run_all.py
"""

import sys
import os
import subprocess

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_SCRIPTS = [
    "tests/test_login.py",
    "tests/test_create_character.py",
    "tests/test_shop.py",
    "tests/test_inventory.py",
    "tests/test_settings.py",
]

def main():
    passed = 0
    failed = 0

    print("=" * 50)
    print("  2048 / 第五人格 Airtest 自动化测试")
    print("=" * 50)

    for script in TEST_SCRIPTS:
        path = os.path.join(TEST_DIR, script)
        print(f"\n>>> 运行: {script}")
        result = subprocess.run(
            [sys.executable, path],
            capture_output=False,
            cwd=TEST_DIR,
        )
        if result.returncode == 0:
            passed += 1
            print(f"<<< {script}: PASS")
        else:
            failed += 1
            print(f"<<< {script}: FAIL (exit code {result.returncode})")

    print("\n" + "=" * 50)
    print(f"  结果: {passed} passed, {failed} failed")
    print("=" * 50)

    return failed


if __name__ == "__main__":
    sys.exit(main())
