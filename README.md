# 🇨🇳 中文 Vibe Coding 输入法

> 专为中文开发者设计的 Vibe Coding 快捷输入工具。按 **F1-F6**，一键输出程序员与 AI 结对编程时的经典语录，自动回车发送。

<p align="center">
  <img src="assets/keyboard.webp" alt="中文 Vibe Coding 键盘" width="500">
</p>

*灵感来源：那张在开发者圈子里疯传的 6 键小键盘 meme*

---

## ✨ 功能

| 按键 | 输出内容 | 使用场景 |
|:----:|:---------|:---------|
| **F1** | `说中文` | 让 AI 用中文回答 / 描述需求 |
| **F2** | `继续` | AI 生成到一半停了，催它输出 |
| **F3** | `还是报错` | AI 说修好了，一跑又崩了 |
| **F4** | `你改了啥` | AI 偷偷改了一堆文件，想看 diff |
| **F5** | `先别重构` | AI 突然想重写整个项目，赶紧按住 |
| **F6** | `回滚回滚` | 彻底搞砸了，一键回到上一版本 |

**特点：**
- ✅ 一键输入，**自动回车**
- ✅ 全局生效，在任何输入框都能用（IDE、浏览器、微信、飞书……）
- ✅ **macOS + Windows + Linux 三平台支持**
- ✅ 备选快捷键，无需担心 F1 被系统占用
- ✅ 随时可改词，改完立即生效

---

## 🍎 macOS

基于 [Hammerspoon](https://www.hammerspoon.org/)。

```bash
brew install --cask hammerspoon
mkdir -p ~/.hammerspoon
cp init.lua ~/.hammerspoon/init.lua
open -a Hammerspoon
```

前往 **系统设置 → 隐私与安全性 → 辅助功能**，开启 **Hammerspoon** 权限，点击菜单栏图标 **Reload Config**。

**备选快捷键:** `Cmd + Shift + 1-6`

---

## 🪟 Windows

基于 [AutoHotkey v2](https://www.autohotkey.com/v2/)。

```powershell
# 1. 安装 AutoHotkey v2
# https://www.autohotkey.com/v2/

# 2. 双击运行
windows\vibe-coding-ime.ahk
```

**进阶:** 右键脚本 → **Compile Script** 可生成独立 exe，无需安装 AutoHotkey。

**控制键:** `F12` 暂停/恢复 · `Ctrl + Alt + R` 重载

---

## 🐧 Linux

基于 Python + `keyboard` + `xdotool`/`ydotool`。

```bash
# Debian / Ubuntu
sudo apt install python3-pip xdotool
pip3 install keyboard

# 运行
python3 linux/vibe-coding-ime.py
```

> **权限:** 需要把用户加入 `input` 组才能监听全局热键：
> ```bash
> sudo usermod -aG input $USER
> # 重新登录后生效
> ```

**备选快捷键:** `Ctrl + Shift + 1-6` · **F12** 暂停/恢复

**开机自启:** 自带 systemd 用户服务文件，详见 [linux/README.md](linux/README.md)。

---

## 🛠️ 自定义词库

| 平台 | 修改文件 |
|:-----|:---------|
| macOS | `~/.hammerspoon/init.lua` → Reload Config |
| Windows | `windows/vibe-coding-ime.ahk` → `Ctrl + Alt + R` |
| Linux | `linux/vibe-coding-ime.py` → 重启脚本 |

---

## 📂 项目结构

```
.
├── init.lua                      # macOS Hammerspoon 配置
├── windows/
│   ├── vibe-coding-ime.ahk       # Windows AutoHotkey v2 脚本
│   └── README.md                 # Windows 详细说明
├── linux/
│   ├── vibe-coding-ime.py        # Linux Python 脚本
│   ├── vibe-coding-ime.service   # systemd 用户服务
│   └── README.md                 # Linux 详细说明
├── assets/
│   └── keyboard.webp             # 项目灵感图
├── README.md
└── LICENSE
```

---

## 🤝 贡献

欢迎提交 Issue 和 PR！

- 有新的「Vibe Coding 经典语录」？欢迎补充
- 发现 Bug？随时提 Issue

---

## 📄 License

MIT © [virindihk](https://github.com/virindihk)

---

<p align="center">
  <sub>Made with 🧋 and rage against AI hallucinations</sub>
</p>
