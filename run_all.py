import sys, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = [
    "tests/test_login.py",
    "tests/test_create_character.py",
    "tests/test_shop.py",
    "tests/test_inventory.py",
    "tests/test_settings.py",
]

def main():
    passed = 0
    failed = 0
    for s in SCRIPTS:
        path = os.path.join(HERE, s)
        print(f">>> {s}")
        r = subprocess.run([sys.executable, path], cwd=HERE)
        if r.returncode == 0:
            passed += 1
            print(f"    PASS")
        else:
            failed += 1
            print(f"    FAIL ({r.returncode})")

    print(f"\n{passed} passed, {failed} failed")
    return failed

if __name__ == "__main__":
    sys.exit(main())
