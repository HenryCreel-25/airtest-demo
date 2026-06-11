# 任务 1 完整操作教程

## 第一阶段：安装软件（约 30 分钟）

### 步骤 1：安装 Python 依赖

打开 PowerShell，逐条执行：

```powershell
# 如果下载慢，换清华源
pip install airtest pocoui opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple
```

验证安装：

```powershell
python -c "from airtest.core.api import *; print('安装成功')"
```

### 步骤 2：安装 MuMu 模拟器

1. 浏览器打开 https://mumu.163.com/
2. 下载 Windows 版，双击安装
3. 安装完成后启动模拟器
4. 在模拟器内完成 Android 初始化（登录 Google 或跳过）
5. 打开模拟器顶部的设置图标 → **关于** → 连续点击"版本号" 7 次，打开开发者选项
6. 进入 **开发者选项** → 打开 **USB 调试**
7. 记下模拟器端口（默认 127.0.0.1:7555）

> MuMu 和 Airtest 都是网易出品，兼容性最好。蓝叠或雷电模拟器也可以，但端口号不同。

### 步骤 3：安装游戏

1. 在模拟器内打开浏览器，搜索"第五人格 官网"
2. 下载 APK 文件
3. 安装后打开游戏，完成新手引导（进到大厅即可）
4. 如果已有账号可以先登录，没有的话用测试账号

### 步骤 4：安装 AirtestIDE

1. 打开 http://airtest.netease.com/
2. 点击 Windows 版下载
3. 解压到任意目录（无需安装，绿色版）
4. 双击 `AirtestIDE.exe` 启动

---

## 第二阶段：截取模板图片（约 20 分钟）

模板图片是 Airtest 的核心——它通过对比这些图片来找到屏幕上的按钮。

### 操作流程

1. 启动 AirtestIDE
2. 点击左侧 **设备窗** → **Android** → **远程设备连接**
3. 输入 `Android://127.0.0.1:7555`，点击连接
4. 连接成功后，右侧会显示模拟器画面

### 截图方法

在 AirtestIDE 中：
1. 操作模拟器上的游戏，进入需要截图的界面（如登录页）
2. 在 AirtestIDE 右侧画面中，用鼠标框选目标区域（如"登录按钮"）
3. 点击工具栏上的 **截图** 图标，或按快捷键 Ctrl+Shift+C
4. 在弹出的对话框中给截图命名，保存到项目的 `screenshots/` 目录

### 需要截取的图片

参照 [screenshots/README.md](screenshots/README.md) 中的清单，逐一截取。大约需要截 20 张左右。

> 截图要点：
> - 框选范围尽量小（只框目标按钮，不要包含背景）
> - 在不同光照/时间下截的图可能匹配不上，建议一次性截完
> - 分辨率要保持一致（模拟器固定 1280×720）

---

## 第三阶段：编写测试脚本（代码已完成）

项目中的 5 个测试脚本已经写好，你不需要修改核心逻辑。将截图放入 `screenshots/` 后，脚本就能直接运行。

每个脚本的结构都是：
```python
# 1. 连接设备
# 2. 等待目标界面加载
# 3. 模拟点击 / 输入
# 4. 断言结果
```

### 理解关键 API

| API | 作用 | 示例 |
|-----|------|------|
| `wait(Template("x.png"), timeout=10)` | 等待图片出现，超时则失败 | 等登录界面加载 |
| `touch(Template("x.png"))` | 点击图片所在位置 | 点登录按钮 |
| `text("hello")` | 输入文字 | 输入账号 |
| `swipe(start, end)` | 滑动 | 滑动角色列表 |
| `assert_exists(Template("x.png"))` | 断言图片存在 | 验证登录成功 |
| `sleep(1)` | 等待 1 秒 | 等动画播放完 |

---

## 第四阶段：运行测试（约 10 分钟）

### 前提

- 模拟器已启动，游戏已进入大厅
- 所有模板图片已放入 `screenshots/`
- Python 依赖已安装

### 运行

```powershell
cd airtest-2048-demo

# 运行单个（建议先跑登录测试，确认截图和连接都正常）
python tests/test_login.py

# 全部运行
python run_all.py
```

### 如果失败，检查

1. **连接失败** → 确认模拟器端口正确（默认 7555），模拟器开启了 USB 调试
2. **图片匹配不上** → 确认截图分辨率和当前一致，适当降低 `threshold` 到 0.6
3. **AirtestIDE 连接不上** → 关闭模拟器重启，或在终端执行 `adb kill-server && adb start-server`
4. **游戏闪退** → 模拟器内存不足，在模拟器设置中分配至少 2GB

---

## 第五阶段：查看结果

测试运行日志会保存在项目根目录的 `log/` 文件夹中：

```
log/
├── login/
│   └── 1764662344/        # 时间戳文件夹
│       ├── log.txt        # 文本日志
│       ├── 1.png          # 每一步的截图
│       └── ...
├── shop/
└── ...
```

Airtest 的特色是每一步操作都会自动截图，方便回溯定位问题。打开 AirtestIDE → **文件** → **打开报告** → 选择 log 目录即可查看图文并茂的测试报告。

---

## 第六阶段：上传 GitHub

```powershell
cd airtest-2048-demo
git init
git add -A
git commit -m "init: Airtest demo with 5 test cases"
git remote add origin git@github.com:HenryCreel-25/airtest-2048-demo.git
git push -u origin master
```

注意：`screenshots/*.png` 会一并上传（模板图片是测试的一部分）。

---

## 时间估算

| 阶段 | 时间 |
|------|------|
| 下载模拟器 + 游戏 | 30 分钟 |
| 安装 Python 依赖 | 5 分钟 |
| 截取模板图片 | 20 分钟 |
| 调试运行 | 15 分钟 |
| 合计 | **约 70 分钟** |
