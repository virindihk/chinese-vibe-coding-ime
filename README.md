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
| **F1** / ⌘⇧1 / ^⇧1 | `说中文` | 让 AI 用中文回答 / 描述需求 |
| **F2** / ⌘⇧2 / ^⇧2 | `继续` | AI 生成到一半停了，催它输出 |
| **F3** / ⌘⇧3 / ^⇧3 | `还是报错` | AI 说修好了，一跑又崩了 |
| **F4** / ⌘⇧4 / ^⇧4 | `你改了啥` | AI 偷偷改了一堆文件，想看 diff |
| **F5** / ⌘⇧5 / ^⇧5 | `先别重构` | AI 突然想重写整个项目，赶紧按住 |
| **F6** / ⌘⇧6 / ^⇧6 | `回滚回滚` | 彻底搞砸了，一键回到上一版本 |

**特点：**
- ✅ 一键输入，**自动回车**
- ✅ 全局生效，在任何输入框都能用（IDE、浏览器、微信、飞书……）
- ✅ **macOS + Windows 双平台支持**
- ✅ 备选快捷键，无需担心 F1 被系统占用
- ✅ 随时可改词，改完立即生效

---

## 🍎 macOS 安装

基于 [Hammerspoon](https://www.hammerspoon.org/)。

```bash
# 1. 安装 Hammerspoon
brew install --cask hammerspoon

# 2. 复制配置
mkdir -p ~/.hammerspoon
cp init.lua ~/.hammerspoon/init.lua

# 3. 启动并授权辅助功能
open -a Hammerspoon
```

前往 **系统设置 → 隐私与安全性 → 辅助功能**，开启 **Hammerspoon** 权限，然后点击菜单栏图标 **Reload Config**。

<details>
<summary>macOS F1 键冲突解决</summary>

macOS 默认 F1 是调亮度。三种方案：

| 方案 | 操作 |
|:-----|:-----|
| **A（推荐）** | 系统设置 → 键盘 → 键盘快捷键 → 功能键 → 勾选「将 F1、F2 等键用作标准功能键」 |
| **B** | 直接按 **Fn + F1** ~ **Fn + F6** |
| **C** | 使用备选快捷键 **Cmd + Shift + 1-6** |

</details>

---

## 🪟 Windows 安装

基于 [AutoHotkey v2](https://www.autohotkey.com/v2/)。

```powershell
# 1. 下载安装 AutoHotkey v2
# https://www.autohotkey.com/v2/

# 2. 双击运行
windows\vibe-coding-ime.ahk
```

右下角出现键盘图标即表示运行中。

<details>
<summary>Windows 进阶：编译成 exe / 开机自启</summary>

**编译成独立 exe（无需安装 AutoHotkey）：**
右键 `vibe-coding-ime.ahk` → **Compile Script**，会生成独立可执行文件。

**开机自启：**
把 `vibe-coding-ime.exe` 放入启动文件夹：
按 `Win + R` → 输入 `shell:startup` → 回车，把 exe 拖进去。

**控制快捷键：**
- **F12** = 暂停 / 恢复
- **Ctrl + Alt + R** = 重新加载脚本

</details>

---

## 🛠️ 自定义词库

### macOS
编辑 `~/.hammerspoon/init.lua`，修改 `vibeCodingPhrases` 后 Reload Config。

### Windows
编辑 `windows/vibe-coding-ime.ahk`，修改对应按键后按 `Ctrl + Alt + R` 生效。

```lua
-- macOS 示例
F3  = "还是报错",

-- Windows 示例（AHK v2）
F3:: {
    SendInput("还是报错")
    Sleep(50)
    Send("{Enter}")
}
```

---

## 📂 项目结构

```
.
├── init.lua                 # macOS Hammerspoon 配置
├── windows/
│   ├── vibe-coding-ime.ahk  # Windows AutoHotkey v2 脚本
│   └── README.md            # Windows 详细说明
├── assets/
│   └── keyboard.webp        # 项目灵感图
├── README.md
└── LICENSE
```

---

## 🤝 贡献

欢迎提交 Issue 和 PR！

- 有新的「Vibe Coding 经典语录」？欢迎补充
- 想支持 Linux 版本？大力欢迎
- 发现 Bug？随时提 Issue

---

## 📄 License

MIT © [virindihk](https://github.com/virindihk)

---

<p align="center">
  <sub>Made with 🧋 and rage against AI hallucinations</sub>
</p>
