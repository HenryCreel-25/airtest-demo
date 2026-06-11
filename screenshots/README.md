# 截图文件目录说明

本目录存放 Airtest 图像识别所需的模板图片。

## 如何截图

1. 打开 **AirtestIDE**（从 http://airtest.netease.com/ 下载解压即可）
2. 连接模拟器（设备窗 -> Android -> 选中 MuMu 模拟器）
3. 进入游戏对应界面
4. 点击 AirtestIDE 工具栏的"截图"按钮，框选目标区域后保存为 .png
5. 将截图放入本目录，文件名必须与测试脚本中 Template() 引用的一致

## 需要的截图清单

### 登录测试 (test_login.py)
| 文件名 | 截图内容 | 截取位置 |
|--------|---------|---------|
| login_account_input.png | 账号输入框 | 游戏登录界面 |
| login_password_input.png | 密码输入框 | 游戏登录界面 |
| login_btn.png | 登录按钮 | 游戏登录界面 |
| login_lobby.png | 大厅界面特征 | 登录成功后的画面 |

### 角色选择测试 (test_create_character.py)
| 文件名 | 截图内容 | 截取位置 |
|--------|---------|---------|
| character_entry.png | 角色入口按钮 | 大厅界面 |
| character_list_title.png | 角色列表标题 | 角色选择界面 |
| character_portrait.png | 一名角色的头像 | 角色选择界面 |
| character_detail.png | 角色详情页特征 | 选中角色后 |

### 商店测试 (test_shop.py)
| 文件名 | 截图内容 |
|--------|---------|
| shop_entry.png | 商店入口按钮 |
| shop_title.png | 商店界面标题 |
| shop_tab_costume.png | 皮肤标签页 |
| shop_item.png | 一个商品图标 |
| shop_buy_btn.png | 购买按钮 |

### 背包测试 (test_inventory.py)
| 文件名 | 截图内容 |
|--------|---------|
| inventory_entry.png | 背包入口按钮 |
| inventory_title.png | 背包界面标题 |
| inventory_has_items.png | 有物品时的背包列表 |
| inventory_item.png | 一个物品图标 |
| inventory_item_detail.png | 物品详情弹窗 |

### 设置测试 (test_settings.py)
| 文件名 | 截图内容 |
|--------|---------|
| settings_entry.png | 设置入口（齿轮图标） |
| settings_title.png | 设置界面标题 |
| settings_volume_slider.png | 音量滑块 |
| settings_sound_toggle.png | 音效开关（开启状态） |
| settings_sound_off.png | 音效开关（关闭状态） |

### 公共
| 文件名 | 截图内容 |
|--------|---------|
| common_back_btn.png | 返回按钮（各界面通用的） |
