# 操作指南

## 1. 装软件

**Python 依赖**

```powershell
pip install airtest pocoui opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple
```

验证：`python -c "from airtest.core.api import *; print('ok')"`

**MuMu 模拟器**

1. 下载 https://mumu.163.com/
2. 装完启动，在设置 → 关于 → 连点"版本号"7 次打开开发者选项
3. 开发者选项里开 USB 调试
4. 默认端口 127.0.0.1:7555

**游戏**

在模拟器浏览器里搜"第五人格 官网"，下 APK 安装，跑完新手引导进大厅。

**AirtestIDE**

http://airtest.netease.com/ 下载解压。用来截图，不需要用它跑脚本。

## 2. 截图

用 AirtestIDE 连接模拟器（设备窗 → Android → 远程设备连接 → 填 `Android://127.0.0.1:7555`），右侧会显示画面。

框选目标区域 → 截图按钮 → 保存到 `screenshots/`。具体需要哪些图看 screenshots/README.md。

要点：框选范围尽量小，分辨率固定 1280×720。

## 3. 跑测试

```powershell
cd airtest-demo
python tests/test_login.py    # 先跑一个试水
python run_all.py             # 全跑
```

常见问题：

- 连接失败：端口对不对，USB 调试开了没
- 图片匹配不上：分辨率变了，或者阈值太高，试试把 threshold 降到 0.6
- AirtestIDE 连不上：`adb kill-server && adb start-server`

## 4. 日志

跑完在 `log/` 目录看结果，每步都有自动截图。
