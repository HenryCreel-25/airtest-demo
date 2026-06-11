# 第五人格 Airtest 自动化测试

5 个测试用例：登录、角色选择、商店、背包、设置。

## 环境

- Python 3.8+
- MuMu 模拟器（默认端口 127.0.0.1:7555）
- 《第五人格》APK

```bash
pip install -r requirements.txt
# or
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 运行

```bash
python tests/test_login.py       # 单个
python run_all.py                # 全部
```

## 结构

```
├── run_all.py
├── tests/
│   ├── test_login.py
│   ├── test_create_character.py
│   ├── test_shop.py
│   ├── test_inventory.py
│   └── test_settings.py
└── screenshots/          # 模板图片（不上传）
```

## 用例

| 用例 | 文件 | 步骤 |
|------|------|------|
| 登录 | test_login.py | 输入账号密码 → 登录 → 检查大厅 |
| 角色选择 | test_create_character.py | 进角色界面 → 选角色 → 检查详情 |
| 商店 | test_shop.py | 进商店 → 切分类 → 点商品 → 检查购买按钮 |
| 背包 | test_inventory.py | 进背包 → 检查列表 → 点物品 → 检查弹窗 |
| 设置 | test_settings.py | 进设置 → 检查滑块 → 切音效 → 检查状态 |
