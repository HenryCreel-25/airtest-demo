# 第五人格 Airtest 自动化测试

基于 Airtest 的《第五人格》手游 UI 自动化测试，覆盖登录、角色选择、商店、背包、设置五个核心模块。

## 环境

- Python 3.8+
- MuMu 模拟器（默认端口 127.0.0.1:7555）
- 《第五人格》APK（需完成新手引导进入大厅）

## 安装

```bash
pip install -r requirements.txt
```

下载慢可换国内镜像：

```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 截图准备

测试依赖模板图片进行图像识别匹配。在模拟器中用 AirtestIDE 对以下界面元素截图，保存为 PNG 放入 `screenshots/` 目录：

- 登录页：账号输入框、密码输入框、登录按钮
- 大厅页：大厅界面（验证登录成功后的状态）
- 角色页：入口按钮、列表标题、角色头像、角色详情
- 商店页：入口按钮、标题、分类标签、商品图标、购买按钮
- 背包页：入口按钮、标题、物品列表、物品图标、详情弹窗
- 设置页：入口按钮、标题、音量滑块、音效开关
- 通用：返回按钮

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
