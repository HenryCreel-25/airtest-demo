# 操作指南

## 1. 安装环境

**Python 依赖**

```powershell
pip install airtest pocoui opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple
```

验证：`python -c "from airtest.core.api import *; print('ok')"`

**MuMu 模拟器**

1. 下载 [MuMu 模拟器](https://mumu.163.com/)
2. 安装后启动，在设置 → 关于 → 连点"版本号"7 次打开开发者选项
3. 开发者选项中开启 USB 调试
4. 默认端口 127.0.0.1:7555

**游戏**

在模拟器浏览器中搜索"第五人格 官网"，下载 APK 安装，完成新手引导进入大厅。

**AirtestIDE**

从 [官网](http://airtest.netease.com/) 下载解压。用于截图，不需要用它执行脚本。

## 2. 截图

在模拟器中用 AirtestIDE 对以下界面元素截图，保存为 PNG 放入项目根目录的 `screenshots/` 目录：

- 登录页：账号输入框、密码输入框、登录按钮
- 大厅页：大厅界面
- 角色页：入口按钮、列表标题、角色头像、角色详情
- 商店页：入口按钮、标题、分类标签、商品图标、购买按钮
- 背包页：入口按钮、标题、物品列表、物品图标、详情弹窗
- 设置页：入口按钮、标题、音量滑块、音效开关
- 通用返回按钮

完整截图清单见 README 的「截图准备」章节。

## 3. 运行测试

```powershell
cd airtest-demo
python tests/test_login.py    # 先跑一个测试验证环境
python run_all.py             # 全部执行
```

常见问题：

- 连接失败：检查 MuMu 模拟器端口是否仍为 7555，确认 USB 调试已开启。
- 图片匹配不上：可能是模拟器分辨率变化导致，可将 threshold 降到 0.6 尝试；也可在 AirtestIDE 中重新截图。
- AirtestIDE 连不上模拟器：执行 `adb kill-server && adb start-server` 后重试。

## 4. 日志

每次运行后 `log/` 目录中会生成带截图的结果日志。
