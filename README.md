# 第五人格 Airtest 自动化测试 Demo

基于 Airtest 图像识别的《第五人格》手游自动化测试项目，包含 5 个测试用例：登录、角色选择、商店浏览、背包查看、设置修改。

## 环境准备

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

> **换源加速**（如果 pip 下载慢）：
> ```bash
> pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
> ```

requirements.txt 包含：
- `airtest` — 图像识别自动化框架
- `pocoui` — UI 树辅助定位（备选）
- `opencv-python` — 图像匹配引擎

### 2. 安装模拟器

下载 [MuMu 模拟器](https://mumu.163.com/)，安装后在模拟器设置中：
- 开启 **开发者选项** → **USB 调试**
- 记下端口号（默认 7555）

### 3. 安装游戏

在模拟器内从应用商店或官网下载《第五人格》APK 并安装。

### 4. 安装 AirtestIDE（可选，用于截图）

从 [airtest.netease.com](http://airtest.netease.com/) 下载 AirtestIDE，解压即用。主要用来截取模板图片。

### 5. 截取模板图片

参考 [screenshots/README.md](screenshots/README.md) 中的截图清单，逐一截取并放入 `screenshots/` 目录。

## 项目结构

```
airtest-2048-demo/
├── README.md
├── requirements.txt
├── run_all.py                 # 运行所有测试
├── tests/
│   ├── test_login.py          # 登录流程
│   ├── test_create_character.py  # 角色选择
│   ├── test_shop.py           # 商店浏览
│   ├── test_inventory.py      # 背包查看
│   └── test_settings.py       # 设置修改
└── screenshots/
    ├── README.md              # 截图清单与操作指南
    └── *.png                  # 模板图片（需自行截取）
```

## 测试用例

| 用例 | 文件 | 流程 |
|------|------|------|
| 登录 | test_login.py | 输入账号密码 → 点击登录 → 验证大厅出现 |
| 角色选择 | test_create_character.py | 进入角色界面 → 滑动列表 → 选择角色 → 验证详情页 |
| 商店浏览 | test_shop.py | 打开商店 → 切换商品分类 → 点击商品 → 验证购买按钮 |
| 背包查看 | test_inventory.py | 打开背包 → 验证物品列表 → 点击物品 → 验证详情弹窗 |
| 设置修改 | test_settings.py | 打开设置 → 验证滑块存在 → 切换音效 → 验证状态变化 |

## 运行

### 单个测试

```bash
python tests/test_login.py
```

### 全部测试

```bash
python run_all.py
```

## 运行原理

Airtest 通过图像匹配定位屏幕上的 UI 元素：

1. 将 `screenshots/` 中的 .png 图片作为模板
2. 在模拟器截图中搜索匹配区域
3. 匹配成功则模拟点击（`touch`）、输入（`text`）或滑动（`swipe`）
4. `assert_exists` 验证目标元素是否出现，未出现则测试失败

每个测试脚本开头通过 `auto_setup` 连接指定设备。如果是从 AirtestIDE 运行，`cli_setup` 会自动处理设备连接，不需要手动写 `connect_device`。

## 注意事项

- 模板图片必须在和测试时相同的分辨率下截取（建议模拟器固定 1280×720）
- `threshold` 参数控制匹配严格度，取 0.7-0.8 较合适
- 如果游戏更新导致界面变化，需要重新截取模板图片
- 测试日志保存在 `log/` 目录，包含每步的截图和运行记录
